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
import inspect
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
    perilaku). Kini yang diuji: argv yang benar-benar dipakai `fetch_pr_files`
    (RP5b) dan penjaga konsistensi `resolve_pr_files` yang menolak daftar tak
    konsisten (RP5a) — dua-duanya diuji-mutasi, dan mutasi yang tidak
    mengubah apa pun membuat uji gagal (bukan lolos palsu).
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
    mutated = original.replace('if log.name in writer_logs:', 'if False and log.name in writer_logs:')
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

    return checks


def _run_check_selfcontained(repo: Path, system: str):
    return subprocess.run(
        [sys.executable, "-B", "tools/check_selfcontained.py", "--sistem", system, "--report"],
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
