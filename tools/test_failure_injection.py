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
  scenarios R1–R8 that reproduce the review's mutations: deleted core
  source, unregistered system folder, non-backticked INDEKS row, deleted
  unit STATUS, kerangka/siap-pakai lifecycle, and the template bootstrap
  self-containment assertion, plus the PR A self-contained folder gate.

Run with FI_SKIP_NESTED=1 to skip repo-copy regressions (used when this file is
invoked inside a copied repo by the R scenarios themselves — prevents recursion).
"""
from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib
import importlib.util
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
     "sistem/sistem-konten-kreator/_sistem/09_AUDIT_MIGRASI_GITHUB_AGENT.md"),
    ("_meta/00_CARA_KERJA_META.md",
     "sistem/sistem-konten-kreator/_sistem/00_CARA_PAKAI_SISTEM.md"),
    ("_meta/SYSTEM_MANIFEST.md",
     "sistem/sistem-pilot-catatan-belajar/unit-aktif/pilot-002-behavioral/OUTPUT.md"),
    ("_meta/SYSTEM_MANIFEST.md",
     "_sistem/11_LOG_SESI.md"),
    ("_meta/SYSTEM_MANIFEST.md",
     "sistem/sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md"),
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
| W-10 audit isi + pengiriman hasil | direncanakan | | |
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
    """R1–R8: the review's mutations, pinned as permanent regressions."""
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

        # R4 (F3): a registered system left with ZERO unit STATUS must fail
        # both validator and FI (before: coverage silently shrank). A system
        # may legitimately hold several units (produksi selesai yang
        # dipertahankan + produksi berjalan), jadi skenarionya menghapus
        # SELURUH unit STATUS sistem target, bukan hanya yang pertama.
        # Sistem Tahap: kerangka DILEWATI (11 Sep 2026, temuan PR sistem-klinik):
        # untuk mereka kehadiran unit sengaja berperingkat warning (aturan Tahap
        # di 03_KONTRAK_WARISAN), jadi menghapus unitnya tidak boleh dan tidak
        # akan membuat validator FAIL — menguji fail-closed di sistem yang
        # check-nya memang longgar = hasil positif-palsu terbalik (R4 merah
        # padahal sistemnya benar). Fail-closed diuji pada sistem siap-pakai.
        target_files = []
        for sys_dir in sorted(list(cp.glob("sistem/sistem-*/")) + list(cp.glob("sistem-*/"))):
            sys_rel = sys_dir.relative_to(cp).as_posix()
            if sys_rel == core.EXACT_PILOT or sys_dir.name == core.EXACT_PILOT:
                continue
            if sys_rel in core.parse_index(idx_backup)[0] or sys_dir.name in core.parse_index(idx_backup)[0]:
                manifest = sys_dir / "SYSTEM_MANIFEST.md"
                if manifest.is_file() and core.manifest_tahap(
                        manifest.read_text(encoding="utf-8")) == "kerangka":
                    continue
                files = core.unit_status_files(sys_dir)
                if files:
                    target_files = files
                    break
        if not target_files:
            checks.append(("R4 (vacuous: tidak ada sistem terdaftar dgn unit STATUS)", True))
        else:
            data = [(t, t.read_text(encoding="utf-8")) for t in target_files]
            for t, _ in data:
                t.unlink()
            checks.append(("R4 unit STATUS terdaftar dihapus -> validator FAIL",
                           run_tool(cp, "tools/validate_repo.py") != 0))
            checks.append(("R4 unit STATUS terdaftar dihapus -> FI FAIL",
                           run_tool(cp, "tools/test_failure_injection.py") != 0))
            for t, isi in data:
                t.write_text(isi, encoding="utf-8")

        # R7 (F5): template bootstrap must be self-contained — extract the
        # fresh template, run the validator there, and pin the exact
        # normalized warning set (5 labeled master-history references; zero
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

        # R8 (PR A): alat gerbang mandiri baru adalah CORE tool. Menghapusnya
        # dari master harus gagal keras, bukan lenyap dari glob turunan.
        core_tool = cp / "tools" / "check_selfcontained.py"
        core_tool_data = core_tool.read_bytes()
        core_tool.unlink()
        checks.append(("R8 CORE tool check_selfcontained.py dihapus -> validator FAIL",
                       run_tool(cp, "tools/validate_repo.py") != 0))
        core_tool.write_bytes(core_tool_data)

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



def klaim_total(baris: str) -> int:
    """Hitung KLAIM TOTAL pada baris '**Jumlah:**' dokumen inventaris FI (pengetatan D-2b).

    Definisi "klaim total" sengaja SEMPIT dan dinyatakan di sini, bukan "ambil semua angka":
      (a) angka yang langsung diikuti `skenario di master`  -> total kanonik;
      (b) frasa `Jumlah ... kini **N**`                     -> total kedua gaya lama;
      (c) kutipan cetakan `PASSED: N scenarios`             -> total kedua yang disalin mentah.
    Frasa riwayat seperti "3 skenario sintetis" atau "RP8 (10 pemeriksaan)" BUKAN klaim total
    dan sengaja tidak dihitung — kalau dihitung, riwayat tidak bisa ditulis sama sekali.

    Sebab pengetatan ini (temuan review independen putaran 2 PR #74, dan ditemukan JUGA di
    `main`): satu baris yang sama memuat 97 di depan dan 73/75 beserta komposisi lamanya di
    ekor, sementara penjaga versi lama hanya membaca kemunculan pertama — jadi dokumen yang
    membantah dirinya sendiri lolos alat. Itu pola D-2 (dua angka, dua tempat, tanpa penjaga)
    di dalam SATU tempat.
    """
    return (len(re.findall(r"\d+\s+skenario di master", baris))
            + len(re.findall(r"Jumlah[^.]{0,60}?kini\s*\*\*\d+\*\*", baris))
            + len(re.findall(r"PASSED:\s*\d+\s+scenarios", baris)))


