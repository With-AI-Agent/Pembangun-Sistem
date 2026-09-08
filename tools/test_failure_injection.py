#!/usr/bin/env python3
"""Executable fail-closed checks for the generic checkpoint contract.

History:
- M-02 (audit 5 Sep 2026): the old checker matched the literal
  `"Pekerjaan belum tersimpan: Tidak ada"` while EVERY real STATUS.md used
  the bold form (some with backticks) — state_is_safe() returned False for
  all four real units, so "4 fail-closed scenarios PASSED" proved nothing.
- Review PR #11 (5 Sep 2026): the tolerant parser still accepted FAKE safety
  evidence (a dirty second field after a safe one, quoted examples, the
  official protocol format `- Status: approved` was invisible), discovered
  units could silently shrink to zero, and the counts were mislabeled.
  The parser now lives in checkpoint_core (single source with
  validate_repo.py), and this file additionally runs the regression
  scenarios R1–R7 that reproduce the review's mutations: deleted core
  source, unregistered system folder, non-backticked INDEKS row, deleted
  unit STATUS, kerangka/siap-pakai lifecycle, and the template bootstrap
  self-containment assertion.

Run with FI_SKIP_NESTED=1 to skip R1–R7 (used when this file is invoked
inside a copied repo by the R scenarios themselves — prevents recursion).
"""
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

import checkpoint_core as core

ROOT = Path(__file__).resolve().parents[1]

# The 5 normalized warnings a clean-template extract MUST produce (and only
# those): labeled master-history references. Any warning elsewhere — above
# all in the bootstrap doc (NEXT_SESSION_PROMPT.md) or the user guide
# (PANDUAN_PENGGUNA.md) — means an active instruction points at a file the
# template does not ship. This set is deliberately exact: it is the
# normalization list of _meta/TEMPLATE_RELEASE.md, pinned here so drift
# fails loudly. (5th pair pinned 6 Sep 2026, meta v1.4.0: the v1.4.0 Log
# Evolusi Bukti cell cites the KK acceptance log as provenance — same
# category as the two earlier SYSTEM_MANIFEST.md history references.)
EXPECTED_TEMPLATE_WARNINGS = {
    ("_meta/00_CARA_KERJA_META.md",
     "sistem-konten-kreator/_sistem/09_AUDIT_MIGRASI_GITHUB_AGENT.md"),
    ("_meta/00_CARA_KERJA_META.md",
     "sistem-konten-kreator/_sistem/00_CARA_PAKAI_SISTEM.md"),
    ("_meta/SYSTEM_MANIFEST.md",
     "sistem-pilot-catatan-belajar/unit-aktif/pilot-002-behavioral/OUTPUT.md"),
    ("_meta/SYSTEM_MANIFEST.md",
     "_sistem/11_LOG_SESI.md"),
    ("_meta/SYSTEM_MANIFEST.md",
     "sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md"),
}

MINI_MANIFEST = """# System Manifest — Sistem Uji Kerangka (skenario FI)

- **Nama sistem:** Sistem Uji Kerangka
- **Tahap:** {tahap}
- **Versi:** `0.0.1`
- **Dipakai via lmarena?** Ya

## Warisan (Kontrak)

| Butir | Status (diterapkan / override) | Letak di folder sistem | Override? |
|---|---|---|---|
| W-01 pegangan | direncanakan | | |
| W-02 LOG_SESI | direncanakan | | |
| W-03 field checkpoint STATUS | direncanakan | | |
| W-04 manifest | diterapkan | SYSTEM_MANIFEST.md | |
| W-05 log keputusan | direncanakan | | |
| W-06 QA 3-lapis | direncanakan | | |
| W-07 fakta platform | diterapkan | bagian di atas | |
| W-08 approval bertingkat | direncanakan | | |
| W-09 ringkasan cadangan | direncanakan | | |
"""


def run_tool(repo: Path, tool: str) -> int:
    """Run a tool against a (possibly modified) repo copy; FI_SKIP_NESTED
    always on so nested FI runs cannot recurse."""
    return subprocess.run(
        [sys.executable, str(repo / tool)],
        capture_output=True, text=True,
        env={**os.environ, "FI_SKIP_NESTED": "1"},
    ).returncode


def index_insert_row(cp: Path, row: str):
    p = cp / "_meta" / "INDEKS_SISTEM.md"
    lines = p.read_text(encoding="utf-8").splitlines()
    in_tbl, last = False, None
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s.startswith("## "):
            in_tbl = s[3:].strip().lower().startswith("daftar sistem")
            continue
        if in_tbl and s.startswith("|"):
            last = i
    if last is None:
        raise RuntimeError("INDEKS_SISTEM: tabel 'Daftar Sistem' tidak ditemukan")
    lines.insert(last + 1, row)
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")


def regression_scenarios(base_dir: Path):
    """R1–R7: the review's mutations, pinned as permanent regressions."""
    checks = []
    with TemporaryDirectory(dir=str(base_dir)) as d:
        cp = Path(d) / "repo"
        shutil.copytree(
            ROOT, cp,
            ignore=shutil.ignore_patterns(
                ".git", "backups", "template_clean", "template_clean.zip"),
        )
        idx = cp / "_meta" / "INDEKS_SISTEM.md"
        idx_backup = idx.read_text(encoding="utf-8")

        # R2 (F2): an unregistered sistem-* folder must fail the validator.
        # The old code skipped any name containing "pilot" — even
        # `sistem-autopilot-data`.
        (cp / "sistem-autopilot-data").mkdir()
        (cp / "sistem-autopilot-data/README.md").write_text("# uji\n", encoding="utf-8")
        checks.append(("R2 sistem tak terdaftar (sistem-autopilot-data) -> validator FAIL",
                       run_tool(cp, "tools/validate_repo.py") != 0))
        shutil.rmtree(cp / "sistem-autopilot-data")

        # R3 (F2): an INDEKS row without the exact backticked folder cell
        # must be a parse error, not silently ignored.
        index_insert_row(cp, "| Sistem Uji | sistem-uji-tanpa-backtick | Sedang dibangun | 2026-09-05 | uji FI R3 |")
        checks.append(("R3 baris INDEKS tanpa backtick -> validator FAIL (parse ketat)",
                       run_tool(cp, "tools/validate_repo.py") != 0))
        idx.write_text(idx_backup, encoding="utf-8")

        # R5/R6 (F9): build-stage lifecycle. Same skeleton system:
        #   Tahap: kerangka  -> missing W-01/W-02/W-03 artifacts = warnings, PASS
        #   Tahap: siap-pakai -> same artifacts = errors, FAIL
        for tahap, expect in (("kerangka", 0), ("siap-pakai", 1)):
            name = f"sistem-uji-{tahap}"
            (cp / name).mkdir()
            (cp / name / "SYSTEM_MANIFEST.md").write_text(
                MINI_MANIFEST.format(tahap=tahap), encoding="utf-8")
            index_insert_row(cp, f"| Sistem Uji {tahap.capitalize()} | `{name}/` | Sedang dibangun | 2026-09-05 | uji FI R5/R6 |")
            rc = run_tool(cp, "tools/validate_repo.py")
            checks.append((
                f"R5/R6 sistem '{name}' (Tahap: {tahap}) -> validator "
                f"{'PASS (warning saja)' if expect == 0 else 'FAIL'}",
                rc == expect))
            shutil.rmtree(cp / name)
            idx.write_text(idx_backup, encoding="utf-8")

        # R4 (F3): deleting a registered system's only unit STATUS must
        # fail both validator and FI (before: coverage silently shrank).
        target = None
        for sys_dir in sorted(cp.glob("sistem-*/")):
            if sys_dir.name == core.EXACT_PILOT:
                continue
            if sys_dir.name in core.parse_index(idx_backup)[0]:
                files = core.unit_status_files(sys_dir)
                if files:
                    target = files[0]
                    break
        if target is None:
            checks.append(("R4 (vacuous: tidak ada sistem terdaftar dgn unit STATUS)", True))
        else:
            data = target.read_text(encoding="utf-8")
            target.unlink()
            checks.append(("R4 unit STATUS terdaftar dihapus -> validator FAIL",
                           run_tool(cp, "tools/validate_repo.py") != 0))
            checks.append(("R4 unit STATUS terdaftar dihapus -> FI FAIL",
                           run_tool(cp, "tools/test_failure_injection.py") != 0))
            target.write_text(data, encoding="utf-8")

        # R7 (F5): template bootstrap must be self-contained — extract the
        # fresh template, run the validator there, and pin the exact
        # normalized warning set (4 labeled master-history references; zero
        # in the bootstrap doc or the user guide).
        checks.append(("R7 template build di salinan repo", run_tool(cp, "tools/build_template.py") == 0))
        z = cp / "_meta" / "_internal" / "template_clean.zip"
        if z.is_file():
            ex = Path(d) / "extract"
            ex.mkdir()
            with zipfile.ZipFile(z) as zf:
                zf.extractall(ex)
            git = shutil.which("git")
            if git:
                subprocess.run([git, "init", "-q"], cwd=ex, capture_output=True)
            out = subprocess.run(
                [sys.executable, str(ex / "tools" / "validate_repo.py")],
                capture_output=True, text=True,
                env={**os.environ, "FI_SKIP_NESTED": "1"},
            )
            got = set()
            for ln in out.stdout.splitlines():
                m = re.match(
                    r"WARNING reference: ([^:]+):\d+: unresolved path reference `([^`]+)`",
                    ln)
                if m:
                    got.add((m.group(1), m.group(2)))
            checks.append(("R7 validator di ekstrak template exit 0", out.returncode == 0))
            checks.append(("R7 warning ekstrak = persis daftar normalisasi (5 histori master)",
                           got == EXPECTED_TEMPLATE_WARNINGS))
            checks.append(("R7 bootstrap mandiri: tanpa warning di NEXT_SESSION_PROMPT/PANDUAN_PENGGUNA",
                           not any(doc in ("_meta/NEXT_SESSION_PROMPT.md", "PANDUAN_PENGGUNA.md")
                                   for doc, _ in got)))
        else:
            checks.append(("R7 zip template tersedia", False))

        # R1 (F1): a deleted CORE source must fail every tool that carries
        # the obligation list (validator, template, backup) — before, the
        # requirement set was derived from presence, so deletion passed.
        (cp / "_meta" / "DEFINITION_OF_DONE.md").unlink()
        checks.append(("R1 file inti dihapus (DEFINITION_OF_DONE.md) -> validator FAIL",
                       run_tool(cp, "tools/validate_repo.py") != 0))
        checks.append(("R1 file inti dihapus -> build_template FAIL",
                       run_tool(cp, "tools/build_template.py") != 0))
        checks.append(("R1 file inti dihapus -> backup_verify FAIL",
                       run_tool(cp, "tools/backup_verify.py") != 0))
    return checks