def _load_review_prompt(repo: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, repo / "tools" / "review_prompt.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("review_prompt.py tidak bisa di-load")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def review_prompt_scenarios(base_dir: Path):
    """RP1-RP5: regresi pembangkit prompt review.

    Ini uji mutasi untuk empat cacat nyata: deteksi pin via self-match string,
    urutan baca yang menjatuhkan Markdown root, jendela-uji yang dipicu
    log penulis PR sendiri, dan daftar berkas PR yang terpotong 100 berkas
    karena `gh pr view --json files` tidak dipaginasi (RP5 — T-2, temuan
    review PR #55).

    RP5 diubah 15 Sep 2026 setelah temuan T-4 review PR #56: versi pertama
    hanya memeriksa keberadaan teks `--paginate` di sumber (tautologi, bukan
    perilaku). Kini yang diuji: (RP5b) argv yang dikembalikan `files_command`,
    (RP5c) bahwa `fetch_pr_files` benar-benar memanggilnya — menutup celah
    "argv karangan di tempat pemanggilan" yang disebut C-2 — dan (RP5a)
    penjaga konsistensi `resolve_pr_files` yang menolak daftar tak konsisten.
    Semuanya diuji-mutasi, dan mutasi yang tidak mengubah apa pun membuat uji
    gagal (bukan lolos palsu).
    """
    checks = []
    cp = base_dir / "repo"
    shutil.copytree(
        ROOT, cp,
        ignore=shutil.ignore_patterns(
            ".git", "backups", "template_clean", "template_clean.zip",
            "__pycache__", "dist"),
    )
    rp = _load_review_prompt(cp, "review_prompt_regression")

    fake_pr = {
        "number": 999,
        "baseRefOid": "1" * 40,
        "headRefOid": "2" * 40,
        "title": "uji mutasi review_prompt",
        "baseRefName": "main",
        "headRefName": "arena/uji",
        "isDraft": False,
    }

    guarded = rp.guarded_inventory(["tools/review_prompt.py"])
    checks.append((
        "RP1 tools/review_prompt.py pelindung eksplisit beralasan pembangkit prompt pengadil",
        any(row == ("tools/review_prompt.py", True, "pembangkit prompt pengadil") for row in guarded),
    ))
    prompt, _ = rp.render(fake_pr, ["tools/review_prompt.py"], generic=False)
    checks.append((
        "RP1 PR menyentuh review_prompt.py -> prompt berbunyi JANGAN merge",
        "**BERLAKU untuk PR ini.**" in prompt and "**JANGAN melakukan merge apa pun**" in prompt,
    ))
    checks.append((
        "RP1 validate_repo.py tidak dianggap memuat pin hanya karena menyebut nama konstanta",
        "tools/validate_repo.py" not in set(rp.pin_bearing_tools()),
    ))

    # Mutasi RP1: hapus pendaftaran eksplisit review_prompt. Tanpa baris ini,
    # self-match string tidak boleh diam-diam menjadi alasan pelindung palsu.
    rp_path = cp / "tools" / "review_prompt.py"
    original = rp_path.read_text(encoding="utf-8")
    mutated = original.replace(
        '    "tools/review_prompt.py": "pembangkit prompt pengadil",\n',
        '',
    )
    rp_path.write_text(mutated, encoding="utf-8")
    rp_mut = _load_review_prompt(cp, "review_prompt_mut_rp1")
    guarded_mut = rp_mut.guarded_inventory(["tools/review_prompt.py"])
    checks.append((
        "RP1 diuji-mutasi: hapus pendaftaran eksplisit -> alasan pembangkit hilang",
        not any(row == ("tools/review_prompt.py", True, "pembangkit prompt pengadil") for row in guarded_mut),
    ))
    rp_path.write_text(original, encoding="utf-8")
    rp = _load_review_prompt(cp, "review_prompt_regression_fresh")

    files = [
        "_meta/00_CARA_KERJA_META.md",
        "PANDUAN_PENGGUNA.md",
        "PROMPT_ENTRI_UNIVERSAL.md",
        "tools/review_prompt.py",
    ]
    order = rp.reading_order(files)
    joined = "\n".join(order)
    checks.append((
        "RP2 urutan baca memuat Markdown root tersentuh dan tidak menggandakan 00_CARA_KERJA_META",
        "`PANDUAN_PENGGUNA.md`" in joined
        and "`PROMPT_ENTRI_UNIVERSAL.md`" in joined
        and joined.count("`_meta/00_CARA_KERJA_META.md`") == 1,
    ))

    # Mutasi RP2: kembalikan filter lama yang hanya menerima .md ber-slash.
    mutated = original.replace('elif rel.endswith(".md"):', 'elif rel.endswith(".md") and "/" in rel:')
    rp_path.write_text(mutated, encoding="utf-8")
    rp_mut = _load_review_prompt(cp, "review_prompt_mut_rp2")
    order_mut = "\n".join(rp_mut.reading_order(files))
    checks.append((
        "RP2 diuji-mutasi: filter lama menjatuhkan Markdown root",
        "`PANDUAN_PENGGUNA.md`" not in order_mut
        and "`PROMPT_ENTRI_UNIVERSAL.md`" not in order_mut,
    ))
    rp_path.write_text(original, encoding="utf-8")
    rp = _load_review_prompt(cp, "review_prompt_regression_window")

    log_root = base_dir / "logs"
    log_root.mkdir()
    (log_root / "LOG_SESI_OWN.md").write_text(
        "# own\n\n- **Keadaan:** `OPEN`\n\ncatatan: jendela uji terbuka untuk PR ini\n",
        encoding="utf-8",
    )
    rp.ROOT = log_root
    blocking, writer = rp.open_test_window(["LOG_SESI_OWN.md"])
    checks.append((
        "RP3 log penulis PR sendiri tidak memicu penyembunyian tetapi pointer tetap ada",
        blocking == [] and writer == ["LOG_SESI_OWN.md:5"],
    ))
    (log_root / "LOG_SESI_OTHER.md").write_text(
        "# other\n\n- **Keadaan:** `OPEN`\n\ncatatan: jendela uji terbuka dari sesi lain\n",
        encoding="utf-8",
    )
    blocking2, writer2 = rp.open_test_window(["LOG_SESI_OWN.md"])
    checks.append((
        "RP3 OPEN log sesi lain menyebut jendela -> penyembunyian tetap berlaku",
        "LOG_SESI_OTHER.md:5" in blocking2 and "LOG_SESI_OWN.md:5" in writer2,
    ))

    # Mutasi RP3: matikan pengecualian log penulis; log sendiri kembali menjadi
    # blocking. Ini membuktikan baris pengecualian benar-benar dijaga uji.
    mutated = original.replace('if rel in writer_logs:', 'if False and rel in writer_logs:')
    rp_path.write_text(mutated, encoding="utf-8")
    rp_mut = _load_review_prompt(cp, "review_prompt_mut_rp3")
    rp_mut.ROOT = log_root
    blocking_mut, writer_mut = rp_mut.open_test_window(["LOG_SESI_OWN.md"])
    checks.append((
        "RP3 diuji-mutasi: pengecualian log penulis dimatikan -> log sendiri blocking",
        "LOG_SESI_OWN.md:5" in blocking_mut and "LOG_SESI_OWN.md:5" not in writer_mut,
    ))
    rp_path.write_text(original, encoding="utf-8")

    closed_root = base_dir / "logs_closed_late"
    closed_root.mkdir()
    (closed_root / "LOG_SESI_CLOSED_LATE.md").write_text(
        "# late closed\n\n"
        "- **Status:** OPEN\n\n"
        "catatan: jendela uji terbuka di header lama\n\n"
        "- **Status sesi: CLOSED — penutupan append-only di akhir berkas.**\n",
        encoding="utf-8",
    )
    rp.ROOT = closed_root
    blocking_closed, writer_closed = rp.open_test_window([])
    checks.append((
        "RP4 status akhir CLOSED mengalahkan header OPEN pada pemindai jendela-uji",
        blocking_closed == [] and writer_closed == [],
    ))
    rp_path.write_text(original, encoding="utf-8")
    rp = _load_review_prompt(cp, "review_prompt_regression_files")

    # RP5 (T-2): `gh pr view --json files` berhenti di 100 berkas, sehingga PR
    # besar bisa terlihat "tidak menyentuh berkas pelindung". Dua hal diuji
    # sebagai PERILAKU (bukan keberadaan teks di sumber): argv yang benar-benar
    # dipakai, dan penjaga konsistensi yang menolak daftar tak konsisten.
    argv = rp.files_command(42)
    checks.append((
        "RP5b argv daftar berkas memuat --paginate + path pulls/<n>/files",
        "--paginate" in argv and "repos/{owner}/{repo}/pulls/42/files" in argv,
    ))

    mut_pag = original.replace('        "--paginate",\n', '')
    assert mut_pag != original, "mutasi RP5b tidak mengubah apa pun — uji tidak valid"
    rp_path.write_text(mut_pag, encoding="utf-8")
    rp_mut = _load_review_prompt(cp, "review_prompt_mut_rp5b")
    checks.append((
        "RP5b diuji-mutasi: --paginate dihapus -> argv kehilangan paginasi",
        "--paginate" not in rp_mut.files_command(42),
    ))
    rp_path.write_text(original, encoding="utf-8")
    rp = _load_review_prompt(cp, "review_prompt_regression_guard")

    fakta = {"files": [{"path": "satu.md"}, {"path": "dua.md"}]}
    rp.fetch_pr_files = lambda number: ["satu.md"]
    try:
        rp.resolve_pr_files(7, fakta)
        menolak = False
    except rp.ToolError:
        menolak = True
    checks.append((
        "RP5a penjaga konsistensi menolak daftar berkas tak konsisten (fail-closed)",
        menolak,
    ))

    rp.fetch_pr_files = lambda number: ["satu.md", "dua.md"]
    checks.append((
        "RP5a daftar konsisten diteruskan (penjaga tidak menolak sembarangan)",
        rp.resolve_pr_files(7, fakta) == ["satu.md", "dua.md"],
    ))

    mut_guard = original.replace(
        "if len(viewed) < PR_FILES_VIEW_CAP and len(viewed) != len(files):",
        "if False and len(viewed) != len(files):",
    )
    assert mut_guard != original, "mutasi RP5a tidak mengubah apa pun — uji tidak valid"
    rp_path.write_text(mut_guard, encoding="utf-8")
    rp_mut = _load_review_prompt(cp, "review_prompt_mut_rp5a")
    rp_mut.fetch_pr_files = lambda number: ["satu.md"]
    try:
        rp_mut.resolve_pr_files(7, fakta)
        menolak_mut = False
    except rp_mut.ToolError:
        menolak_mut = True
    checks.append((
        "RP5a diuji-mutasi: penjaga dimatikan -> daftar tak konsisten lolos",
        not menolak_mut,
    ))
    rp_path.write_text(original, encoding="utf-8")
    rp = _load_review_prompt(cp, "review_prompt_regression_link")

    # RP5c (C-2 review PR #56): rantai pemanggilannya ikut diuji — bukan
    # hanya nilai argv helper-nya. Kalau fetch_pr_files menyusun argv sendiri
    # (tanpa paginasi), uji ini merah walaupun files_command benar.
    tangkap = {}

    def _run_palsu(cmd):
        tangkap["cmd"] = list(cmd)
        return 0, "satu.md\n", ""

    rp._run = _run_palsu
    hasil = rp.fetch_pr_files(42)
    checks.append((
        "RP5c fetch_pr_files benar-benar memakai argv files_command (bukan argv karangan)",
        tangkap.get("cmd") == rp.files_command(42) and hasil == ["satu.md"],
    ))

    mut_link = original.replace(
        "    code, out, err = _run(files_command(number))",
        '    code, out, err = _run(["gh", "api",'
        ' f"repos/{{owner}}/{{repo}}/pulls/{number}/files", "--jq", ".[].filename"])',
    )
    assert mut_link != original, "mutasi RP5c tidak mengubah apa pun — uji tidak valid"
    rp_path.write_text(mut_link, encoding="utf-8")
    rp_mut = _load_review_prompt(cp, "review_prompt_mut_rp5c")
    tangkap_mut = {}
    rp_mut._run = lambda cmd: (tangkap_mut.update(cmd=list(cmd)) or (0, "satu.md\n", ""))
    rp_mut.fetch_pr_files(42)
    checks.append((
        "RP5c diuji-mutasi: argv in-line tanpa paginasi -> tidak lagi sama dengan files_command",
        tangkap_mut.get("cmd") != rp_mut.files_command(42),
    ))
    rp_path.write_text(original, encoding="utf-8")
    rp = _load_review_prompt(cp, "review_prompt_regression_nested")

    # RP6 (C-1, temuan review PR #56): pemindaian log sesi harus mencakup
    # `_log-sesi/` — sebelum diperbaiki, pemindai hanya mengglob root sehingga
    # buta total sejak log pindah folder (v1.13.0).
    nested = base_dir / "logs_nested"
    (nested / "_log-sesi").mkdir(parents=True)
    (nested / "_log-sesi" / "LOG_SESI_NESTED.md").write_text(
        "# nested\n\n- **Keadaan:** `OPEN`\n\ncatatan: jendela uji terbuka untuk PR ini\n",
        encoding="utf-8",
    )
    rp.ROOT = nested
    blocking_n, _ = rp.open_test_window([])
    checks.append((
        "RP6 log sesi di _log-sesi/ ikut terdeteksi (bukan hanya root)",
        blocking_n == ["_log-sesi/LOG_SESI_NESTED.md:5"],
    ))
    blocking_w, writer_w = rp.open_test_window(["_log-sesi/LOG_SESI_NESTED.md"])
    checks.append((
        "RP6 log penulis di _log-sesi/ dikecualikan dari penyembunyian (tetap dipointer)",
        blocking_w == [] and writer_w == ["_log-sesi/LOG_SESI_NESTED.md:5"],
    ))

    mut_dir = original.replace(
        'LOG_SESI_DIRS = ("", "_log-sesi")', 'LOG_SESI_DIRS = ("",)')
    assert mut_dir != original, "mutasi RP6 tidak mengubah apa pun — uji tidak valid"
    rp_path.write_text(mut_dir, encoding="utf-8")
    rp_mut = _load_review_prompt(cp, "review_prompt_mut_rp6")
    rp_mut.ROOT = nested
    blocking_mut, _ = rp_mut.open_test_window([])
    checks.append((
        "RP6 diuji-mutasi: _log-sesi/ dihapus dari LOG_SESI_DIRS -> log di sana tak terdeteksi",
        blocking_mut == [],
    ))
    rp_path.write_text(original, encoding="utf-8")

    # ------------------------------------------------------------------
    # RP7 - regresi temuan R3 review independen PR #74: pembangkit prompt
    # menyajikan `git diff <base tip> <head>` sebagai perintah wajib sementara
    # daftar berkasnya berasal dari diff PR terhadap MERGE-BASE. Keduanya berbeda
    # (terukur 53 vs 49 oleh reviewer; 59 vs 55 sesudahnya) sehingga reviewer
    # mencurigai penghapusan bukti yang tidak pernah terjadi.
    # ------------------------------------------------------------------
    rp = _load_review_prompt(cp, "review_prompt_rp7")
    MB, BT, HD = "b" * 40, "a" * 40, "c" * 40
    pr7 = dict(fake_pr, baseRefOid=BT, headRefOid=HD)

    # RP7a - tanpa objek diff: merge-base TIDAK TERHITUNG, dinyatakan, tidak ditebak.
    prompt_a, _ = rp.render(pr7, ["tools/review_prompt.py"], generic=False)
    checks.append((
        "RP7a tanpa pengukuran -> merge-base dinyatakan TIDAK TERHITUNG (fail-closed, bukan ditebak)",
        "TIDAK TERHITUNG" in prompt_a and "OBJEK YANG HENDAK DIPUTUSKAN" in prompt_a,
    ))

    # RP7b - dengan objek terukur: KETIGA sha muncul, dua diff berlabel dengan perintah
    # yang benar, dan selisihnya dinyatakan sebagai angka.
    objek = {
        "merge_base": MB,
        "nama_merge_base": ["_meta/A.md", "_meta/B.md"],
        "nama_langsung": ["_meta/A.md", "_meta/B.md", "_log-sesi/L.md", "sistem/x/C.md"],
        "kesalahan": [],
    }
    prompt_b, _ = rp.render(pr7, ["_meta/A.md", "_meta/B.md"], generic=False, objek=objek)
    checks.append((
        "RP7b diff (A) memakai MERGE-BASE, bukan base tip",
        f"git diff --stat {MB} {HD}" in prompt_b,
    ))
    checks.append((
        "RP7b diff (B) memakai base tip dan diberi label sebagai selisih langsung",
        f"git diff --stat {BT} {HD}" in prompt_b and "SELISIH LANGSUNG" in prompt_b,
    ))
    checks.append((
        "RP7b selisih terukur dinyatakan: 2 berkas hanya di (B) = bukan perubahan PR",
        "hanya di (B), jadi BUKAN perubahan PR ini: 2 berkas" in prompt_b
        and "`_log-sesi/L.md`" in prompt_b and "`sistem/x/C.md`" in prompt_b,
    ))
    checks.append((
        "RP7b ketiga sha ter-pin di tabel objek (base tip, merge-base, head)",
        all(x in prompt_b for x in (BT, MB, HD)),
    ))

    # RP7c - konsistensi daftar API vs diff lokal: SAMA dan BERBEDA dua-duanya diuji.
    prompt_sama, _ = rp.render(pr7, ["_meta/A.md", "_meta/B.md"], generic=False,
                               objek=dict(objek, nama_merge_base=["_meta/A.md", "_meta/B.md"]))
    prompt_beda, _ = rp.render(pr7, ["_meta/A.md", "_meta/Z.md"], generic=False, objek=objek)
    checks.append((
        "RP7c konsistensi daftar dinyatakan SAMA bila API = diff lokal",
        "**SAMA**" in prompt_sama,
    ))
    checks.append((
        "RP7c konsistensi daftar dinyatakan BERBEDA bila API != diff lokal (tidak dipilih diam-diam)",
        "**BERBEDA**" in prompt_beda and "wajib dinyatakan di verdict" in prompt_beda,
    ))

    # RP7d - kesalahan pengukuran disampaikan ke prompt, tidak ditelan.
    prompt_err, _ = rp.render(pr7, ["_meta/A.md"], generic=False,
                              objek={"merge_base": None, "nama_merge_base": None,
                                     "nama_langsung": None,
                                     "kesalahan": ["merge-base tidak bisa dihitung (git keluar 128)"]})
    checks.append((
        "RP7d kegagalan pengukuran dinyatakan di prompt (fail-closed)",
        "Yang TIDAK bisa diukur, dinyatakan" in prompt_err
        and "merge-base tidak bisa dihitung" in prompt_err
        and f"git diff --stat {MB} {HD}" not in prompt_err,
    ))

    # Mutasi RP7 - kembalikan perilaku lama: diff (A) memakai base tip. Kedua diff jadi
    # identik dan selisihnya hilang; RP7b harus GAGAL. Kalau mutasi ini tidak mengubah
    # apa pun, berarti uji di atas tautologi.
    mut_a = original.replace(
        'a(f"git diff --stat {mb} {head}")', 'a(f"git diff --stat {base} {head}")')
    assert mut_a != original, "mutasi RP7a tidak mengubah apa pun - uji tidak valid"
    rp_path.write_text(mut_a, encoding="utf-8")
    rp_mut = _load_review_prompt(cp, "review_prompt_mut_rp7")
    prompt_mut, _ = rp_mut.render(pr7, ["_meta/A.md", "_meta/B.md"], generic=False, objek=objek)
    checks.append((
        "RP7 diuji-mutasi: diff (A) dikembalikan ke base tip -> perintah merge-base hilang",
        f"git diff --stat {MB} {HD}" not in prompt_mut,
    ))
    rp_path.write_text(original, encoding="utf-8")

    # Mutasi RP7 kedua - buang penanda fail-closed: tanpa objek, prompt tidak boleh
    # lagi menyatakan TIDAK TERHITUNG, dan RP7a harus gagal.
    mut_b = original.replace('mb = objek.get("merge_base") or "TIDAK TERHITUNG"',
                             'mb = objek.get("merge_base") or ""')
    assert mut_b != original, "mutasi RP7b tidak mengubah apa pun - uji tidak valid"
    rp_path.write_text(mut_b, encoding="utf-8")
    rp_mut2 = _load_review_prompt(cp, "review_prompt_mut_rp7b")
    prompt_mut2, _ = rp_mut2.render(pr7, ["tools/review_prompt.py"], generic=False)
    checks.append((
        "RP7 diuji-mutasi: penanda TIDAK TERHITUNG dibuang -> prompt diam tanpa merge-base",
        "TIDAK TERHITUNG" not in prompt_mut2,
    ))
    rp_path.write_text(original, encoding="utf-8")

    # ------------------------------------------------------------------
    # RP8 - dua cacat prompt yang ditemukan dengan MEMBACA KELUARAN ALATNYA SENDIRI:
    #   (1) bagian 6 mencetak perintah `gh pr merge <N> --merge` untuk PR yang bagian 7-nya
    #       sendiri MELARANG merge (PR menyentuh alat pengadil) - kontradiksi di satu dokumen,
    #       dan yang muncul lebih dulu adalah perintah merge;
    #   (2) prompt tidak pernah menetapkan format komentar verdict, padahal ambil_verdict.py
    #       memutuskan dari BARIS BERPARKAH PERTAMA dengan kosakata ketat. Akibatnya nyata:
    #       2 dari 3 verdict PR #74 tidak pernah terhitung dan kuorum terbaca 1/3.
    # Pemeriksaannya LINTAS ALAT: contoh judul yang diwajibkan prompt dimasukkan ke pengumpul
    # verdict dan harus benar-benar terbaca - bukan hanya terlihat benar di mata.
    # ------------------------------------------------------------------
    _av_spec = importlib.util.spec_from_file_location(
        "ambil_verdict_rp8", ROOT / "tools" / "ambil_verdict.py")
    assert _av_spec is not None and _av_spec.loader is not None
    av = importlib.util.module_from_spec(_av_spec)
    _av_spec.loader.exec_module(av)

    NUM = pr7["number"]
    perintah_merge = f"gh pr merge {NUM} --merge"
    prompt_arb, _ = rp.render(pr7, ["tools/review_prompt.py"], generic=False, objek=objek)
    prompt_biasa, _ = rp.render(pr7, ["sistem/sistem-undangan/STATUS.md"], generic=False, objek=objek)

    checks.append((
        "RP8 PR menyentuh alat pengadil -> perintah merge HILANG dan diganti larangan (bukan kontradiksi)",
        perintah_merge not in prompt_arb and "DILARANG" in prompt_arb,
    ))
    checks.append((
        "RP8 PR biasa -> aturan merge normal TETAP ada (supresinya bersyarat, bukan dihapus menyeluruh)",
        perintah_merge in prompt_biasa,
    ))

    judul = [b for b in prompt_arb.splitlines() if b.startswith("## Review independen PR")]
    checks.append((
        "RP8 prompt menetapkan TEPAT SATU contoh judul verdict yang bisa disalin hakim",
        len(judul) == 1,
    ))
    badan = judul[0] + "\n\n- **temuan**: contoh\n"
    checks.append((
        "RP8 LINTAS ALAT: contoh judul itu terhitung sebagai SLOT HAKIM oleh ambil_verdict",
        av.slot_hakim(badan) is True,
    ))
    checks.append((
        "RP8 LINTAS ALAT: contoh judul itu menghasilkan verdict MERAH (bukan TIDAK DITEMUKAN)",
        av.simpulkan(badan) == "MERAH",
    ))
    checks.append((
        "RP8 LINTAS ALAT: varian HIJAU dari contoh itu terbaca HIJAU",
        av.simpulkan(badan.replace("MERAH", "HIJAU")) == "HIJAU",
    ))
    checks.append((
        "RP8 syarat 'jangan sebut penulis di baris pertama' itu NYATA: judul yang memuatnya dibuang",
        av.slot_hakim("## Review independen PR — tanggapan penulis — VERDICT: MERAH\n") is False,
    ))
    checks.append((
        "RP8 syarat 'jangan di dalam pagar kode' itu NYATA: verdict terpagar tidak terbaca",
        av.simpulkan("```md\n" + badan + "```\n").startswith("TIDAK DITEMUKAN")
        and av.slot_hakim("```md\n" + badan + "```\n") is False,
    ))

    # Mutasi RP8-1: buang supresi bersyaratnya -> perintah merge harus MUNCUL lagi untuk PR
    # yang menyentuh alat pengadil. Kalau tidak muncul, pemeriksaan pertama di atas tautologi.
    mut1 = original.replace('    if arbiter:\n        a("**PERHATIAN — PR INI MENYENTUH ALAT PENGADIL',
                            '    if False:\n        a("**PERHATIAN — PR INI MENYENTUH ALAT PENGADIL')
    assert mut1 != original, "mutasi RP8-1 tidak mengubah apa pun - uji tidak valid"
    rp_path.write_text(mut1, encoding="utf-8")
    rp_m1 = _load_review_prompt(cp, "review_prompt_mut_rp8a")
    p_m1, _ = rp_m1.render(pr7, ["tools/review_prompt.py"], generic=False, objek=objek)
    checks.append((
        "RP8 diuji-mutasi: supresi merge dimatikan -> perintah merge muncul lagi untuk PR pengadil",
        perintah_merge in p_m1,
    ))
    rp_path.write_text(original, encoding="utf-8")

    # Mutasi RP8-2: ganti contoh judul dengan judul tanpa token putusan -> tidak lagi terbaca
    # sebagai slot maupun verdict. Bukti bahwa kata putusan di baris pertama load-bearing.
    mut2 = original.replace(
        'a(f"## Review independen PR #{merge_num} — putaran 1 — VERDICT: MERAH")',
        'a(f"## Catatan untuk PR #{merge_num}")')
    assert mut2 != original, "mutasi RP8-2 tidak mengubah apa pun - uji tidak valid"
    rp_path.write_text(mut2, encoding="utf-8")
    rp_m2 = _load_review_prompt(cp, "review_prompt_mut_rp8b")
    p_m2, _ = rp_m2.render(pr7, ["tools/review_prompt.py"], generic=False, objek=objek)
    j_m2 = [b for b in p_m2.splitlines() if b.startswith("## Catatan untuk PR")]
    checks.append((
        "RP8 diuji-mutasi: contoh judul tanpa token putusan -> BUKAN slot dan verdict TIDAK DITEMUKAN",
        len(j_m2) == 1 and av.slot_hakim(j_m2[0] + "\n") is False
        and av.simpulkan(j_m2[0] + "\n").startswith("TIDAK DITEMUKAN"),
    ))
    rp_path.write_text(original, encoding="utf-8")

    # ------------------------------------------------------------------
    # RP9 - temuan review independen putaran 2 PR #74 (hakim ke-3, dan dikonfirmasi
    # ulang oleh penulis): perbaikan R3 malah MEMBEKUKAN angka pengukurannya sendiri ke
    # dalam kode - "pada PR #74 terukur 53 vs 49 berkas" tercetak untuk SETIAP PR, lalu
    # dibantah oleh angka yang dihitung alat di paragraf berikutnya ((A) 55 / (B) 59).
    # Itu kelas cacat yang sama dengan R3: dokumen yang meyakinkan tetapi tidak cocok
    # dengan data. Keluaran tercetak harus bebas angka beku; angka hanya dari objek_diff().
    # ------------------------------------------------------------------
    objek_rp9 = {"merge_base": MB, "nama_merge_base": ["a.md", "b.md"],
                 "nama_langsung": ["a.md", "b.md", "c.md", "d.md"], "kesalahan": []}
    p_rp9, _ = rp.render(pr7, ["a.md", "b.md"], generic=False, objek=objek_rp9)
    checks.append((
        "RP9 prompt TIDAK memuat angka diff yang dibekukan di kode (53 vs 49)",
        "53 vs 49" not in p_rp9 and "53" not in p_rp9.split("## 3a")[1].split("## 3b")[0],
    ))
    checks.append((
        "RP9 angka selisih yang tercetak berasal dari objek, bukan dari teks tetap",
        "(A) 2 berkas" in p_rp9 and "(B) 4 berkas" in p_rp9
        and "BUKAN perubahan PR ini: 2 berkas" in p_rp9,
    ))

    # Mutasi RP9 - bekukan lagi angkanya di keluaran: pemeriksaan di atas harus gagal.
    mut9 = original.replace(
        'a("**berbeda** begitu base bergerak sejak branch dibuat. Selisihnya **DIHITUNG dan DICETAK di bawah** —")',
        'a("**berbeda** begitu base bergerak sejak branch dibuat — pada PR #74 terukur **53 vs 49 berkas**.")')
    assert mut9 != original, "mutasi RP9 tidak mengubah apa pun - uji tidak valid"
    rp_path.write_text(mut9, encoding="utf-8")
    rp_m9 = _load_review_prompt(cp, "review_prompt_mut_rp9")
    p_m9, _ = rp_m9.render(pr7, ["a.md", "b.md"], generic=False, objek=objek_rp9)
    checks.append((
        "RP9 diuji-mutasi: angka beku dikembalikan ke keluaran -> terdeteksi",
        "53 vs 49" in p_m9,
    ))
    rp_path.write_text(original, encoding="utf-8")

    return checks


def _run_check_selfcontained(repo: Path, system: str, *extra: str):
    return subprocess.run(
        [sys.executable, "-B", "tools/check_selfcontained.py", "--sistem", system, "--report", *extra],
        cwd=str(repo),
        capture_output=True,
        text=True,
        env={**os.environ, "FI_SKIP_NESTED": "1", "PYTHONDONTWRITEBYTECODE": "1"},
    )


def _write_minimal_selfcontained_system(repo: Path, name: str) -> Path:
    root = repo / name
    if root.exists():
        shutil.rmtree(root)
    (root / "_sistem").mkdir(parents=True)
    (root / "README.md").write_text(f"# {name}\n", encoding="utf-8")
    (root / "_sistem" / "validate_system.py").write_text(
        "#!/usr/bin/env python3\nprint('VALIDATOR FI: PASS')\n",
        encoding="utf-8",
    )
    return root


def _derived_label(repo: Path, src_rel: str, *, body: bytes | None = None, diff_line: str = "> Perbedaan: tidak ada\n") -> bytes:
    src = repo / src_rel
    source_body = src.read_bytes() if body is None else body
    sha = hashlib.sha1(src.read_bytes()).hexdigest()
    label = (
        f"> Salinan turunan. Sumber: {src_rel} sha {sha} tanggal 2026-09-08 versi-meta 1.10.0\n"
        f"{diff_line}"
        "> Pemakaian: fixture failure-injection check_selfcontained\n"
    ).encode("utf-8")
    return label + source_body


def check_selfcontained_scenarios(base_dir: Path):
    """SC1-SC10: gerbang folder mandiri wajib bergigi, termasuk mutasi alat.

    SC1-SC5 (PR A, 8 Sep 2026): empat mode gagal + kewajiban baris kedua label.
    SC6-SC10 (PR A2, 9 Sep 2026): tiga pembedaan CAKUPAN alat — area yang tidak
    boleh keluar dari master diminta sebagai provenance (bukan salinan
    berlabel), dokumen bukti tidak ditegakkan tetapi rujukannya tetap terdaftar
    sebagai rujukan historis, dan rujukan ber-backtick ke BERKAS `_meta/...` di
    dokumen aktif tetap gagal. SC9 menjaga pembedaan sebutan area; SC10
    menjaga larangan salinan berlabel dari area yang tidak boleh keluar dari
    master.
    """
    checks = []
    cp = base_dir / "repo_sc"
    shutil.copytree(
        ROOT, cp,
        ignore=shutil.ignore_patterns(
            ".git", "backups", "template_clean", "template_clean.zip",
            "__pycache__", "dist"),
    )
    tool_path = cp / "tools" / "check_selfcontained.py"
    original = tool_path.read_text(encoding="utf-8")

    def scenario(label: str, system: str, setup, expected_code: str, mutation_old: str, mutation_new: str):
        root = _write_minimal_selfcontained_system(cp, system)
        setup(root)
        before = _run_check_selfcontained(cp, system)
        mutated = original.replace(mutation_old, mutation_new, 1)
        if mutated == original:
            return (label + " — penanda mutasi ditemukan", False)
        tool_path.write_text(mutated, encoding="utf-8")
        after = _run_check_selfcontained(cp, system)
        tool_path.write_text(original, encoding="utf-8")
        return (
            label,
            before.returncode != 0
            and f"[{expected_code}]" in before.stdout
            and after.returncode == 0,
        )

    checks.append(scenario(
        "SC1 SELF-PREFIX ditolak; mutasi pemeriksaan membuat fixture lolos",
        "sistem-fi-self-prefix",
        lambda root: (root / "README.md").write_text("# uji\n`sistem-fi-self-prefix/README.md`\n", encoding="utf-8"),
        "SELF-PREFIX",
        'if token.startswith(f"{system}/"):',
        'if False and token.startswith(f"{system}/"):',
    ))
    checks.append(scenario(
        "SC2 MISSING-LABELED-COPY ditolak; mutasi pemeriksaan membuat fixture lolos",
        "sistem-fi-missing-copy",
        lambda root: (root / "README.md").write_text("# uji\n`tools/validate_repo.py`\n", encoding="utf-8"),
        "MISSING-LABELED-COPY",
        'if token.startswith("_meta/") or token.startswith("tools/"):',
        'if False and (token.startswith("_meta/") or token.startswith("tools/")):',
    ))

    def setup_stale(root: Path):
        (root / "_salinan-meta").mkdir()
        src_rel = "_meta/TEMPLATE_LOG_SESI.md"
        stale_body = (cp / src_rel).read_bytes() + b"\nMUTASI STALE-COPY\n"
        (root / "_salinan-meta" / "TEMPLATE_LOG_SESI.md").write_bytes(
            _derived_label(cp, src_rel, body=stale_body)
        )
        (root / "README.md").write_text("# uji\n`_meta/TEMPLATE_LOG_SESI.md`\n", encoding="utf-8")

    checks.append(scenario(
        "SC3 STALE-COPY ditolak; mutasi pemeriksaan membuat fixture lolos",
        "sistem-fi-stale-copy",
        setup_stale,
        "STALE-COPY",
        'if info.body != src_bytes and not diff_declared:',
        'if False and info.body != src_bytes and not diff_declared:',
    ))

    def setup_derived_no_label(root: Path):
        (root / "_salinan-meta").mkdir()
        (root / "_salinan-meta" / "NOTE.md").write_text("# turunan tanpa label\n", encoding="utf-8")

    checks.append(scenario(
        "SC4 DERIVED-NO-LABEL ditolak; mutasi pemeriksaan membuat fixture lolos",
        "sistem-fi-derived-no-label",
        setup_derived_no_label,
        "DERIVED-NO-LABEL",
        'elif looks_like_unlabelled_derivative(rel):',
        'elif False and looks_like_unlabelled_derivative(rel):',
    ))

    def setup_missing_difference_line(root: Path):
        (root / "_salinan-meta").mkdir()
        src_rel = "_meta/TEMPLATE_LOG_SESI.md"
        (root / "_salinan-meta" / "TEMPLATE_LOG_SESI.md").write_bytes(
            _derived_label(cp, src_rel, diff_line="> Pemakaian: sengaja tanpa baris Perbedaan\n")
        )
        (root / "README.md").write_text("# uji\n`_meta/TEMPLATE_LOG_SESI.md`\n", encoding="utf-8")

    mutation_old = (
        "    if not diff_match:\n"
        "        findings.append(\n"
        "            Finding(\n"
        "                \"LABEL-FORMAT\",\n"
        "                f\"{rel}: baris kedua label wajib berbentuk '> Perbedaan: <...>'\",\n"
        "            )\n"
        "        )\n"
        "        return None\n"
        "    diff = diff_match.group(1).strip()"
    )
    mutation_new = (
        "    if not diff_match:\n"
        "        diff = \"\"\n"
        "    else:\n"
        "        diff = diff_match.group(1).strip()"
    )
    checks.append(scenario(
        "SC5 baris kedua Perbedaan wajib; mutasi pemeriksaan membuat fixture lolos",
        "sistem-fi-label-line2",
        setup_missing_difference_line,
        "LABEL-FORMAT",
        mutation_old,
        mutation_new,
    ))

    # --- SC6-SC10 (PR A2): cakupan alat, diuji-mutasi ------------------------
    def scoped_scenario(label, system, setup, mutation_old, mutation_new,
                        expect_before, expect_after):
        """Seperti `scenario`, tetapi ekspektasi sebelum/sesudah mutasi adalah
        predikat atas keluaran alat (bukan hanya exit code + satu kode temuan):
        pembedaan cakupan dinilai dari pesan yang ditawarkan alat."""
        root = _write_minimal_selfcontained_system(cp, system)
        setup(root)
        before = _run_check_selfcontained(cp, system)
        # Ekspektasi perilaku dinilai DULU, sebelum penanda mutasi dicari: kalau
        # pemeriksaannya sudah dilepas dari alat secara permanen, skenario ini
        # harus merah karena PERILAKUNYA hilang, bukan karena teksnya berubah.
        if not expect_before(before):
            return (label + " — perilaku yang diharapkan tidak ada di alat", False)
        mutated = original.replace(mutation_old, mutation_new, 1)
        if mutated == original:
            return (label + " — penanda mutasi tidak ditemukan", False)
        tool_path.write_text(mutated, encoding="utf-8")
        after = _run_check_selfcontained(cp, system)
        tool_path.write_text(original, encoding="utf-8")
        return (label, expect_after(after))

    def setup_master_only_ref(root: Path):
        (root / "README.md").write_text(
            "# uji\n\nAsal prinsip ini: `_meta/_internal/HANDOFF_NEXT_SESSION.md`\n",
            encoding="utf-8",
        )

    checks.append(scoped_scenario(
        "SC6 rujukan area master-only di dokumen AKTIF diminta provenance tanpa backtick, BUKAN salinan berlabel",
        "sistem-fi-master-only-ref",
        setup_master_only_ref,
        "                    forbidden = core.master_only_reason(token)\n"
        "                    if forbidden:",
        "                    forbidden = None\n"
        "                    if forbidden:",
        lambda before: (
            before.returncode != 0
            and "[MASTER-ONLY-REF]" in before.stdout
            and "tulis sebagai provenance tanpa backtick" in before.stdout
            and "[MISSING-LABELED-COPY]" not in before.stdout
        ),
        lambda after: (
            "[MASTER-ONLY-REF]" not in after.stdout
            and "[MISSING-LABELED-COPY]" in after.stdout
        ),
    ))

    def setup_evidence_doc_ref(root: Path):
        (root / "ACCEPTANCE_TEST_LOG.md").write_text(
            "# Bukti run\n\n"
            "Run 1: `tools/test_failure_injection.py` PASS sesuai `_meta/FAILURE_INJECTION_TESTS.md`.\n",
            encoding="utf-8",
        )

    checks.append(scoped_scenario(
        "SC7 rujukan _meta/ di dokumen bukti ACCEPTANCE_TEST_LOG.md bukan kegagalan dan terdaftar sebagai rujukan historis",
        "sistem-fi-evidence-doc",
        setup_evidence_doc_ref,
        "        enforced = rel in active_rel",
        "        enforced = True",
        lambda before: (
            before.returncode == 0
            and "rujukan historis (tidak ditegakkan): 2" in before.stdout
            and "ACCEPTANCE_TEST_LOG.md:3: `tools/test_failure_injection.py`" in before.stdout
            and "ACCEPTANCE_TEST_LOG.md:3: `_meta/FAILURE_INJECTION_TESTS.md`" in before.stdout
            and "[MISSING-LABELED-COPY]" not in before.stdout
        ),
        lambda after: (
            after.returncode != 0
            and "[MISSING-LABELED-COPY]" in after.stdout
            and "rujukan historis (tidak ditegakkan): 0" in after.stdout
        ),
    ))

    def setup_active_meta_file_ref(root: Path):
        (root / "README.md").write_text(
            "# uji\n\nAturan yang dipakai: `_meta/PAKET_REPO_MANDIRI.md`\n",
            encoding="utf-8",
        )

    checks.append(scoped_scenario(
        "SC8 rujukan berkas _meta/ di dokumen aktif tetap MISSING-LABELED-COPY (cakupan baru tidak melonggarkan)",
        "sistem-fi-active-meta-file",
        setup_active_meta_file_ref,
        "                    if token not in labels_by_source:",
        "                    if False and token not in labels_by_source:",
        lambda before: (
            before.returncode != 0
            and "[MISSING-LABELED-COPY]" in before.stdout
            and "_meta/PAKET_REPO_MANDIRI.md" in before.stdout
        ),
        lambda after: after.returncode == 0,
    ))

    def setup_area_mention(root: Path):
        (root / "README.md").write_text(
            "# uji\n\nPrinsip meta ada di `_meta/`, alat regresi ada di `tools/`.\n",
            encoding="utf-8",
        )

    checks.append(scoped_scenario(
        "SC9 rujukan berbentuk direktori di dokumen aktif = sebutan area, bukan kegagalan",
        "sistem-fi-area-mention",
        setup_area_mention,
        "                    if token.endswith(\"/\"):",
        "                    if False and token.endswith(\"/\"):",
        lambda before: (
            before.returncode == 0
            and "sebutan area: 2" in before.stdout
            and "`_meta/`" in before.stdout
            and "[MISSING-LABELED-COPY]" not in before.stdout
        ),
        lambda after: (
            after.returncode != 0
            and "[MISSING-LABELED-COPY]" in after.stdout
        ),
    ))

    def setup_master_only_copy(root: Path):
        """Salinan berlabel yang SUMBERNYA di area master-only: menyalinnya
        pelanggaran, jadi temuan — solusinya hapus salinan, bukan resinkronisasi."""
        (root / "_salinan-meta").mkdir()
        src_rel = "_meta/_internal/HANDOFF_NEXT_SESSION.md"
        (root / "_salinan-meta" / "HANDOFF_NEXT_SESSION.md").write_bytes(
            _derived_label(cp, src_rel)
        )

    checks.append(scoped_scenario(
        "SC10 salinan berlabel dari area master-only ditolak sebagai MASTER-ONLY-COPY (hapus salinannya)",
        "sistem-fi-master-only-copy",
        setup_master_only_copy,
        "        forbidden = core.master_only_reason(src_rel)",
        "        forbidden = None",
        lambda before: (
            before.returncode != 0
            and "[MASTER-ONLY-COPY]" in before.stdout
            and "hapus salinannya dan tulis sebagai provenance tanpa backtick" in before.stdout
        ),
        lambda after: after.returncode == 0 and "[MASTER-ONLY-COPY]" not in after.stdout,
    ))

    # SC11-SC12 (18 Sep 2026): alat yang MENDETEKSI salinan berlabel basi juga harus bisa
    # MEMPERBAIKI. Salinan basi sudah terjadi DUA KALI (v1.18.0 "3 salinan berlabel disinkron", dan
    # 18 Sep 2026 sesudah PROTOKOL_REVIEW_INDEPENDEN.md disunting) — deteksi tanpa perbaikan
    # mendorong penyuntingan salinan dengan tangan, dan itu cara salinan jadi basi tanpa jejak.
    src_rel = "_meta/PLATFORM_LMARENA.md"
    src_master = cp / src_rel
    src_asli = src_master.read_bytes()

    system = "sistem-fi-salinan-basi"
    root = _write_minimal_selfcontained_system(cp, system)
    (root / "_salinan-meta").mkdir()
    salinan = root / "_salinan-meta" / "PLATFORM_LMARENA.md"
    salinan.write_bytes(_derived_label(cp, src_rel))
    sinkron_awal = _run_check_selfcontained(cp, system)  # fixture harus sehat dulu

    # master bergerak -> salinan jadi basi. Inilah kejadian nyatanya, bukan karangan.
    src_master.write_bytes(src_asli + b"\n<!-- mutasi uji FI: master bergerak -->\n")
    before = _run_check_selfcontained(cp, system)
    synced = _run_check_selfcontained(cp, system, "--sinkronkan")
    after = _run_check_selfcontained(cp, system)
    checks.append((
        "SC11 salinan berlabel basi: STALE-COPY terdeteksi, --sinkronkan MEMPERBAIKI, alat lalu PASS",
        sinkron_awal.returncode == 0
        and before.returncode != 0 and "[STALE-COPY]" in before.stdout
        and "DISINKRONKAN" in synced.stdout
        and after.returncode == 0,
    ))

    # SC11b - mutasi: lumpuhkan PENULISAN sinkron. Kalau "perbaikan" itu bohong (mencetak
    # DISINKRONKAN tanpa menulis berkas), salinan tetap basi dan SC11 harus gagal — inilah giginya.
    # Keadaan basi dibangun ulang dari nol: salinan sehat terhadap master LAMA, lalu master bergerak.
    src_master.write_bytes(src_asli)
    salinan.write_bytes(_derived_label(cp, src_rel))
    assert _run_check_selfcontained(cp, system).returncode == 0, "fixture SC11b tidak sehat sejak awal"
    src_master.write_bytes(src_asli + b"\n<!-- mutasi uji FI (2): master bergerak lagi -->\n")
    tool_path.write_text(
        original.replace("            path.write_bytes(baru)\n", "            pass  # mutasi FI\n", 1),
        encoding="utf-8")
    mutasi_berhasil = tool_path.read_text(encoding="utf-8") != original
    mut_run = _run_check_selfcontained(cp, system, "--sinkronkan")
    tool_path.write_text(original, encoding="utf-8")
    checks.append((
        "SC11b diuji-mutasi: penulisan sinkron dilumpuhkan -> salinan TETAP basi (SC11 punya gigi)",
        mutasi_berhasil and mut_run.returncode != 0,
    ))

    # SC12 - salinan yang MENYATAKAN perbedaan nyata tidak boleh ditimpa: itu keputusan orang lain,
    # dan menimpanya diam-diam = menghapus keputusan tanpa jejak.
    system2 = "sistem-fi-salinan-bedanya-dinyatakan"
    root2 = _write_minimal_selfcontained_system(cp, system2)
    (root2 / "_salinan-meta").mkdir()
    salinan2 = root2 / "_salinan-meta" / "PLATFORM_LMARENA.md"
    salinan2.write_bytes(_derived_label(
        cp, src_rel, body=b"# isi fixture yang SENGAJA berbeda\n",
        diff_line="> Perbedaan: fixture FI - isi sengaja berbeda untuk uji SC12\n"))
    sebelum = salinan2.read_bytes()
    run2 = _run_check_selfcontained(cp, system2, "--sinkronkan")
    checks.append((
        "SC12 --sinkronkan TIDAK menimpa salinan yang menyatakan perbedaan nyata",
        salinan2.read_bytes() == sebelum and "DILEWATI" in run2.stdout
        and "tidak boleh ditimpa" in run2.stdout,
    ))

    src_master.write_bytes(src_asli)

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

    # AT-16/C5: corpus counts are forbidden even when pinned to a SHA.
    def c5_mutation(text):
        with TemporaryDirectory() as d:
            cp = Path(d) / "repo"
            shutil.copytree(ROOT, cp, ignore=shutil.ignore_patterns(".git"))
            mp = cp / "_meta/SYSTEM_MANIFEST.md"
            mt = mp.read_text(encoding="utf-8")
            old = "verdict PASS 0-warning; angka stabil tetap"
            mp.write_text(mt.replace(old, text, 1), encoding="utf-8")
            r = subprocess.run([sys.executable, "tools/validate_repo.py"], cwd=cp, capture_output=True)
            return r.returncode
    checks.append(("C5 377 rujukan ditolak", c5_mutation("377 rujukan") != 0))
    checks.append(("C5 377 rujukan pada SHA tetap ditolak", c5_mutation("377 rujukan pada 2a717dce93f098d2f61d260d1413f2207f1dbb78") != 0))
    checks.append(("C5 PASS 0-warning angka stabil lolos", c5_mutation("PASS 0-warning (29 wajib)") == 0))

    # Penjaga drift Status/Versi pada manifest meta. Uji drift-nya TIDAK menyebut versi nyata
    # (hanya Status yang diganti, Versi dibiarkan apa adanya) supaya skenario ini tidak
    # membusuk setiap kali versi manifest naik.

    def versi_status(status_line, versi_line=None):
        with TemporaryDirectory() as d:
            cp = Path(d) / "repo"
            shutil.copytree(ROOT, cp, ignore=shutil.ignore_patterns(".git"))
            mp = cp / "_meta/SYSTEM_MANIFEST.md"
            mt = mp.read_text(encoding="utf-8")
            mt2 = re.sub(r"^- \*\*Status:\*\* `[^`]*`$", status_line, mt, count=1, flags=re.MULTILINE)
            assert mt2 != mt, "mutasi Status tidak mengubah apa pun - uji tidak valid"
            if versi_line is not None:
                mt3 = re.sub(r"^- \*\*Versi:\*\* `[^`]*`$", versi_line, mt2, count=1, flags=re.MULTILINE)
                assert mt3 != mt2, "mutasi Versi tidak mengubah apa pun - uji tidak valid"
                mt2 = mt3
            mp.write_text(mt2, encoding="utf-8")
            r = subprocess.run([sys.executable, "tools/validate_repo.py"], cwd=cp,
                               capture_output=True, text=True)
            return r.returncode, r.stdout

    # Kontrol positif dulu: kalau keadaan selaras tidak lolos, dua uji di bawah tidak berarti.
    # Pasangan versi yang dipakai SENGAJA berbeda dari yang nyata (9.9.9) supaya mutasinya
    # benar-benar mengubah berkas - menulis ulang nilai yang sudah sama adalah mutasi no-op
    # dan assert di dalam versi_status() akan (dengan benar) menolaknya.
    checks.append(("manifest selaras (Status = Versi, pasangan 9.9.9) lolos",
                   versi_status("- **Status:** `Released — v9.9.9`", "- **Versi:** `9.9.9`")[0] == 0))
    rc_drift, out_drift = versi_status("- **Status:** `Released — v0.0.1`", None)
    checks.append(("Status tertinggal dari Versi ditolak + alasannya tercetak (drift nyata dua bump terakhir)",
                   rc_drift != 0 and "bergerak bersama" in out_drift))
    checks.append(("Status tanpa versi ditolak karena bentuknya yang dipakai mendeteksi drift",
                   versi_status("- **Status:** `Released`", None)[0] != 0))

    # D-2b: penjaga "satu klaim total per baris" diuji — penghitungnya (satuan) dan
    # kabelnya ke exit code (ujung-ke-ujung, dengan FI_NESTED supaya tidak rekursif).
    _bersih = "**Jumlah:** 99 skenario di master (18 sintetis + 17 unit nyata) disalin dari cetakan alat."
    checks.append(("D-2b baris bersih -> tepat 1 klaim total", klaim_total(_bersih) == 1))
    checks.append(("D-2b total kedua gaya 'kini **N**' -> 2 klaim (ditolak)",
                   klaim_total(_bersih + " Jumlah di branch ini kini **73** — disalin dari cetakan.") == 2))
    checks.append(("D-2b total kedua gaya kutipan cetakan -> 2 klaim (ditolak)",
                   klaim_total(_bersih + " (`FAILURE-INJECTION TESTS PASSED: 75 scenarios (15 sintetis)`)") == 2))
    checks.append(("D-2b riwayat penambahan BUKAN klaim total (tidak ikut dihitung)",
                   klaim_total(_bersih + " Angka **84 → 87** muncul karena 3 skenario sintetis ditambahkan; "
                                         "RP8 (10 pemeriksaan) mengunci dua cacat prompt.") == 1))
    # Uji ujung-ke-ujung ini hanya di MASTER. Di ekstrak template ia redundan (penjaga D-2b
    # yang sesungguhnya sudah berjalan pada dokumen nyata di sana) dan mahal: FI di ekstrak
    # dipanggil build_template, jadi tanpa pembatasan ini setiap smoke extract membayar satu
    # pemanggilan FI bersarang lagi. Dideteksi dari KEADAAN (folder benih hanya ada di ekstrak),
    # mengikuti cara `_di_ekstrak` ditentukan di bagian D-2 — bukan dari variabel lingkungan.
    _di_ekstrak_lokal = (ROOT / "sistem-benih").is_dir()
    if not os.environ.get("FI_NESTED") and not _di_ekstrak_lokal:
        with TemporaryDirectory() as d:
            cp = Path(d) / "repo"
            shutil.copytree(ROOT, cp, ignore=shutil.ignore_patterns(
                ".git", "backups", "template_clean", "template_clean.zip", "__pycache__", "dist"))
            dp = cp / "_meta/FAILURE_INJECTION_TESTS.md"
            dt = dp.read_text(encoding="utf-8")
            _l = dt.splitlines(keepends=True)
            _k = next(k for k, x in enumerate(_l) if x.startswith("**Jumlah:**"))
            _l[_k] = _l[_k].rstrip("\n") + " Jumlah di branch ini kini **73** — disalin dari cetakan alat.\n"
            dp.write_text("".join(_l), encoding="utf-8")
            assert "kini **73**" in dp.read_text(encoding="utf-8"), "mutasi D-2b tidak menempel"
            r = subprocess.run([sys.executable, "tools/test_failure_injection.py"], cwd=cp,
                               capture_output=True, text=True,
                               env=dict(os.environ, FI_NESTED="1"))
            checks.append(("D-2b ujung-ke-ujung: dokumen ber-total ganda -> alat exit non-zero dan menyebut D-2b",
                           r.returncode != 0 and "D-2b" in r.stdout))

    # Inventaris inti tidak boleh punya entri ganda: duplikat membuat validator mencetak angka
    # kewajiban yang lebih tinggi dari kenyataan (35 vs 34) dan angka itu menyebar ke dokumen.
    checks.append(("CORE_TOOL_FILES tidak punya entri ganda (angka kewajiban yang dicetak = berkas unik)",
                   len(core.CORE_TOOL_FILES) == len(set(core.CORE_TOOL_FILES))))
    checks.append(("CORE_REQUIRED tidak punya entri ganda",
                   len(core.CORE_REQUIRED) == len(set(core.CORE_REQUIRED))))

    n_synth = len(checks)

    # Regression against REAL repo data (F3): every registered system must
    # have at least one unit STATUS, and every unit STATUS that claims to
    # be safe must actually satisfy the shared checker.
    index_text = (ROOT / "_meta" / "INDEKS_SISTEM.md").read_text(encoding="utf-8")
    registered = set(core.parse_index(index_text)[0])
    real = []
    for sys_dir in sorted(list(ROOT.glob("sistem/sistem-*/")) + list(ROOT.glob("sistem-*/"))):
        sys_rel = sys_dir.relative_to(ROOT).as_posix()
        files = core.unit_status_files(sys_dir)
        is_reg = sys_rel in registered or sys_dir.name in registered
        if is_reg and not files:
            checks.append((f"registered system {sys_rel} punya unit STATUS (F3)", False))
            continue
        for status_path in files:
            real.append((status_path, core.state_is_safe(status_path.parent)))
    for status_path, safe in real:
        checks.append((f"real unit consistent: {status_path.relative_to(ROOT)}", safe))

    # R1–R8 regression scenarios (skipped when nested — FI_SKIP_NESTED).
    reg = []
    if not os.environ.get("FI_SKIP_NESTED"):
        with TemporaryDirectory() as d:
            reg = regression_scenarios(Path(d))
    checks += reg

    # SC1–SC5 gerbang folder mandiri (skipped when nested, same reason).
    sc_checks = []
    if not os.environ.get("FI_SKIP_NESTED"):
        with TemporaryDirectory() as d:
            sc_checks = check_selfcontained_scenarios(Path(d))
    checks += sc_checks

    # RP1–RP4 pembangkit prompt review (skipped when nested, same reason).
    rp_checks = []
    if not os.environ.get("FI_SKIP_NESTED"):
        with TemporaryDirectory() as d:
            rp_checks = review_prompt_scenarios(Path(d))
    checks += rp_checks

    # --- D-2 (temuan R2 review PR #74): penjaga sinkron jumlah skenario vs dokumen ---
    # Sebelumnya angka di _meta/FAILURE_INJECTION_TESTS.md adalah SALINAN TANGAN, sehingga
    # menambah satu sistem terdaftar (yang menaikkan "unit nyata") membuat dokumen tertinggal
    # TANPA terdeteksi alat apa pun. Sekarang selisihnya adalah kegagalan, bukan catatan.
    # Mode DIDETEKSI DARI KEADAAN, bukan dari variabel lingkungan: di ekstrak template ketiga
    # grup regresi tidak dijalankan, jadi ketiganya kosong. Versi pertama penjaga ini hanya
    # membandingkan angka master (74) dan membuat smoke extract GAGAL karena di sana jumlahnya 16.
    _di_ekstrak = not (reg or sc_checks or rp_checks)
    if not os.environ.get("FI_SKIP_NESTED"):
        doc = ROOT / "_meta" / "FAILURE_INJECTION_TESTS.md"
        if not doc.is_file():
            print("FAILURE-INJECTION TESTS FAILED")
            print(f"- D-2: dokumen inventaris tidak ditemukan: {doc}")
            raise SystemExit(1)
        _teks_doc = doc.read_text(encoding="utf-8")
        if _di_ekstrak:
            m = re.search(r"(\d+)\s*di ekstrak template\s*\(([^)]*)\)", _teks_doc)
            _pola = "**Jumlah:** ... N di ekstrak template (...)"
        else:
            m = re.search(r"^\*\*Jumlah:\*\*\s*(\d+)\s*skenario di master\s*\(([^)]*)\)",
                          _teks_doc, re.M)
            _pola = "**Jumlah:** N skenario di master (...)"
        if not m:
            print("FAILURE-INJECTION TESTS FAILED")
            print(f"- D-2: baris '{_pola}' tidak ditemukan/tidak terparse "
                  f"di _meta/FAILURE_INJECTION_TESTS.md")
            raise SystemExit(1)
        # D-2b (pengetatan 18 Sep 2026): baris itu harus memuat TEPAT SATU klaim total.
        # Berlaku di KEDUA mode (master dan ekstrak): dokumennya berkas yang sama, dan
        # uji ujung-ke-ujung D-2b juga dijalankan di dalam ekstrak oleh build_template.
        _baris_jumlah = next((l for l in _teks_doc.splitlines()
                              if l.startswith("**Jumlah:**")), "")
        _n_klaim = klaim_total(_baris_jumlah)
        if _n_klaim != 1:
            print("FAILURE-INJECTION TESTS FAILED")
            print(
                f"- D-2b: baris '**Jumlah:**' di _meta/FAILURE_INJECTION_TESTS.md memuat "
                f"{_n_klaim} klaim total (harus TEPAT 1). Dokumen yang membantah dirinya "
                "sendiri di satu baris tidak bisa jadi acuan. Buang total yang basi — "
                "JANGAN melonggarkan penghitung `klaim_total()`, dan jangan menghapus "
                "riwayat penambahan (riwayat bukan klaim total)."
            )
            raise SystemExit(1)
        # Parsing PER KOMPONEN BERNAMEKA, bukan "ambil semua angka": versi pertama penjaga ini
        # memakai re.findall(r"\d+") dan ikut menangkap angka 11 dari label "regresi review PR-11",
        # sehingga penjaganya sendiri melaporkan selisih palsu. Tertangkap oleh uji pertamanya.
        komponen = [("sintetis", n_synth), ("unit nyata", len(real))]
        if not _di_ekstrak:
            komponen += [("regresi review PR-11", len(reg)),
                         ("regresi check_selfcontained", len(sc_checks)),
                         ("regresi review_prompt", len(rp_checks))]
        angka_doc, aktual, hilang = [], [], []
        for label, nilai in komponen:
            mm = re.search(rf"(\d+)\s+{re.escape(label)}", m.group(2))
            if not mm:
                hilang.append(label)
            else:
                angka_doc.append(int(mm.group(1)))
            aktual.append(nilai)
        if hilang:
            print("FAILURE-INJECTION TESTS FAILED")
            print(f"- D-2: komponen tidak ditemukan di baris '**Jumlah:**' dokumen: {hilang}. "
                  f"Penjaga ini menolak menebak — perbaiki label di dokumen atau di penjaga.")
            raise SystemExit(1)
        if int(m.group(1)) != len(checks) or angka_doc != aktual:
            print("FAILURE-INJECTION TESTS FAILED")
            print(f"- D-2: jumlah skenario tidak sinkron dengan _meta/FAILURE_INJECTION_TESTS.md baris "
                  f"'**Jumlah:**' — dokumen menulis {m.group(1)} ({angka_doc}), alat mencetak "
                  f"{len(checks)} ({aktual}). Perbarui DOKUMENNYA dari cetakan alat; "
                  f"JANGAN mengurangi skenario atau menggeser pin agar cocok dengan angka lama.")
            raise SystemExit(1)

    failed = [name for name, ok in checks if not ok]
    if failed:
        print("FAILURE-INJECTION TESTS FAILED")
        for name in failed:
            print(f"- {name}")
        raise SystemExit(1)
    print(f"FAILURE-INJECTION TESTS PASSED: {len(checks)} scenarios "
          f"({n_synth} sintetis + {len(real)} unit nyata + {len(reg)} regresi review PR-11"
          f" + {len(sc_checks)} regresi check_selfcontained"
          f" + {len(rp_checks)} regresi review_prompt)")


if __name__ == "__main__":
    run()