def pack_scenarios(base_dir: Path):
    """P1-P3 (7-8 Sep 2026): fail-closed paket repo mandiri (tools/pack_repo.py).

    Dijalankan di SALINAN repo. Klaim yang dipin di sini adalah klaim yang
    kalau diam-diam melemah membuat paket "LULUS" tanpa isi yang benar:
      P1 profil paket = daftar KEWAJIBAN, bukan daftar kelonggaran;
      P2 run yang gagal TIDAK meninggalkan folder paket setengah jadi;
      P3 daftar putih `absent_refs_allowed` tidak boleh membusuk (entri basi
         = error, bukan sisa yang dimaafkan) — diuji-mutasi: mematikan
         pemeriksaan anti pembusukan di validate_repo.py membuat P3 MERAH.
    """
    checks = []
    env = {**os.environ, "FI_SKIP_NESTED": "1", "PYTHONDONTWRITEBYTECODE": "1"}
    sistem = "sistem-konten-kreator"

    def sh(cwd: Path, *args):
        return subprocess.run([sys.executable, "-B", *args], cwd=str(cwd),
                              capture_output=True, text=True, env=env)

    cp = base_dir / "repo"
    shutil.copytree(
        ROOT, cp,
        ignore=shutil.ignore_patterns(
            ".git", "backups", "template_clean", "template_clean.zip",
            "__pycache__", "dist"),
    )

    # --- P1: hapus satu dokumen yang TERDAFTAR di meta_subset profil paket.
    # Kalau kewajiban diturunkan dari "apa yang kebetulan ada" (bug F1 versi
    # paket), penghapusan ini akan lolos diam-diam.
    out = base_dir / "pak1"
    ok = sh(cp, "tools/pack_repo.py", sistem, "--out", str(out)).returncode == 0
    checks.append(("P1 pra-syarat: pack sistem-konten-kreator berhasil", ok))
    if ok:
        prof = json.loads((out / "_meta" / "PAKET_REPO.json").read_text(encoding="utf-8"))
        rel = prof["meta_subset"][0]
        (out / rel).unlink()
        r = subprocess.run([sys.executable, "-B", "tools/validate_repo.py"],
                           cwd=str(out), capture_output=True, text=True, env=env)
        # Bukan cukup "gagal" — harus gagal DENGAN ALASAN kewajiban profil,
        # supaya check ini tidak lulus lewat error lain (mis. rujukan
        # menggantung) kalau daftar kewajiban diam-diam dilemahkan.
        checks.append(("P1 entri profil paket dihapus dari paket -> validator paket FAIL "
                       "dengan alasan 'missing required file'",
                       r.returncode != 0
                       and f"missing required file: {rel}" in r.stdout))
    else:
        checks.append(("P1 entri profil paket dihapus dari paket -> validator paket FAIL "
                       "dengan alasan 'missing required file'", False))

    # --- P2: rujukan menggantung yang TIDAK bisa dikategorikan = pemblokir.
    # `--check` harus non-zero, run sungguhan harus non-zero DAN tidak boleh
    # meninggalkan folder paket (paket setengah jadi = bukti palsu).
    (cp / sistem / "README.md").open("a", encoding="utf-8").write(
        "\nRujukan uji injeksi: `panduan/BERKAS_YANG_TIDAK_ADA.md`\n")
    rc_check = sh(cp, "tools/pack_repo.py", sistem, "--check").returncode
    out2 = base_dir / "pak2"
    rc_run = sh(cp, "tools/pack_repo.py", sistem, "--out", str(out2)).returncode
    checks.append(("P2 rujukan menggantung tak terkategori -> --check FAIL", rc_check != 0))
    checks.append(("P2 run gagal -> exit non-zero DAN folder paket tidak ditinggalkan",
                   rc_run != 0 and not out2.exists()))

    # --- P3: anti pembusukan daftar putih `absent_refs_allowed`. Entri yang
    # TIDAK lagi cocok dengan rujukan menggantung nyata wajib membuat
    # validator paket FAIL — kalau tidak, daftar putih membusuk jadi tempat
    # rujukan palsu berlindung dan angka bukti paket tidak lagi jujur.
    # Diuji-mutasi: menyalin validator paket, mematikan blok pemeriksaan anti
    # pembusukan, lalu membuktikan validator kini LOLOS — artinya kegagalan
    # tadi memang berasal dari pemeriksaan yang dipin di sini, bukan dari
    # error lain yang kebetulan ikut meledak.
    out3 = base_dir / "pak3"
    # Salinan repo SEGAR: `cp` sudah dimutasi P2 (README.md disuntik rujukan
    # menggantung) sehingga tidak bisa dipakai untuk injeksi daftar putih.
    cp3 = base_dir / "repo3"
    shutil.copytree(
        ROOT, cp3,
        ignore=shutil.ignore_patterns(
            ".git", "backups", "template_clean", "template_clean.zip",
            "__pycache__", "dist"),
    )
    ok3 = sh(cp3, "tools/pack_repo.py", sistem, "--out", str(out3)).returncode == 0
    checks.append(("P3 pra-syarat: pack bersih untuk injeksi daftar putih", ok3))
    if ok3:
        prof_path = out3 / "_meta" / "PAKET_REPO.json"
        prof = json.loads(prof_path.read_text(encoding="utf-8"))
        ghost = "panduan/BERKAS_HANTU_P3_TIDAK_DIRUJUK.md"
        prof.setdefault("absent_refs_allowed", []).append(
            {"ref": ghost, "kategori": "K0", "alasan": "injeksi uji P3 (ghost)"})
        prof_path.write_text(json.dumps(prof, indent=2, ensure_ascii=False) + "\n",
                             encoding="utf-8")
        r = subprocess.run([sys.executable, "-B", "tools/validate_repo.py"],
                           cwd=str(out3), capture_output=True, text=True, env=env)
        checks.append(("P3 entri daftar putih basi -> validator paket FAIL 'entri basi'",
                       r.returncode != 0 and "entri basi" in r.stdout))
        val_path = out3 / "tools" / "validate_repo.py"
        val = val_path.read_text(encoding="utf-8")
        marker = "for ref in sorted(set(ABSENT_ALLOWED) - ref_absent_hits):"
        if marker not in val:
            checks.append(("P3 diuji-mutasi: penanda blok anti pembusukan ditemukan", False))
        else:
            val_path.write_text(val.replace(
                marker, "for ref in ():  # MUTASI P3: anti pembusukan dimatikan"),
                encoding="utf-8")
            r2 = subprocess.run([sys.executable, "-B", "tools/validate_repo.py"],
                                cwd=str(out3), capture_output=True, text=True, env=env)
            val_path.write_text(val, encoding="utf-8")
            checks.append(("P3 diuji-mutasi: anti pembusukan dimatikan -> validator "
                           "paket LOLOS (tidak ada 'entri basi')",
                           r2.returncode == 0 and "entri basi" not in r2.stdout))
    else:
        checks.append(("P3 entri daftar putih basi -> validator paket FAIL 'entri basi'", False))
        checks.append(("P3 diuji-mutasi: anti pembusukan dimatikan -> validator "
                       "paket LOLOS (tidak ada 'entri basi')", False))
    return checks


def run():
    checks = []
    with TemporaryDirectory() as d:
        base = Path(d)

        # FI-01: output without status must fail closed.
        unit = base / "fi01"
        unit.mkdir()
        (unit / "OUTPUT.md").write_text("output", encoding="utf-8")
        checks.append(("FI-01 missing STATUS", not core.state_is_safe(unit)))

        # FI-02: released status without output must fail closed.
        unit = base / "fi02"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- **Status:** `released`\n- **Pekerjaan belum tersimpan:** Tidak ada\n",
            encoding="utf-8",
        )
        checks.append(("FI-02 missing output", not core.state_is_safe(unit)))

        # FI-07: a blocked state must never be treated as released.
        unit = base / "fi07"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- **Status:** `blocked`\n- **Pekerjaan belum tersimpan:** Tidak ada\n",
            encoding="utf-8",
        )
        checks.append(("FI-07 blocked state", core.state_is_safe(unit)))

        # Healthy state in the REAL repo format (bold field, no backticks).
        unit = base / "healthy"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- **Status:** `released`\n- **Pekerjaan belum tersimpan:** Tidak ada\n",
            encoding="utf-8",
        )
        (unit / "OUTPUT.md").write_text("checked output", encoding="utf-8")
        checks.append(("healthy released state (real bold format)", core.state_is_safe(unit)))

        # Real-world variant with backticks (konten-kreator template style).
        unit = base / "healthy_backticked"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- **Status:** `in-progress`\n- **Pekerjaan belum tersimpan:** `Tidak ada`\n",
            encoding="utf-8",
        )
        checks.append(("backticked value accepted", core.state_is_safe(unit)))

        # Field absent must fail closed — this was the deck-presentasi case
        # (T6_STATUS.md had no field at all; M-03).
        unit = base / "field_absent"
        unit.mkdir()
        (unit / "STATUS.md").write_text("- **Status:** `in-progress`\n", encoding="utf-8")
        checks.append(("missing field fails closed", not core.state_is_safe(unit)))

        # Free-text "none" variations are NOT safe (C-01 exactness).
        unit = base / "unsafe_value"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- **Status:** `in-progress`\n- **Pekerjaan belum tersimpan:** aman kok\n",
            encoding="utf-8",
        )
        checks.append(("unsafe value fails closed", not core.state_is_safe(unit)))

        # --- Review PR #11 (F4): fake-safety-evidence scenarios -----------
        # A dirty SECOND field after a safe first one is ambiguity, not safety.
        unit = base / "dup_field"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- **Status:** `in-progress`\n"
            "- **Pekerjaan belum tersimpan:** Tidak ada\n"
            "- **Pekerjaan belum tersimpan:** naskah-draft.md belum di-commit\n",
            encoding="utf-8",
        )
        checks.append(("dup field (aman lalu kotor) -> tidak aman", not core.state_is_safe(unit)))

        # Official protocol format `- Status: approved` (no bold/backticks).
        unit = base / "proto_approved_no_output"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- Status: approved\n- Pekerjaan belum tersimpan: Tidak ada\n",
            encoding="utf-8",
        )
        checks.append(("protokol '- Status: approved' tanpa OUTPUT -> tidak aman",
                       not core.state_is_safe(unit)))

        unit = base / "proto_approved_with_output"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- Status: approved\n- Pekerjaan belum tersimpan: Tidak ada\n",
            encoding="utf-8",
        )
        (unit / "OUTPUT.md").write_text("checked", encoding="utf-8")
        checks.append(("protokol '- Status: approved' dgn OUTPUT -> aman",
                       core.state_is_safe(unit)))

        # Examples inside code fences are ignored (state is not taken from
        # a pasted example).
        unit = base / "fenced_example"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "Contoh salah format:\n"
            "```\n- **Pekerjaan belum tersimpan:** aman kok\n```\n"
            "- **Status:** `in-progress`\n"
            "- **Pekerjaan belum tersimpan:** Tidak ada\n",
            encoding="utf-8",
        )
        checks.append(("contoh dalam fence diabaikan -> aman", core.state_is_safe(unit)))

        # Blockquote examples (line not starting with the field) ignored.
        unit = base / "quoted_example"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "> **Pekerjaan belum tersimpan:** Tidak ada — contoh kutipan, bukan state\n"
            "- **Status:** `in-progress`\n"
            "- **Pekerjaan belum tersimpan:** Tidak ada\n",
            encoding="utf-8",
        )
        checks.append(("kutipan blok (>) tidak dihitung -> aman", core.state_is_safe(unit)))

    n_synth = len(checks)

    # Regression against REAL repo data (F3): every registered system must
    # have at least one unit STATUS, and every unit STATUS that claims to
    # be safe must actually satisfy the shared checker.
    index_text = (ROOT / "_meta" / "INDEKS_SISTEM.md").read_text(encoding="utf-8")
    registered = set(core.parse_index(index_text)[0])
    real = []
    for sys_dir in sorted(ROOT.glob("sistem-*/")):
        files = core.unit_status_files(sys_dir)
        if sys_dir.name in registered and not files:
            checks.append((f"registered system {sys_dir.name} punya unit STATUS (F3)", False))
            continue
        for status_path in files:
            real.append((status_path, core.state_is_safe(status_path.parent)))
    for status_path, safe in real:
        checks.append((f"real unit consistent: {status_path.relative_to(ROOT)}", safe))

    # R1–R7 regression scenarios (skipped when nested — FI_SKIP_NESTED).
    reg = []
    if not os.environ.get("FI_SKIP_NESTED"):
        with TemporaryDirectory() as d:
            reg = regression_scenarios(Path(d))
    checks += reg

    # P1–P2 paket repo mandiri (skipped when nested, same reason).
    pak = []
    if not os.environ.get("FI_SKIP_NESTED"):
        with TemporaryDirectory() as d:
            pak = pack_scenarios(Path(d))
    checks += pak

    failed = [name for name, ok in checks if not ok]
    if failed:
        print("FAILURE-INJECTION TESTS FAILED")
        for name in failed:
            print(f"- {name}")
        raise SystemExit(1)
    print(f"FAILURE-INJECTION TESTS PASSED: {len(checks)} scenarios "
          f"({n_synth} sintetis + {len(real)} unit nyata + {len(reg)} regresi review PR-11"
          f" + {len(pak)} paket repo mandiri)")


if __name__ == "__main__":
    run()
