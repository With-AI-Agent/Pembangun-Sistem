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

# These two Run 22 production units live at the repository-root
# `_produksi-aktif/` scope, not below a registered `sistem-*` directory.  The
# generic real-unit sweep below therefore cannot discover them.  Keep this
# explicit, narrow list so the actual checkpoint state of the two acceptance
# artifacts is covered without changing the registered-system enumeration.
RUN22_REAL_PRODUCTION_UNITS = (
    "_produksi-aktif/toko-bu-sinta-kotak-amal-kecil",
    "_produksi-aktif/toko-bu-sinta-lampu-teras",
)

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


def run_tool_out(repo: Path, tool: str):
    """Seperti `run_tool` tetapi mengembalikan (rc, keluaran gabungan).

    Diperlukan RP23: penurunan severity menjadi WARNING hanya bisa dibuktikan kalau
    teks warningnya dibaca, bukan cuma kode keluarnya - "lulus" dan "lulus karena
    pemeriksaannya dilewati diam-diam" tidak bisa dibedakan dari rc saja."""
    p = subprocess.run(
        [sys.executable, str(repo / tool)],
        capture_output=True, text=True,
        env={**os.environ, "FI_SKIP_NESTED": "1"},
    )
    return p.returncode, p.stdout + p.stderr


def _pindah_ke_kronologi(t: str, m) -> str:
    """RP22f: buang baris cap dari blok header, taruh di kronologi (luar header)."""
    baris = m.group(0)
    tanpa = "\n".join(g for g in t.split("\n") if not g.startswith("- **Segar pada:**")) + "\n"
    return tanpa.rstrip("\n") + "\n\n### Entri uji FI\n\n" + baris + "\n"


def _duplikat_kontradiktif(t: str, m) -> str:
    """RP22g: dua baris cap di blok header dengan angka FI yang berbeda."""
    baris = m.group(0)
    return t.replace(baris, baris + "\n" + baris.replace("FI " + m.group(2), "FI 1"), 1)


def _bungkus_pagar_kode(t: str, m) -> str:
    """RP22h: baris cap dibungkus pagar kode - contoh format, bukan field keadaan."""
    return t.replace(m.group(0), "```\n" + m.group(0) + "\n```", 1)


def root_production_unit_is_safe(unit: Path) -> bool:
    """Check the checkpoint contract for a root-level production unit.

    Unlike generic system units, production folders use their model-specific
    output names (`naskah-draft.md` and `breakdown-output.md`) rather than a
    generic `OUTPUT.md`.  Run 22's two units are explicitly covered here so
    their real repo state is tested without pretending they are registered
    systems.
    """
    status = unit / "STATUS.md"
    if not status.is_file():
        return False
    text = status.read_text(encoding="utf-8")
    kind, value = core.parse_unsaved_field(text)
    if kind != "value" or value != core.SAFE_VALUE:
        return False
    return (
        (unit / "naskah-draft.md").is_file()
        and (unit / "breakdown-output.md").is_file()
        and any((unit / "assets").glob("*"))
    )


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


def bandingkan_jumlah_dokumen(teks_doc: str, komponen: list, total_aktual: int,
                              di_ekstrak: bool) -> list:
    """Bandingkan baris `**Jumlah:**` dokumen inventaris dengan cetakan alat. MURNI: tanpa SystemExit.

    Mengembalikan daftar pesan kegagalan (kosong = sinkron). Dipisah dari `run()` supaya **bisa diuji** —
    dan itu bukan soal kerapian: temuan #1 hakim putaran 3 PR #74 membuktikan pembanding ini tidak
    pernah jalan di mode ekstrak, karena seluruh bloknya terbungkus `if not FI_SKIP_NESTED` padahal
    satu-satunya pemanggil yang menjalankan ekstrak (`build_template.smoke_extract`) justru menyetel
    `FI_SKIP_NESTED=1`. Terukur: dokumen menulis "16 di ekstrak template (15 sintetis + 1 unit nyata
    benih)" sementara cetakan ekstrak 25 (24 sintetis + 1 unit) — dan tidak ada satu alat pun protes.

    Pengetatan **D-2c** (baru, dari temuan yang sama): klaim jumlah ekstrak harus **TEPAT SATU**. Di
    dokumen repo ini klaim itu terganda dua kali pada baris yang sama; dua angka di satu baris adalah
    pola yang sudah ditutup D-2b untuk angka master, jadi penutupannya disamakan.
    """
    gagal: list = []
    if di_ekstrak:
        semua = re.findall(r"(\d+)\s*di ekstrak template\s*\(([^)]*)\)", teks_doc or "")
        if len(semua) > 1:
            gagal.append(
                f"D-2c: baris jumlah memuat {len(semua)} klaim 'di ekstrak template' "
                f"({[a for a, _b in semua]}) — harus TEPAT 1. Dua angka di satu dokumen bisa saling "
                "membantah; buang yang duplikat/basi, JANGAN melonggarkan penghitung ini.")
        m = re.search(r"(\d+)\s*di ekstrak template\s*\(([^)]*)\)", teks_doc or "")
        pola = "**Jumlah:** ... N di ekstrak template (...)"
    else:
        m = re.search(r"^\*\*Jumlah:\*\*\s*(\d+)\s*skenario di master\s*\(([^)]*)\)",
                      teks_doc or "", re.M)
        pola = "**Jumlah:** N skenario di master (...)"
    if not m:
        gagal.append(f"D-2: baris '{pola}' tidak ditemukan/tidak terparse "
                     "di _meta/FAILURE_INJECTION_TESTS.md")
        return gagal
    baris = next((l for l in (teks_doc or "").splitlines() if l.startswith("**Jumlah:**")), "")
    n_klaim = klaim_total(baris)
    if n_klaim != 1:
        gagal.append(
            f"D-2b: baris '**Jumlah:**' di _meta/FAILURE_INJECTION_TESTS.md memuat {n_klaim} klaim total "
            "(harus TEPAT 1). Dokumen yang membantah dirinya sendiri di satu baris tidak bisa jadi "
            "acuan. Buang total yang basi — JANGAN melonggarkan penghitung `klaim_total()`, dan jangan "
            "menghapus riwayat penambahan (riwayat bukan klaim total).")
        return gagal
    angka_doc, aktual, hilang = [], [], []
    for label, nilai in komponen:
        mm = re.search(rf"(\d+)\s+{re.escape(label)}", m.group(2))
        if not mm:
            hilang.append(label)
        else:
            angka_doc.append(int(mm.group(1)))
        aktual.append(nilai)
    if hilang:
        gagal.append(f"D-2: komponen tidak ditemukan di baris '**Jumlah:**' dokumen: {hilang}. "
                     "Penjaga ini menolak menebak — perbaiki label di dokumen atau di penjaga.")
        return gagal
    if gagal:
        return gagal
    if int(m.group(1)) != total_aktual or angka_doc != aktual:
        gagal.append(
            f"D-2: jumlah skenario tidak sinkron dengan _meta/FAILURE_INJECTION_TESTS.md baris "
            f"'**Jumlah:**' — dokumen menulis {m.group(1)} ({angka_doc}), alat mencetak "
            f"{total_aktual} ({aktual}). Perbarui DOKUMENNYA dari cetakan alat; JANGAN mengurangi "
            "skenario atau menggeser pin agar cocok dengan angka lama.")
    return gagal



def selisih_populasi_dari_garis_lain(teks_doc: str, komponen: list, total_aktual: int,
                                     unit_paths: list, git, ada_git: bool):
    """Putuskan apakah selisih D-2 boleh DITURUNKAN jadi peringatan karena datang dari garis riwayat lain.

    MURNI (`git` disuntikkan sebagai callable) supaya bisa diuji tanpa repo — pola yang sama dengan
    `bandingkan_jumlah_dokumen` dan `klaim_total`. Mengembalikan `(boleh_diturunkan, alasan)`.

    Konteks nyata (19 Sep 2026, diukur pada pohon hasil merge PR #74 di atas `main` `98d3cb7`): `main`
    menambah satu unit produksi yang tidak ada di branch ini
    (`sistem/sistem-konten-kreator/_produksi-aktif/toko-bu-sinta-bangku-tua`). Sesudah merge, grup
    "unit nyata" naik 19 -> 20, jadi angka dokumen yang ditulis branch ini (190) **tidak mungkin benar**
    di pohon hasil merge, dan D-2 memerahkan gerbang wajib FI di `main` seketika sesudah merge — untuk
    pelanggaran yang tidak dilakukan siapa pun di branch ini dan yang tidak bisa dicegah penulisnya.
    Itu kelas cacat yang sama dengan temuan #2 hakim C putaran 7, dan aturan C8 menuntut severity
    dijajarkan dengan siapa yang bisa bertindak.

    Pembedanya ANCESTRY, bukan niat: bila ada unit yang ditambahkan oleh commit yang merupakan
    DESCENDANT dari commit terakhir yang memperbarui dokumen, penulis dokumen itu seharusnya sudah
    menghitungnya -> penjaga tetap KERAS (giginya utuh, termasuk untuk `main` sesudah merge). Bila
    tidak ada satu pun — semua unit sudah ada sebelum dokumen diperbarui di garisnya, atau datang dari
    garis yang menyimpang lalu diserap merge — selisihnya milik pohon hasil merge -> PERINGATAN beralasan.
    """
    if not ada_git:
        return False, "tidak ada .git di root repo, asal-usul unit tidak bisa ditentukan"
    m = re.search(r"^\*\*Jumlah:\*\*\s*(\d+)\s*skenario di master\s*\(([^)]*)\)", teks_doc or "", re.M)
    if not m:
        return False, "baris '**Jumlah:** N skenario di master (...)' tidak terparse"
    doc_unit = aktual_unit = None
    beda = []
    for label, nilai in komponen:
        mm = re.search(rf"(\d+)\s+{re.escape(label)}", m.group(2))
        if not mm:
            return False, f"komponen '{label}' tidak ditemukan di baris jumlah dokumen"
        if int(mm.group(1)) != nilai:
            beda.append(label)
        if label == "unit nyata":
            doc_unit, aktual_unit = int(mm.group(1)), nilai
    if beda != ["unit nyata"]:
        return False, f"selisih menyentuh komponen {beda or 'lain'}, bukan kelebihan populasi unit semata"
    if aktual_unit is None or doc_unit is None or aktual_unit <= doc_unit:
        return False, "jumlah unit nyata alat tidak lebih besar dari dokumen (populasi menyusut, bukan bertambah)"
    if total_aktual - int(m.group(1)) != aktual_unit - doc_unit:
        return False, "selisih total tidak sama dengan selisih unit nyata, jadi ada penyebab lain"
    doc_commit = git("log", "-n", "1", "--format=%H", "--",
                     "_meta/FAILURE_INJECTION_TESTS.md").stdout.strip()
    if not doc_commit:
        return False, "commit terakhir yang memperbarui dokumen tidak terbaca dari riwayat"
    sesudah_doc = []
    for rel in unit_paths:
        add = git("log", "--diff-filter=A", "-n", "1", "--format=%H", "--", rel).stdout.strip()
        if add and add != doc_commit and git("merge-base", "--is-ancestor", doc_commit, add).returncode == 0:
            sesudah_doc.append(rel)
    if sesudah_doc:
        return False, ("ada unit yang ditambahkan SESUDAH dokumen terakhir diperbarui di garis riwayat "
                       "yang sama: " + ", ".join(sesudah_doc[:3]))
    return True, ("semua unit di pohon ini sudah ada sebelum dokumen terakhir diperbarui di garis "
                  "riwayatnya, jadi kelebihan populasi datang dari garis lain yang diserap merge")


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

    # Mutasi RP2: kembalikan perilaku LAMA sepenuhnya. Dua perubahan perlu, bukan satu: sesudah
    # cabang catch-all dipasang (temuan #6 hakim putaran 3), berkas yang jatuh dari filter `.md`
    # tertangkap cabang terakhir, sehingga mutasi versi lama menjadi NO-OP dan uji ini kehilangan
    # giginya (terukur 18 Sep 2026: RP2 GAGAL sesudah catch-all ada). Jadi mutasinya harus meniru
    # kode lama apa adanya: filter `.md` dipersempit DAN catch-all dimatikan.
    mutated = original.replace('elif rel.endswith(".md"):', 'elif rel.endswith(".md") and "/" in rel:')
    mutated = mutated.replace("""        else:
            # Temuan hakim putaran 3 PR #74 (#6):""", """        elif False:
            # Temuan hakim putaran 3 PR #74 (#6):""")
    assert mutated != original, "mutasi RP2 tidak mengubah apa pun - uji tidak valid"
    # Sesudah mutasi pola itu muncul DUA kali: cabang ".md ber-slash" yang memang sudah ada, dan
    # cabang ".md root" yang baru dipersempit. Yang wajib hilang adalah cabang lama yang tak bersyarat.
    assert mutated.count('elif rel.endswith(".md") and "/" in rel:') == 2, "mutasi RP2 filter .md tidak masuk"
    assert 'elif rel.endswith(".md"):' not in mutated, "cabang .md root yang lama masih ada - mutasi gagal"
    assert "        elif False:\n            # Temuan hakim putaran 3" in mutated, "mutasi RP2 catch-all tidak masuk"
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

    # ------------------------------------------------------------------
    # RP10 - nomor putaran review DICETAK dari perhitungan kanal, bukan ditebak hakim.
    # Cacat nyatanya: prompt menyuruh "ganti `putaran 1` dengan angka yang sebenarnya" dan menyebut
    # "maksimal 2 putaran" sebagai fakta tetap; begitu pemilik membuka putaran 3 (18 Sep 2026),
    # keduanya salah dan hakim dipaksa menebak — tebakan salah = slot verdict salah dikelompokkan.
    # ------------------------------------------------------------------
    p_rp10, _ = rp.render(pr7, ["a.md", "b.md"], generic=False, objek=objek_rp9, putaran=3)
    checks.append((
        "RP10 nomor putaran yang dicetak = yang dihitung (putaran 3), bukan beku di angka 1",
        "putaran 3 — VERDICT: MERAH" in p_rp10
        and "DIHITUNG ALAT" in p_rp10
        and "Ganti `putaran 1`" not in p_rp10
        and "Review ini **putaran 3**" in p_rp10,
    ))
    checks.append((
        "RP10 prompt tidak lagi membekukan riwayat SATU PR sebagai diagnosis semua PR",
        "pada PR ini dua verdict putaran pertama" not in p_rp10
        and "jangan mewarisi diagnosis PR lain" in p_rp10,
    ))
    p_rp10b, _ = rp.render(pr7, ["a.md", "b.md"], generic=False, objek=objek_rp9, putaran=None)
    checks.append((
        "RP10 kalau kanal tak terbaca: prompt menyuruh HITUNG SENDIRI, tidak mencetak angka salah",
        "hitung sendiri" in p_rp10b and "putaran 1 — VERDICT: MERAH" in p_rp10b,
    ))

    # Mutasi RP10 - bekukan lagi nomor putarannya: pemeriksaan pertama harus gagal.
    mut10 = original.replace(
        'a(f"## Review independen PR #{merge_num} — putaran {putaran} — VERDICT: MERAH")',
        'a(f"## Review independen PR #{merge_num} — putaran 1 — VERDICT: MERAH")')
    assert mut10 != original, "mutasi RP10 tidak mengubah apa pun - uji tidak valid"
    rp_path.write_text(mut10, encoding="utf-8")
    rp_m10 = _load_review_prompt(cp, "review_prompt_mut_rp10")
    p_m10, _ = rp_m10.render(pr7, ["a.md", "b.md"], generic=False, objek=objek_rp9, putaran=3)
    checks.append((
        "RP10 diuji-mutasi: nomor putaran dibekukan ke 1 -> terdeteksi",
        "putaran 3 — VERDICT: MERAH" not in p_m10,
    ))
    rp_path.write_text(original, encoding="utf-8")

    # ------------------------------------------------------------------
    # RP11 - prompt wajib menyebut CARA MENEMPEL verdict + kewajiban memverifikasinya.
    # Cacat nyatanya: pada putaran sebelumnya di repo ini dua dari tiga verdict TIDAK PERNAH SAMPAI
    # ke GitHub dan kuorum gagal tanpa pesan error. Prompt mengatur format verdict sampai se-detail
    # itu, tetapi tidak pernah menyebut cara menempelnya — jadi langkah yang paling mudah gagal
    # justru satu-satunya yang tidak dijelaskan.
    # ------------------------------------------------------------------
    checks.append((
        "RP11 prompt menyebut perintah tempel verdict lewat REST + slug repo",
        "comments --input /tmp/verdict.json" in p_rp10 and "gh api repos/" in p_rp10,
    ))
    checks.append((
        "RP11 prompt mewajibkan VERIFIKASI bahwa verdict benar-benar tertempel",
        "VERIFIKASI tertempel" in p_rp10 and "jangan mengandalkan exit code" in p_rp10,
    ))
    checks.append((
        "RP11 prompt memperingatkan `gh pr comment` tidak diandalkan (gejala gagalnya menipu)",
        "jangan diandalkan" in p_rp10 and "projectCards" in p_rp10,
    ))

    # Mutasi RP11 - buang perintah tempelnya dari keluaran: pemeriksaan pertama harus gagal.
    # Anchor mutasi diambil dari teks yang benar-benar tercetak, bukan dari kutipan bersarang.
    mut11 = original.replace("comments --input /tmp/verdict.json", "comments-PERINTAH-DIBUANG")
    assert mut11 != original, "mutasi RP11 tidak mengubah apa pun - uji tidak valid"
    rp_path.write_text(mut11, encoding="utf-8")
    rp_m11 = _load_review_prompt(cp, "review_prompt_mut_rp11")
    p_m11, _ = rp_m11.render(pr7, ["a.md", "b.md"], generic=False, objek=objek_rp9, putaran=3)
    checks.append((
        "RP11 diuji-mutasi: perintah tempel verdict dibuang -> terdeteksi",
        "comments --input /tmp/verdict.json" not in p_m11,
    ))
    rp_path.write_text(original, encoding="utf-8")

    # ------------------------------------------------------------------
    # RP12 - blok serah terima: path absolut + link, DICETAK ALAT, bukan ditulis tangan agent.
    # Cacat nyatanya (keluhan pemilik giliran 19, 18 Sep 2026): prompt review diserahkan dengan
    # menyebut NAMA BERKAS saja, tanpa path absolut dan tanpa link, sehingga pemilik - yang
    # menyatakan tidak punya basic coding - harus mencari sendiri berkasnya dan bingung. Pemilik
    # lalu menetapkan aturan tetap: "Setiap menyiapkan review independen dan pemeriksaan
    # menyeluruh independen, agent harus beri link nya." Link yang ditulis tangan bisa salah atau
    # ketinggalan: kelas cacat yang sama dengan angka beku (RP9/RP10), jadi dicetak dari data terukur.
    # ------------------------------------------------------------------
    import contextlib
    import io

    SLUG_UJI = "With-AI-Agent/Pembangun-Sistem"
    SHA_UJI = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6abcd"
    serah12 = rp.handoff_block(74, SHA_UJI, "/tmp/rp12_uji.md", slug=SLUG_UJI)
    checks.append((
        "RP12 blok serah terima memuat path absolut + link PR + permalink head",
        "/tmp/rp12_uji.md" in serah12
        and f"https://github.com/{SLUG_UJI}/pull/74" in serah12
        and f"https://github.com/{SLUG_UJI}/commit/{SHA_UJI}" in serah12
        and "BLOK SERAH TERIMA" in serah12,
    ))
    checks.append((
        "RP12 fail-closed: slug tak terbaca -> link PR TIDAK dicetak (bukan link karangan)",
        (lambda t: "https://github.com/<OWNER>" not in t and "TIDAK DICETAK" in t)(
            rp.handoff_block(74, SHA_UJI, "/tmp/rp12_uji.md", slug="<OWNER>/<REPO>")),
    ))
    checks.append((
        "RP12 blok serah terima memuat perintah regenerasi + pengumpul verdict + wajib verifikasi",
        "review_prompt.py --pr 74" in serah12
        and "ambil_verdict.py --pr 74" in serah12
        and "WAJIB memverifikasi" in serah12,
    ))

    # main() harus benar-benar MENEMPEL blok itu ke berkas prompt - punya fungsinya saja tidak cukup
    # (regresi senyap yang mungkin: fungsi ada tetapi tidak pernah dipanggil dari jalur penulisan).
    out12 = base_dir / "rp12_prompt.md"
    buf12o, buf12e = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(buf12o), contextlib.redirect_stderr(buf12e):
        rc12 = rp.main(["--generic", "--out", str(out12)])
    teks12 = out12.read_text(encoding="utf-8") if out12.is_file() else ""
    checks.append((
        "RP12 main() menempel blok serah terima ke berkas prompt + meneriakkannya ke stderr",
        rc12 == 0 and "BLOK SERAH TERIMA" in teks12
        and "BLOK SERAH TERIMA" in buf12e.getvalue()
        and str(out12) in buf12e.getvalue(),
    ))

    # Mutasi RP12 - buang penempelannya: pemeriksaan di atas harus gagal.
    mut12 = original.replace('    text = text + "\\n" + teks_serah', '    text = text  # MUTASI RP12')
    assert mut12 != original, "mutasi RP12 tidak mengubah apa pun - uji tidak valid"
    rp_path.write_text(mut12, encoding="utf-8")
    rp_m12 = _load_review_prompt(cp, "review_prompt_mut_rp12")
    out12b = base_dir / "rp12_prompt_mut.md"
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        rp_m12.main(["--generic", "--out", str(out12b)])
    teks12b = out12b.read_text(encoding="utf-8") if out12b.is_file() else ""
    serah12c = rp.handoff_block(None, SHA_UJI, "/tmp/rp12_audit.md", slug=SLUG_UJI, objek="_meta",
                                jenis="pemeriksaan menyeluruh independen (audit isi)")
    checks.append((
        "RP12 varian AUDIT ISI: objek + permalink tree + kanal --terbaru tercetak (aturan pemilik "
        "mencakup pemeriksaan menyeluruh, bukan hanya review)",
        "`_meta`" in serah12c and f"/tree/{SHA_UJI}/_meta" in serah12c
        and "ambil_verdict.py --terbaru" in serah12c
        and "audit_prompt.py --objek _meta" in serah12c
        and "pemeriksaan menyeluruh independen (audit isi)" in serah12c
        and "sha pin di dalam prompt == sha HEAD dari git" in serah12c
        and "sha head PR dari API" not in serah12c,
    ))
    checks.append((
        "RP12 diuji-mutasi: penempelan blok serah terima dibuang -> terdeteksi",
        "BLOK SERAH TERIMA" not in teks12b,
    ))
    rp_path.write_text(original, encoding="utf-8")

    # ------------------------------------------------------------------
    # RP13 - link ke BERKAS PROMPT ITU SENDIRI (T-48, koreksi pemilik giliran 20): prompt ditempel ke
    # kanal PR sebagai KOMENTAR PENULIS dan permalink-nya dicetak. Risiko nyatanya: prompt memuat
    # contoh judul verdict yang SENGAJA tidak dipagari (supaya hakim bisa menyalinnya), jadi kalau
    # komentar pengumuman ini terbaca sebagai slot hakim, kuorum jadi palsu - persis cacat D-3 yang
    # sudah ditutup. Karena itu yang diuji LINTAS ALAT: badan komentarnya dimasukkan ke
    # `slot_hakim()` milik `ambil_verdict.py` dan harus BUKAN slot.
    # ------------------------------------------------------------------
    import importlib.util as _iu
    _spec_av = _iu.spec_from_file_location("av_rp13", cp / "tools" / "ambil_verdict.py")
    av13 = _iu.module_from_spec(_spec_av)
    _spec_av.loader.exec_module(av13)

    prompt13 = p_rp10 + "\n```bash\ngh api repos/x\n```\n"      # memuat pagar 3-backtick di dalamnya
    badan13 = rp.bangun_komentar_pengumuman(prompt13, 74, SHA_UJI, "/tmp/rp13.md")
    # Catatan: prompt di dalamnya memuat baris penutup pagar 3-backtick yang juga "murni backtick",
    # jadi yang dibandingkan adalah PAGAR TERLUAR (yang terpanjang) terhadap run terpanjang di dalam
    # prompt, dan pagar terluar itu harus muncul persis dua kali (buka + tutup).
    panjang13 = [len(x.strip()) for x in badan13.split("\n")
                 if x.strip() and set(x.strip()) <= {"`"}]
    terdalam13 = max((len(r) for r in re.findall(r"`+", prompt13)), default=0)
    checks.append((
        "RP13 komentar pengumuman: judul menyebut penulis + BUKAN verdict, prompt dipagari pagar "
        "terluar yang LEBIH PANJANG dari run terpanjang di dalam prompt (muncul tepat 2x), dan "
        "isinya utuh di dalam pagar",
        badan13.splitlines()[0].startswith("## Komentar penulis PR")
        and "BUKAN verdict" in badan13.splitlines()[0]
        and panjang13 and max(panjang13) >= 4
        and max(panjang13) > terdalam13
        and panjang13.count(max(panjang13)) == 2
        and prompt13.rstrip("\n") in badan13,
    ))
    checks.append((
        "RP13 LINTAS ALAT: komentar pengumuman BUKAN slot hakim menurut ambil_verdict.slot_hakim()",
        av13.slot_hakim(badan13) is False,
    ))

    # Mutasi RP13 - buang label `penulis` dari judul: komentar harus TERBACA sebagai slot hakim.
    # Kalau mutasi ini tidak mengubah kesimpulan, pengaman pertama hanyalah hiasan.
    badan13_mut = badan13.replace("## Komentar penulis PR — BUKAN verdict: prompt review independen "
                                  "siap salin",
                                  "## Prompt review independen PR #74 — putaran 3 (siap salin)", 1)
    assert badan13_mut != badan13, "mutasi RP13 tidak mengubah apa pun - uji tidak valid"
    checks.append((
        "RP13 diuji-mutasi: label penulis dibuang dari judul -> TERBACA sebagai slot hakim "
        "(bukti pengamannya nyata, bukan hiasan)",
        av13.slot_hakim(badan13_mut) is True,
    ))

    # Fail-closed: slug tak terbaca -> tidak menempel dan tidak mencetak link karangan.
    url13, cat13 = rp.umumkan_prompt(74, prompt13, slug="<OWNER>/<REPO>")
    checks.append((
        "RP13 fail-closed: slug repo tak terbaca -> tidak ada permalink dan alasannya dinyatakan",
        url13 is None and "slug repo tidak terbaca" in cat13,
    ))

    # ------------------------------------------------------------------
    # RP14 - putaran yang SEDANG BERJALAN tidak boleh dinamai sebagai putaran berikutnya (temuan #2
    # hakim putaran 3 PR #74, P1). Cacat nyatanya terukur: begitu SATU hakim putaran 3 menempel
    # verdictnya, `review_prompt.py --pr 74` pada head yang sama mencetak "putaran 4" tiga kali,
    # padahal pemilik membuka putaran 3 dan dua hakim lain masih bekerja di bawah teks "putaran 3".
    # ------------------------------------------------------------------
    H_UJI = "f683db8" + "0" * 33

    def _verd(r, head=None):
        t = f"## Review independen PR #74 — putaran {r} — VERDICT: MERAH\n"
        if head:
            t += f"\nHead yang diputuskan: `{head}`\n"
        return {"body": t}

    kanal_1dari3 = {"comments": [_verd(1), _verd(2), _verd(2), _verd(2), _verd(3, H_UJI)], "reviews": []}
    kanal_3dari3 = {"comments": [_verd(1), _verd(2), _verd(2), _verd(2),
                                 _verd(3, H_UJI), _verd(3, H_UJI), _verd(3, H_UJI)], "reviews": []}
    checks.append((
        "RP14a kuorum putaran belum lengkap (1 dari 3) -> prompt menamai putaran yang berjalan, bukan +1",
        rp.hitung_putaran(kanal_1dari3, 3, H_UJI) == 3,
    ))
    checks.append((
        "RP14b kuorum lengkap TAPI head belum bergerak sejak verdict -> tetap putaran yang berjalan",
        rp.hitung_putaran(kanal_3dari3, 3, H_UJI) == 3,
    ))
    checks.append((
        "RP14c kuorum lengkap DAN head sudah bergerak (koreksi masuk) -> putaran berikutnya",
        rp.hitung_putaran(kanal_3dari3, 3, "9" * 40) == 4,
    ))
    checks.append((
        "RP14d kuorum yang lebih besar dihormati (5 hakim, baru 3 masuk) -> masih putaran berjalan",
        rp.hitung_putaran(kanal_3dari3, 5, "9" * 40) == 3,
    ))
    checks.append((
        "RP14e komentar penulis yang menyebut 'putaran 9' tidak dihitung sebagai slot -> putaran 1",
        rp.hitung_putaran({"comments": [{"body": "## Tanggapan penulis atas verdict putaran 9\n"}],
                           "reviews": []}, 3, H_UJI) == 1,
    ))

    # ------------------------------------------------------------------
    # RP15 - urutan baca wajib memuat SETIAP berkas yang berubah (temuan #6 hakim putaran 3).
    # Terukur pada PR ini: 58 dari 60 berkas masuk daftar; yang jatuh persis dua berkas non-Markdown
    # di luar tools/ - `_meta/_internal/uji/uji_upscaling.py` dan
    # `sistem/sistem-undangan/_sistem/validate_system.py`.
    # ------------------------------------------------------------------
    files15 = ["_meta/00_CARA_KERJA_META.md", "_meta/_internal/uji/uji_upscaling.py",
               "sistem/sistem-undangan/_sistem/validate_system.py", "data/konfig.json", "CATATAN.md"]
    order15 = "\n".join(rp.reading_order(files15))
    checks.append((
        "RP15a setiap berkas yang berubah masuk urutan baca (non-Markdown di luar tools/ tidak jatuh)",
        all(f in order15 for f in files15),
    ))
    checks.append((
        "RP15b tidak ada berkas ganda dan urutan tetap diawali pegangan wajib",
        order15.count("`CATATAN.md`") == 1 and order15.count("uji_upscaling.py") == 1
        and rp.reading_order(files15)[0].startswith("`LOG_SESI_"),
    ))
    # Mutasi RP15: buang cabang catch-all -> dua berkas non-Markdown di luar tools/ harus JATUH.
    mut15 = original.replace(
        '''        else:
            # Temuan hakim putaran 3 PR #74 (#6): semua cabang di atas hanya menerima `*.md` (plus apa''',
        '''        elif False:
            # Temuan hakim putaran 3 PR #74 (#6): semua cabang di atas hanya menerima `*.md` (plus apa''')
    assert mut15 != original, "mutasi RP15 tidak mengubah apa pun - uji tidak valid"
    rp_path.write_text(mut15, encoding="utf-8")
    rp_mut15 = _load_review_prompt(cp, "review_prompt_mut_rp15")
    order15_mut = "\n".join(rp_mut15.reading_order(files15))
    checks.append((
        "RP15c diuji-mutasi: cabang catch-all dibuang -> berkas non-Markdown di luar tools/ jatuh",
        "uji_upscaling.py" not in order15_mut and "validate_system.py" not in order15_mut,
    ))
    rp_path.write_text(original, encoding="utf-8")

    # ------------------------------------------------------------------
    # RP16 - ujung base: nilai BEKU dari API tidak boleh dilabeli "SEKARANG" (temuan #7 hakim
    # putaran 3). Terukur: main bergerak ke 26147e1 (PR lain merge 13:35Z) sementara `.base.sha`
    # PR #74 tetap c1d00c3, dan prompt menulis "hanya di (B): 0 berkas" padahal selisih terhadap
    # ujung main yang sebenarnya memuat 11 berkas tambahan.
    # ------------------------------------------------------------------
    t16a, p16a = rp.baris_ujung_base("c1d00c3" + "0" * 33, {
        "sha": "26147e1" + "0" * 33, "waktu_utc": "2026-09-18T14:00:00Z",
        "sumber": "git ls-remote origin refs/heads/main", "kesalahan": []})
    checks.append((
        "RP16a base bergerak -> dinyatakan BERGERAK + waktu ukur, dan base PR dilabeli BEKU (bukan SEKARANG)",
        any("BASE SUDAH BERGERAK" in x for x in p16a)
        and any("BEKU sejak PR dibuat" in x for x in t16a)
        and any("2026-09-18T14:00:00Z" in x for x in t16a)
        and not any("SEKARANG" in x for x in t16a),
    ))
    t16b, p16b = rp.baris_ujung_base(SHA_UJI, {
        "sha": SHA_UJI, "waktu_utc": "2026-09-18T14:00:00Z", "sumber": "git ls-remote", "kesalahan": []})
    checks.append((
        "RP16b base tidak bergerak -> dinyatakan sama DAN tetap menyuruh ukur ulang sebelum menyimpulkan",
        any("sama" in x for x in p16b) and not any("BASE SUDAH BERGERAK" in x for x in p16b)
        and any("ukur ulang" in x for x in p16b),
    ))
    t16c, p16c = rp.baris_ujung_base(SHA_UJI, {
        "sha": None, "waktu_utc": None, "sumber": None, "kesalahan": ["ujung branch tidak terbaca"]})
    checks.append((
        "RP16c ujung base tak terukur -> TIDAK TERUKUR dinyatakan + perintah ukur (fail-closed, tak disamakan)",
        any("TIDAK TERUKUR" in x for x in t16c) and any("git ls-remote" in x for x in p16c)
        and not any("sama" in x for x in p16c),
    ))

    # ------------------------------------------------------------------
    # RP17 - teks gerbang tidak boleh menjanjikan hal yang tidak terukur (temuan #1 KEDUA hakim
    # putaran 4 PR #74). Prompt mewajibkan `validate_repo.py` "harus PASS, 0 warning", padahal PR
    # ini sendiri yang menambahkan warning tier (keputusan pemilik 18 Sep 2026): di head 8305eeb
    # alat mencetak "WARNINGS: 2" dari dua baris berkas bukti historis, dan di merge-base
    # "WARNINGS: none". Gerbang yang tak bisa dipenuhi itu membuat review MERAH tanpa cacat baru.
    # Sebelumnya TIDAK ADA regresi yang memaku teks gerbang -> ia basi diam-diam.
    # ------------------------------------------------------------------
    out17 = base_dir / "rp17_prompt.md"
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        rp.main(["--generic", "--out", str(out17)])
    teks17 = out17.read_text(encoding="utf-8") if out17.is_file() else ""
    checks.append((
        "RP17a gerbang validator di prompt TIDAK menjanjikan '0 warning' dan menyatakan aturan warning tier",
        "0 warning" not in teks17 and "WARNINGS: N" in teks17
        and "berkas bukti historis" in teks17 and "harus PASS" in teks17
        and "Warning di dokumen HIDUP" in teks17,
    ))
    dod17 = (cp / "_meta" / "DEFINITION_OF_DONE.md").read_text(encoding="utf-8")
    cara17 = (cp / "_meta" / "00_CARA_KERJA_META.md").read_text(encoding="utf-8")
    checks.append((
        "RP17b dokumen hidup ikut selaras: DoD + cara kerja meta tidak menjanjikan '0 warning'",
        "PASS dengan 0 warning" not in dod17 and "harus PASS 0 warning" not in cara17
        and "Warning tier hanya sah untuk berkas bukti historis" in dod17
        and "warning hanya sah di berkas bukti historis" in cara17,
    ))
    # Mutasi RP17: kembalikan teks gerbang lama -> RP17a harus gagal (kontrol positif).
    mut17 = original.replace(
        """    a("python3 tools/validate_repo.py          # harus PASS; baris 'WARNINGS: N' dikutip apa adanya")""",
        """    a("python3 tools/validate_repo.py          # harus PASS, 0 warning")""")
    assert mut17 != original, "mutasi RP17 tidak mengubah apa pun - uji tidak valid"
    assert "0 warning" in mut17, "mutasi RP17 tidak menghasilkan teks lama - uji tidak valid"
    rp_path.write_text(mut17, encoding="utf-8")
    rp_m17 = _load_review_prompt(cp, "review_prompt_mut_rp17")
    out17b = base_dir / "rp17_prompt_mut.md"
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        rp_m17.main(["--generic", "--out", str(out17b)])
    teks17b = out17b.read_text(encoding="utf-8") if out17b.is_file() else ""
    checks.append((
        "RP17c diuji-mutasi: teks gerbang dikembalikan ke '0 warning' -> janji tak terukur itu terdeteksi",
        "0 warning" in teks17b and "WARNINGS: N" not in teks17b,
    ))
    rp_path.write_text(original, encoding="utf-8")

    # ------------------------------------------------------------------
    # RP18 - blok serah terima tidak boleh mencetak pernyataan palsu (temuan #1 hakim C putaran 5
    # PR #74). `else` di handoff_block() terikat ke `if permalink:` bukan ke `if out_path:`, jadi
    # alat yang DIPANGGIL DENGAN --out tetap mencetak "berkas TIDAK ditulis" padahal berkasnya
    # ditulis (terukur: review_prompt 25.714 byte, audit_prompt 17.256 byte, dua kalimat
    # bertentangan di berkas yang sama). Cacat ini ada di ALAT PENGADIL dan tepat di blok yang
    # menjalankan aturan tetap pemilik (serahkan path + link). Perbaikan: else diikat ke out_path,
    # dan klaim keberadaan berkas DIUKUR sesudah penulisan lalu ditempel ke berkas itu sendiri.
    # ------------------------------------------------------------------
    out18 = base_dir / "rp18_prompt.md"
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        rc18 = rp.main(["--generic", "--out", str(out18)])
    teks18 = out18.read_text(encoding="utf-8") if out18.is_file() else ""
    checks.append((
        "RP18a dengan --out: berkas ditulis DAN tidak ada klaim palsu 'berkas TIDAK ditulis'",
        rc18 == 0 and out18.is_file() and "TIDAK ditulis ke berkas" not in teks18
        and "path absolut — salin persis" in teks18,
    ))
    checks.append((
        "RP18b keberadaan berkas DIUKUR sesudah ditulis (baris verifikasi ada di dalam berkasnya)",
        "Verifikasi sesudah ditulis (diukur, bukan diklaim)" in teks18 and "byte" in teks18,
    ))
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        serah18c = rp.handoff_block(None, SHA_UJI, None)
    checks.append((
        "RP18c tanpa --out: cabang jujur TETAP ada (tidak ditulis ke berkas + suruhan --out)",
        "TIDAK ditulis ke berkas" in serah18c and "--out <path>" in serah18c,
    ))
    serah18d = rp.handoff_block(None, SHA_UJI, str(base_dir / "rp18_belum_ada.md"))
    checks.append((
        "RP18d out_path yang BELUM ada di disk -> tidak mengklaim ADA (fail-closed, bukan karangan)",
        "ADA di disk," not in serah18d and "diukur SESUDAH alat menulisnya" in serah18d,
    ))
    ap18 = base_dir / "rp18_audit.md"
    r18e = subprocess.run(
        # salinan uji tidak memuat .git, jadi sha HEAD di-pin manual (jalur yang ditawarkan alat
        # sendiri waktu git tidak terbaca) — tanpa ini alat keluar rc=2 dan RP18e gagal palsu.
        [sys.executable, "-B", "tools/audit_prompt.py", "--objek", "_meta", "--pin", SHA_UJI,
         "--out", str(ap18)],
        cwd=str(cp), capture_output=True, text=True,
        env={**os.environ, "FI_SKIP_NESTED": "1", "PYTHONDONTWRITEBYTECODE": "1"})
    teks18e = ap18.read_text(encoding="utf-8") if ap18.is_file() else ""
    checks.append((
        "RP18e audit_prompt.py --out (peminjam handoff_block): berkas ada, tanpa klaim palsu, terverifikasi",
        r18e.returncode == 0 and ap18.is_file() and "TIDAK ditulis ke berkas" not in teks18e
        and "path absolut — salin persis" in teks18e and "Verifikasi sesudah ditulis" in teks18e,
    ))
    # Mutasi RP18: kembalikan `else` ke ikatan lama (ke `if permalink:`) -> RP18a harus menangkapnya.
    mut18 = original.replace(
        """    else:
        a("- **Berkas prompt:** TIDAK ditulis ke berkas (keluar ke stdout). Jalankan ulang dengan")
        a("  `--out <path>` supaya ada berkas yang bisa diberi path dan link.")
    if permalink:
        a(f"- **LINK KE PROMPT INI (tahan lama, bisa dibuka siapa pun):** {permalink}")
        a("  Komentar **penulis PR**, BUKAN verdict: alat pengumpul verdict menggolongkannya"
          " sebagai komentar penulis dan isinya dipagari, jadi contoh judul verdict di dalamnya"
          " tidak bisa terbaca. Ini link yang diserahkan ke pemilik dan ke siapa pun yang"
          " membuka sesi hakim — path di atas hanya ada di mesin kerja agent.")""",
        """    if permalink:
        a(f"- **LINK KE PROMPT INI (tahan lama, bisa dibuka siapa pun):** {permalink}")
        a("  Komentar **penulis PR**, BUKAN verdict: alat pengumpul verdict menggolongkannya"
          " sebagai komentar penulis dan isinya dipagari, jadi contoh judul verdict di dalamnya"
          " tidak bisa terbaca. Ini link yang diserahkan ke pemilik dan ke siapa pun yang"
          " membuka sesi hakim — path di atas hanya ada di mesin kerja agent.")
    else:
        a("- **Berkas prompt:** TIDAK ditulis ke berkas (keluar ke stdout). Jalankan ulang dengan")
        a("  `--out <path>` supaya ada berkas yang bisa diberi path dan link.")""")
    assert mut18 != original, "mutasi RP18 tidak mengubah apa pun - uji tidak valid"
    assert mut18.count("TIDAK ditulis ke berkas") == original.count("TIDAK ditulis ke berkas"), \
        "mutasi RP18 mengubah jumlah kalimat, bukan ikatan else - uji tidak valid"
    rp_path.write_text(mut18, encoding="utf-8")
    rp_m18 = _load_review_prompt(cp, "review_prompt_mut_rp18")
    out18m = base_dir / "rp18_prompt_mut.md"
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        rp_m18.main(["--generic", "--out", str(out18m)])
    teks18m = out18m.read_text(encoding="utf-8") if out18m.is_file() else ""
    checks.append((
        "RP18f diuji-mutasi: else dikembalikan ke if permalink -> klaim palsu itu TERDETEKSI",
        out18m.is_file() and "TIDAK ditulis ke berkas" in teks18m
        and "path absolut — salin persis" in teks18m,
    ))
    rp_path.write_text(original, encoding="utf-8")

    # ------------------------------------------------------------------
    # RP19 - penjaga yang tidak menjaga lebih berbahaya daripada tidak ada penjaga (temuan #1 hakim
    # A dan C putaran 5): RP17b hanya mencari DUA frasa ("PASS dengan 0 warning" di DoD, "harus PASS
    # 0 warning" di cara kerja meta) sehingga frasa yang benar-benar hidup di peta struktur -
    # "PASS wajib 0-warning" - lolos: FI hijau padahal cacat yang diklaim sudah ditutup masih ada,
    # dan T-50 sempat ditandai SELESAI atas dasar penjaga buta itu. RP19 memindai POLA di daftar
    # dokumen normatif hidup, dan daftarnya fail-closed (tidak boleh menyusut diam-diam - pelajaran
    # dari CORE_REQUIRED). Dokumen riwayat/ujian (log sesi, ACCEPTANCE_TEST_LOG, dokumen FI, register,
    # INDEKS) SENGAJA di luar cakupan: di sana frasa lama sah dikutip sebagai riwayat, dan keputusan
    # pemilik 18 Sep 2026 memang melindungi berkas bukti historis append-only.
    # ------------------------------------------------------------------
    pola19 = re.compile(r"(0\s*[-\u2013]?\s*warning|nol\s+warning|WARNINGS?\s*:\s*none|"
                        r"0\s+peringatan|tanpa\s+warning)", re.I)
    dok19 = ["_meta/00_CARA_KERJA_META.md", "_meta/DEFINITION_OF_DONE.md",
             "_meta/PROTOKOL_REVIEW_INDEPENDEN.md", "_meta/PROTOKOL_AUDIT_ISI.md",
             "_meta/NEXT_SESSION_PROMPT.md", "_meta/03_KONTRAK_WARISAN.md",
             "_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md", "_meta/PANDUAN_PENGGUNA_TEMPLATE.md",
             "PANDUAN_PENGGUNA.md", "PROMPT_ENTRI_UNIVERSAL.md"]
    hilang19 = [d for d in dok19 if not (cp / d).is_file()]
    hit19 = []
    for d19 in dok19:
        f19 = cp / d19
        if f19.is_file():
            t19 = f19.read_text(encoding="utf-8")
            hit19 += [f"{d19}:{t19[:m.start()].count(chr(10)) + 1}" for m in pola19.finditer(t19)]
    checks.append((
        "RP19a daftar dokumen normatif hidup fail-closed: tidak ada yang hilang/diganti nama diam-diam",
        not hilang19,
    ))
    checks.append((
        "RP19b tidak ada janji gerbang berpola 'nol warning' di dokumen normatif hidup",
        not hit19,
    ))
    f19m = cp / "_meta" / "00_CARA_KERJA_META.md"
    asli19 = f19m.read_text(encoding="utf-8")
    f19m.write_text(asli19.replace("Regresi struktural tersedia sebagai alat",
                                   "Validator harus PASS dengan nol warning. "
                                   "Regresi struktural tersedia sebagai alat", 1),
                    encoding="utf-8")
    hit19m = [m.group(0) for m in pola19.finditer(f19m.read_text(encoding="utf-8"))]
    f19m.write_text(asli19, encoding="utf-8")
    checks.append((
        "RP19c diuji-mutasi: janji 'nol warning' disuntik ke dokumen hidup -> pola RP19 menangkapnya",
        bool(hit19m),
    ))

    # RP20 - penjaga field `- **Keadaan:**` di setiap log sesi (usulan hakim putaran 5 PR #74
    # temuan #6). Cacat yang lolos tanpa penjaga: header "Keadaan Sesi" LOG_SESI_2026-09-17.md
    # basi sejak 6f60c7c (menulis folder sistem-undangan "belum dibuat" padahal ada) dan log
    # lanjutan slot 24 tidak punya blok itu sama sekali; dua log lama malah memakai nilai di luar
    # OPEN/CLOSED ("menunggu gerbang ...") atau bentuk field lama (`- **Status:**`). RP20a
    # memastikan validator lulus di salinan DAN daftar lognya tidak kosong (fail-closed: penjaga
    # tidak boleh bisa dimatikan dengan memindahkan/mengosongkan folder log). RP20b kontrol
    # mutasi: field-nya dicabut dari satu log -> validator WAJIB menolak, dan sesudah dipulihkan
    # validator lulus lagi (bukti kegagalan tadi disebabkan mutasinya, bukan hal lain).
    log20 = sorted((cp / "_log-sesi").glob("LOG_SESI_*.md"))
    checks.append((
        "RP20a validator PASS di salinan dan daftar LOG_SESI tidak kosong (penjaga field Keadaan aktif)",
        bool(log20) and run_tool(cp, "tools/validate_repo.py") == 0,
    ))
    f20 = log20[0]
    asli20 = f20.read_text(encoding="utf-8")
    f20.write_text("\n".join(g for g in asli20.split("\n")
                             if not g.startswith("- **Keadaan:**")) + "\n", encoding="utf-8")
    rc20 = run_tool(cp, "tools/validate_repo.py")
    f20.write_text(asli20, encoding="utf-8")
    checks.append((
        "RP20b diuji-mutasi: field `- **Keadaan:**` dicabut dari satu log -> validator MENOLAK, "
        "dipulihkan -> lulus lagi",
        rc20 != 0 and run_tool(cp, "tools/validate_repo.py") == 0,
    ))

    # RP21 - cacat susulan di blok serah terima, DITEMUKAN SENDIRI 19 Sep 2026 saat prompt putaran 6
    # PR #74 dibangkitkan ulang ke path yang sudah berisi berkas dari pembangkitan sebelumnya:
    # `handoff_block()` mencetak "Verifikasi berkas (diukur): ADA di disk, 27.678 byte" sementara
    # berkas hasil penulisan 27.598 byte - angka yang diserahkan adalah ukuran berkas LAMA yang lalu
    # ditimpa. Kelas cacatnya sama dengan temuan #1 hakim C putaran 5 (pernyataan palsu di blok yang
    # menjalankan aturan tetap pemilik "serahkan path + link"), dan RP18 buta terhadapnya karena
    # RP18d hanya menguji path yang BELUM ada. Penjaga yang tidak menjaga, ketiga kalinya di PR ini.
    out21 = base_dir / "rp21_prompt.md"
    sampah21 = "X" * 999_999                      # isi yang jelas bukan prompt, ukurannya khas
    out21.write_text(sampah21, encoding="utf-8")
    lama21 = out21.stat().st_size
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        rc21 = rp.main(["--generic", "--out", str(out21)])
    teks21 = out21.read_text(encoding="utf-8") if out21.is_file() else ""
    checks.append((
        "RP21a path tujuan SUDAH berisi berkas lama: ditimpa, dan blok serah terima tidak mengklaim "
        "ukuran yang diukur sebelum penulisan",
        rc21 == 0 and out21.is_file() and sampah21 not in teks21 and len(teks21) != lama21
        and "ADA di disk," not in teks21 and f"{lama21:,} byte" not in teks21
        and "diukur SESUDAH alat menulisnya" in teks21 and "Berkas lama akan DITIMPA" in teks21,
    ))
    # RP21b - invariant yang membuat klaim alat bisa diaudit siapa pun: angka di baris verifikasi
    # (diukur sesudah penulisan, sebelum baris itu sendiri ditempel) + panjang baris itu == ukuran
    # berkas di disk, dan jumlah barisnya tepat +1. Alat yang mengukur sebelum menulis memecah
    # invariant ini, jadi pemeriksa eksternal tidak perlu memercayai kata-katanya.
    baris21 = [g for g in teks21.split("\n") if g.startswith("- **Verifikasi sesudah ditulis")]
    ok21b = False
    if len(baris21) == 1:
        m21 = re.search(r"([\d,]+) byte / ([\d,]+) baris", baris21[0])
        if m21:
            klaim_byte = int(m21[1].replace(",", ""))
            klaim_baris = int(m21[2].replace(",", ""))
            ok21b = (out21.stat().st_size == klaim_byte + len((baris21[0] + "\n").encode("utf-8"))
                     and len(teks21.splitlines()) == klaim_baris + 1)
    checks.append((
        "RP21b invariant ukuran: angka baris verifikasi + panjang barisnya == ukuran berkas di disk, "
        "dan jumlah barisnya tepat +1",
        ok21b,
    ))
    # RP21c - kontrol mutasi: kembalikan cabang lama yang mengukur sebelum menulis. RP21a wajib
    # menangkapnya; kalau mutasi ini lolos, regresi di atas hanya hiasan.
    asli21 = rp_path.read_text(encoding="utf-8")
    mut21 = asli21.replace(
        """        a("- **Verifikasi berkas:** diukur SESUDAH alat menulisnya — baris verifikasi terukur")
        a("  ditambahkan alat ke akhir berkas. Blok ini dirangkai sebelum penulisan, jadi ia")
        a("  tidak boleh mendahului pengukuran; periksa dengan `ls -l` sesudah alat selesai.")
        if p.exists():
            a(f"- **Berkas lama akan DITIMPA:** `{p.name}` sudah ada di path itu sebelum penulisan,")""",
        """        if p.exists():
            a(f"- **Verifikasi berkas (diukur):** ADA di disk, {p.stat().st_size:,} byte.")
        else:
            a("- **Verifikasi berkas:** diukur SESUDAH alat menulisnya — baris verifikasi terukur")
            a("  ditambahkan alat ke akhir berkas. Blok ini dirangkai sebelum penulisan, jadi ia")
            a("  tidak boleh mendahului pengukuran; periksa dengan `ls -l` sesudah alat selesai.")
        if False:
            a(f"- **Berkas lama akan DITIMPA:** `{p.name}` sudah ada di path itu sebelum penulisan,")""")
    assert mut21 != asli21, "mutasi RP21 tidak mengubah apa pun - uji tidak valid"
    rp_path.write_text(mut21, encoding="utf-8")
    rp_m21 = _load_review_prompt(cp, "review_prompt_mut_rp21")
    out21m = base_dir / "rp21_prompt_mut.md"
    out21m.write_text(sampah21, encoding="utf-8")
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        rp_m21.main(["--generic", "--out", str(out21m)])
    teks21m = out21m.read_text(encoding="utf-8") if out21m.is_file() else ""
    checks.append((
        "RP21c diuji-mutasi: cabang pengukur-sebelum-menulis dikembalikan -> klaim ukuran berkas lama "
        "itu TERDETEKSI",
        "ADA di disk," in teks21m and f"{lama21:,} byte" in teks21m,
    ))
    rp_path.write_text(asli21, encoding="utf-8")

    # ------------------------------------------------------------------
    # RP22 - KESEGARAN header "Keadaan Sesi" (temuan #3 hakim putaran 6 PR #74 + temuan sapuan
    # penulis pada log OPEN yang lain). RP20 hanya memaku KEBERADAAN field `- **Keadaan:**`,
    # dan kelas cacat "header basi" lolos tiga kali: LOG_SESI_2026-09-17 menulis folder
    # sistem-undangan "belum dibuat" dan R-05 "belum dibangun" padahal keduanya ada; log slot 24
    # tidak punya blok Keadaan sama sekali; lalu header slot 24 BASI LAGI pada head 30b3cb2
    # (masih 63 commit / +12.737 / FI 169 / "body sepuluh kali" / "putaran 6 belum punya slot
    # hakim" sementara head terukur 66 / +12.951 / 172 / kesebelas / tiga verdict sudah masuk)
    # padahal dua commit terakhir hanya append kronologi. Penjaga baru menuntut satu baris
    # `- **Segar pada:** head `<sha7>` · <tanggal> · FI <N> · manifest v<X.Y.Z>` di setiap log
    # OPEN dan membandingkan tiap bagiannya dengan nilai hidup. Bagian utama SENGAJA tidak
    # bergantung git supaya bisa diuji di salinan tanpa `.git` (harness ini ignore ".git");
    # bagian sha (HEAD..HEAD~3) hanya jalan bila git tersedia.
    # ------------------------------------------------------------------
    log22 = sorted((cp / "_log-sesi").glob("LOG_SESI_*.md"))
    open22 = [f for f in log22
              if re.search(r"^- \*\*Keadaan:\*\*\s*`?OPEN`?", f.read_text(encoding="utf-8"), re.M)]
    checks.append((
        "RP22a kontrol positif: salinan punya log OPEN berbaris `- **Segar pada:**` dan validator "
        "LULUS - supaya empat uji mutasi di bawah bukan tautologi",
        bool(open22) and run_tool(cp, "tools/validate_repo.py") == 0,
    ))
    f22 = open22[0]
    asli22 = f22.read_text(encoding="utf-8")
    pola22 = (r"^- \*\*Segar pada:\*\* (\d{4}-\d{2}-\d{2}) \u00b7 FI (\d+) "
              r"\u00b7 manifest v(\d+\.\d+\.\d+) \u00b7 head terukur `([0-9a-f]{7,40})`\s*$")
    m22 = re.search(pola22, asli22, re.M)
    checks.append(("RP22a2 baris segar FORMAT BARU di log OPEN nyata terbaca oleh pola regresi (bukan "
                   "cuma oleh validator); format lama `head <sha> · <tanggal> · FI <N> · manifest v<X>` "
                   "ditolak karena memasangkan sha dengan angka yang tidak pernah benar pada sha itu",
                   bool(m22)))
    if m22 is None:
        # Fail-closed dan TERBACA: kalau barisnya tidak ada, keempat uji mutasi di bawah tidak bisa
        # dijalankan. Melanjutkan akan membuat `m22.group(0)` melempar AttributeError - regresi yang
        # crash alih-alih melaporkan kegagalan adalah penjaga yang lebih buruk daripada tidak ada,
        # jadi kegagalannya dinyatakan sebagai empat check yang gagal dengan alasannya.
        for tag22x in ("RP22b", "RP22c", "RP22d", "RP22e", "RP22f", "RP22g", "RP22h"):
            checks.append((
                f"{tag22x} TIDAK BISA DIUJI: tidak ada baris `- **Segar pada:**` format baru di blok "
                "header log OPEN pertama - migrasikan barisnya (bukan melonggarkan polanya)",
                False,
            ))
        return checks
    for tag22, ubah22, pesan22 in (
        ("RP22b", lambda t, m: "\n".join(g for g in t.split("\n")
                                          if not g.startswith("- **Segar pada:**")) + "\n",
         "baris `- **Segar pada:**` dicabut dari log OPEN"),
        ("RP22c", lambda t, m: t.replace(m.group(0), m.group(0).replace("FI " + m.group(2), "FI 1"), 1),
         "angka FI di baris segar dibuat tidak cocok dengan dokumen FI hidup (persis bentuk cacat "
         "yang lolos tiga kali: header menulis FI 169 ketika repo sudah 172)"),
        ("RP22d", lambda t, m: t.replace(m.group(0),
                                         m.group(0).replace("manifest v" + m.group(3), "manifest v0.0.1"), 1),
         "versi manifest di baris segar dibuat tidak cocok dengan manifest hidup"),
        ("RP22e", lambda t, m: t.replace(m.group(0), m.group(0).replace(m.group(1), "2020-01-01", 1), 1),
         "tanggal di baris segar dibuat lebih tua dari tanggal terbaru di log itu (kronologi append, "
         "header tidak disegarkan)"),
        # TIGA mutasi baru - temuan #1 hakim B putaran 7: penjaga yang mencari baris cap di SELURUH
        # berkas meluluskan log yang blok headernya tidak punya field itu, karena contoh di kronologi
        # atau di dalam pagar kode sudah cukup untuk membuatnya "ditemukan".
        ("RP22f", lambda t, m: _pindah_ke_kronologi(t, m),
         "baris cap DIPINDAH ke kronologi, di luar blok header 'Keadaan Sesi' - teksnya masih ada di "
         "berkas tetapi headernya tidak lagi punya keadaan terukur"),
        ("RP22g", lambda t, m: _duplikat_kontradiktif(t, m),
         "baris cap DIDUPLIKASI di blok header dengan angka FI berbeda - deklarasi ganda yang saling "
         "bertentangan tidak boleh lulus"),
        ("RP22h", lambda t, m: _bungkus_pagar_kode(t, m),
         "baris cap dibungkus PAGAR KODE di dalam blok header - contoh format bukan field keadaan"),
    ):
        f22.write_text(ubah22(asli22, m22), encoding="utf-8")
        rc22 = run_tool(cp, "tools/validate_repo.py")
        f22.write_text(asli22, encoding="utf-8")
        checks.append((
            f"{tag22} diuji-mutasi: {pesan22} -> validator MENOLAK, dipulihkan -> lulus lagi",
            rc22 != 0 and run_tool(cp, "tools/validate_repo.py") == 0,
        ))

    # ------------------------------------------------------------------
    # RP23 - bagian (e) penjaga kesegaran (sha cap vs HEAD..HEAD~3) DIUJI DENGAN `.git` NYATA.
    # Hakim C putaran 7 PR #74 menunjuk dua hal, keduanya direproduksi penulis sebelum diperbaiki:
    #   (1) RP22a–e dijalankan pada salinan TANPA `.git` (harness meng-copy dengan ignore ".git"),
    #       jadi bagian sha TIDAK PERNAH teruji - penjaga yang cabang utamanya tidak diuji, kelas
    #       yang sama dengan RP17b dan cabang buta RP18d/RP21 yang sudah diakui penulis;
    #   (2) penjaga itu membuat `main` VALIDATION FAILED SEKETIKA sesudah PR ini di-merge - pada
    #       squash merge MAUPUN merge commit, lalu permanen sesudah satu commit apa pun di atasnya -
    #       karena log OPEN milik sesi ini tidak bisa disegarkan oleh sesi lain (append-only +
    #       kepemilikan log). Penjaga saya sendiri memerahkan gerbang wajib repo untuk semua sesi.
    # Perbaikannya: bagian (b)(c)(e) hanya keras selama log "live" (disentuh salah satu dari 4 commit
    # terakhir); sha yang tidak dikenal di repo (clone dangkal / squash merge) menurunkan (e) menjadi
    # warning beralasan. Empat skenario di bawah mengunci keduanya - gigi penjaga tetap ada, dan
    # commit sesi lain tidak lagi memerahkan gerbang.
    # ------------------------------------------------------------------
    git_ada = subprocess.run(["git", "--version"], capture_output=True, text=True).returncode == 0
    if not git_ada:
        checks.append((
            "RP23 TIDAK BISA DIUJI: git tidak tersedia di lingkungan ini - bagian (e) penjaga "
            "kesegaran tidak teruji. Fail-closed: dinyatakan GAGAL, bukan dilewati diam-diam",
            False,
        ))
        return checks

    def _g23(*a):
        return subprocess.run(["git"] + list(a), cwd=str(cp), capture_output=True, text=True)

    if not (cp / ".git").exists():
        for cmd in (("init", "-q"), ("config", "user.email", "fi@uji.lokal"),
                    ("config", "user.name", "Uji FI"), ("add", "-A"),
                    ("commit", "-qm", "FI: pohon awal untuk menguji bagian (e) penjaga kesegaran")):
            _g23(*cmd)
    if not (cp / ".git").exists():
        checks.append(("RP23 TIDAK BISA DIUJI: `git init` di salinan gagal - bagian (e) tidak teruji "
                       "(fail-closed, dinyatakan GAGAL)", False))
        return checks

    def _cap23(sha):
        t = f22.read_text(encoding="utf-8")
        mm = re.search(pola22, t, re.M)
        baru = (f"- **Segar pada:** {mm.group(1)} · FI {mm.group(2)} · manifest v{mm.group(3)} "
                f"· head terukur `{sha}`")
        f22.write_text(t.replace(mm.group(0), baru, 1), encoding="utf-8")

    def _commit23(pesan, sentuh_log):
        if not sentuh_log:
            _g23("commit", "-q", "--allow-empty", "-m", pesan)
            return
        f22.write_text(f22.read_text(encoding="utf-8").rstrip("\n") + f"\n\n### {pesan}\n",
                       encoding="utf-8")
        _g23("add", str(f22.relative_to(cp)))
        _g23("commit", "-qm", pesan)

    rel23 = str(f22.relative_to(cp)).replace("\\", "/")
    _cap23(_g23("rev-parse", "--short=7", "HEAD").stdout.strip())
    _commit23("RP23: segarkan cap ke head terukur", True)
    rc_a, out_a = run_tool_out(cp, "tools/validate_repo.py")
    checks.append((
        "RP23a kontrol positif dengan .git NYATA: cap menunjuk head terukur dan log disentuh commit "
        "terbaru -> validator LULUS (supaya tiga skenario di bawah bukan tautologi)",
        rc_a == 0,
    ))
    for i in range(3):
        _commit23(f"RP23: append kronologi {i + 1} tanpa menyegarkan cap", True)
    rc_b, out_b = run_tool_out(cp, "tools/validate_repo.py")
    checks.append((
        "RP23b GIGI bagian (e) - sebelumnya tidak pernah teruji: tiga commit menyentuh log tanpa "
        "menyegarkan cap -> head terukur keluar dari jendela HEAD..HEAD~3 sementara log tetap live -> "
        "validator MENOLAK dan menyebut berkas log itu",
        rc_b != 0 and rel23 in out_b and "bukan HEAD maupun tiga commit" in out_b,
    ))
    for i in range(4):
        _commit23(f"RP23: commit asing sesi lain {i + 1}", False)
    rc_c, out_c = run_tool_out(cp, "tools/validate_repo.py")
    checks.append((
        "RP23c sebab MERAH putaran 7 disembuhkan: empat commit yang TIDAK menyentuh log (commit sesi "
        "lain di atas merge) -> log tidak lagi live -> bagian (b)(c)(e) DITURUNKAN menjadi warning "
        "beralasan dan validator LULUS - gerbang wajib repo tidak lagi merah untuk sesi lain",
        rc_c == 0 and "WARNING kesegaran header" in out_c
        and "tidak disentuh oleh 4 commit terakhir" in out_c,
    ))
    _cap23("deadbeef")
    _commit23("RP23: cap memakai sha yang tidak dikenal (simulasi squash merge)", True)
    rc_d, out_d = run_tool_out(cp, "tools/validate_repo.py")
    checks.append((
        "RP23d sha cap yang TIDAK DIKENAL di repo ini (clone dangkal, atau riwayat branch yang dibuang) "
        "-> bagian (e) DITURUNKAN menjadi warning beralasan dan validator LULUS - bukan FAILED, bukan "
        "mati senyap",
        rc_d == 0 and "tidak dikenal di repo ini" in out_d,
    ))
    # RP23e/f - C8 diuji pada bentuk akhirnya: KEDUA cara merge yang ditawarkan GitHub tidak boleh
    # memerahkan gerbang wajib di pohon hasil merge. Ini yang diukur hakim C dan yang saya reproduksi
    # sendiri di clone terpisah pada `main` terbaru. Versi pertama perbaikan (hanya live-scoping) BELUM
    # menyembuhkan: squash merge dan merge commit masih VALIDATION FAILED sampai ada empat commit asing
    # di atasnya, jadi klaim "sembuh" akan palsu kalau hanya RP23c yang menguncinya. Yang menyembuhkan
    # adalah dua jalur tambahan: cap yang bukan leluhur HEAD (ciri squash) dan merge commit di dalam
    # jendela - keduanya menurunkan bagian (e) menjadi warning beralasan.
    trunk23 = _g23("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    _g23("checkout", "-q", "-b", "uji-cabang-23")
    # Cap harus menunjuk commit yang HANYA ADA DI CABANG. Versi pertama uji ini mengisi cap dengan sha
    # HEAD saat cabang dibuat - sha itu ternyata nenek moyang bersama trunk dan cabang, jadi sesudah
    # `merge --squash` ia TETAP leluhur HEAD dan keadaan "bukan leluhur" tidak pernah terbentuk: ujinya
    # gagal karena skenarionya salah bangun, bukan karena penjaganya salah. Commit cabang pertama dibuat
    # lebih dulu, barulah cap diarahkan ke sana.
    _commit23("RP23e: commit pertama yang hanya ada di cabang", True)
    _cap23(_g23("rev-parse", "--short=7", "HEAD").stdout.strip())
    _commit23("RP23e: segarkan cap ke commit khusus cabang", True)
    # DELAPAN commit, bukan empat: sesudah merge, jendela `rev-list -n 4 HEAD` berisi campuran commit
    # batang utama dan commit cabang yang urutannya bergantung tanggal commit, jadi dengan empat commit
    # sha cap kadang MASIH masuk jendela dan warning yang diuji tidak pernah muncul - skenarionya tidak
    # deterministik. Versi pertama uji ini gagal persis karena itu, dan kegagalannya tampak sebagai
    # "perbaikannya tidak jalan" padahal yang rusak adalah ujinya.
    for i in range(8):
        _commit23(f"RP23e: pekerjaan cabang {i + 1} tanpa menyegarkan cap", True)
    cap23 = re.search(pola22, f22.read_text(encoding="utf-8"), re.M).group(4)
    _g23("checkout", "-q", trunk23)
    _commit23("RP23e: commit di batang utama", False)
    _g23("merge", "--no-ff", "-qm", "RP23e: merge cabang", "uji-cabang-23")

    def _prasyarat23(pesan_merge):
        """Pastikan keadaan yang mau diuji benar-benar terbentuk, supaya hasilnya bukan kebetulan.

        Tanpa ini, uji bisa 'lulus' karena validator memang tidak menemukan apa pun (sha cap kebetulan
        masih di dalam jendela) dan klaim "kedua cara merge sudah disembuhkan" jadi kosong."""
        jendela = _g23("rev-list", "-n", "4", "HEAD").stdout.split()
        terakhir = _g23("rev-list", "-n", "1", "HEAD", "--", rel23).stdout.split()
        if not jendela:
            return False, "jendela HEAD kosong"
        ada_merge = len(_g23("show", "--no-patch", "--format=%P", jendela[0]).stdout.split()) > 1
        syarat = {
            "log live (commit terakhir yang menyentuhnya ada di dalam jendela)":
                bool(terakhir) and terakhir[0] in jendela,
            "sha cap di luar jendela HEAD..HEAD~3":
                not any(s.startswith(cap23) for s in jendela),
            ("HEAD adalah merge commit" if pesan_merge else "sha cap bukan leluhur HEAD (squash)"):
                (ada_merge if pesan_merge
                 else _g23("merge-base", "--is-ancestor", cap23, "HEAD").returncode != 0),
        }
        return all(syarat.values()), "; ".join(k for k, v in syarat.items() if not v) or "lengkap"

    ok_e, alasan_e = _prasyarat23(True)
    rc_e, out_e = run_tool_out(cp, "tools/validate_repo.py")
    checks.append((
        "RP23e-prasyarat: sesudah MERGE COMMIT keadaan yang mau diuji benar-benar terbentuk (log live, "
        "sha cap di luar jendela, HEAD merge commit) - supaya uji di bawahnya bukan kebetulan",
        ok_e,
    ))
    checks.append((
        "RP23e MERGE COMMIT tidak memerahkan pohon hasil merge: log live dan cap-nya di luar jendela "
        "HEAD..HEAD~3, tetapi satu dari 4 commit terakhir adalah merge commit -> bagian (e) DITURUNKAN "
        "menjadi warning beralasan dan validator LULUS (aturan C8; versi pertama perbaikan masih FAILED "
        "di sini, terukur pada pohon yang sudah di-commit sebelum klaim apa pun dibuat)",
        ok_e and rc_e == 0 and "MERGE COMMIT - pohon ini baru menyerap" in out_e,
    ))
    _g23("reset", "-q", "--hard", "HEAD~1")
    _g23("merge", "--squash", "uji-cabang-23")
    _g23("commit", "-qm", "RP23f: squash merge cabang")
    ok_f, alasan_f = _prasyarat23(False)
    rc_f, out_f = run_tool_out(cp, "tools/validate_repo.py")
    checks.append((
        "RP23f-prasyarat: sesudah SQUASH MERGE keadaan yang mau diuji terbentuk (log live, sha cap di luar "
        "jendela, dan sha cap BUKAN leluhur HEAD karena riwayat cabang dibuang squash)",
        ok_f,
    ))
    checks.append((
        "RP23f SQUASH MERGE tidak memerahkan pohon hasil merge: cap dari branch yang digabung bukan "
        "leluhur HEAD -> bagian (e) DITURUNKAN menjadi warning beralasan dan validator LULUS (aturan C8)",
        ok_f and rc_f == 0 and "BUKAN leluhur HEAD" in out_f,
    ))
    # Selalu ditambahkan (bukan hanya saat gagal) supaya JUMLAH skenario tetap deterministik - kalau
    # hanya muncul saat gagal, angka yang dicetak alat berubah-ubah dan penjaga D-2 jadi tidak bisa
    # dipercaya. Nilainya ok_e AND ok_f, dan namanya membawa alasan persisnya bila ada yang tidak terbentuk.
    checks.append((
        f"RP23 catatan prasyarat (merge: {alasan_e} · squash: {alasan_f}) - kata 'lengkap' berarti keadaan "
        "yang mau diuji benar-benar terbentuk di repo uji, jadi RP23e dan RP23f di atas bukan kebetulan",
        ok_e and ok_f,
    ))
    f22.write_text(asli22, encoding="utf-8")

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

def _run_validator(repo: Path):
    """Jalankan validator pada salinan repo; kembalikan (kode keluar, gabungan keluaran)."""
    r = subprocess.run(
        [sys.executable, str(repo / "tools" / "validate_repo.py")],
        capture_output=True, text=True,
        env={**os.environ, "FI_SKIP_NESTED": "1"},
    )
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def table_integrity_scenarios(base_dir: Path):
    """TI1-TI5: regresi penjaga integritas tabel Markdown di `validate_repo.py` (T-47).

    Cacat nyatanya (18 Sep 2026): **14 baris tabel di 7 berkas** repo ini rusak — dua baris Log
    Evolusi manifest yatim di tengah prosa (masuk dari commit `1361f2f` dan `e78f59f`, yaitu
    pekerjaan agent ini sendiri), empat baris register "Sudah ditutup" terputus dari tabelnya oleh
    garis `---`, lima baris berpipa tak ter-escape di dalam sel, dua baris diputus baris kosong, dan
    satu baris kehilangan sel — dan **semuanya lolos** karena penjaga kolom versi lama hanya membaca
    2 berkas (register + ledger) sementara validator tetap mencetak PASS. Klaim "penjaga bergigi"
    yang tercatat sehari sebelumnya hanya benar untuk dua berkas itu.
    """
    checks = []
    cp = base_dir / "repo_ti"
    shutil.copytree(
        ROOT, cp,
        ignore=shutil.ignore_patterns(
            ".git", "backups", "template_clean", "template_clean.zip", "__pycache__", "dist"),
    )

    # TI1 - KONTROL POSITIF: pohon bersih harus LOLOS. Tanpa uji ini empat uji berikutnya bisa
    # "lolos" karena validatornya memang selalu gagal (tautologi) - pelajaran yang sudah tercatat.
    rc1, _out1 = _run_validator(cp)
    checks.append(("TI1 kontrol positif: pohon bersih -> validator PASS (bukan tautologi)", rc1 == 0))

    REG = cp / "_meta" / "DAFTAR_PEKERJAAN_TERBUKA.md"
    MAN = cp / "_meta" / "SYSTEM_MANIFEST.md"
    asli_reg = REG.read_text(encoding="utf-8")
    asli_man = MAN.read_text(encoding="utf-8")

    def _indeks(teks: str, awalan: str) -> int:
        for k, l in enumerate(teks.split("\n")):
            if l.strip().startswith(awalan):
                return k
        raise AssertionError(f"anchor tidak ditemukan: {awalan[:48]}")

    # TI2 - baris kosong disisipkan di tengah tabel: baris-baris sesudahnya jadi yatim.
    L = asli_reg.split("\n")
    L.insert(_indeks(asli_reg, "| T-40 |"), "")
    REG.write_text("\n".join(L), encoding="utf-8")
    rc2, out2 = _run_validator(cp)
    checks.append((
        "TI2 baris kosong memutus tabel register -> terdeteksi sebagai BARIS TABEL YATIM",
        rc2 != 0 and "BARIS TABEL YATIM" in out2,
    ))
    REG.write_text(asli_reg, encoding="utf-8")

    # TI3 - satu pipa pemisah sel dibuang: jumlah kolom tidak lagi cocok dengan header.
    L = asli_man.split("\n")
    i = _indeks(asli_man, "| 2026-09-18 | v1.24.0 →")
    L[i] = L[i].replace(" | ", " ", 1)
    MAN.write_text("\n".join(L), encoding="utf-8")
    rc3, out3 = _run_validator(cp)
    checks.append((
        "TI3 pipa pemisah sel dibuang di manifest -> terdeteksi sebagai kolom tidak cocok header",
        rc3 != 0 and "kolom padahal header tabelnya" in out3,
    ))
    MAN.write_text(asli_man, encoding="utf-8")

    # TI4 - baris tabel dipindah ke tengah prosa: bentuk cacat yang benar-benar terjadi dua kali.
    L = asli_man.split("\n")
    baris = L.pop(_indeks(asli_man, "| 2026-09-18 | v1.25.0 →"))
    L.insert(_indeks("\n".join(L), "- **Status:**"), baris)
    MAN.write_text("\n".join(L), encoding="utf-8")
    rc4, out4 = _run_validator(cp)
    checks.append((
        "TI4 baris tabel dipindah ke prosa -> terdeteksi sebagai BARIS TABEL YATIM",
        rc4 != 0 and "BARIS TABEL YATIM" in out4,
    ))
    MAN.write_text(asli_man, encoding="utf-8")

    # TI5 - pengecualian vendor: tabel rusak di dalam `skills/` TIDAK boleh menggagalkan validator.
    # Dokumen pihak ketiga disalin apa adanya; mengubahnya merusak provenance dan sinkronisasi hulu.
    vend = cp / "sistem" / "sistem-building-aplikasi" / "skills"
    assert vend.is_dir(), f"folder vendor untuk TI5 tidak ada: {vend}"
    (vend / "FI_RUSAK_SENGAJA.md").write_text(
        "# tabel rusak sengaja (uji TI5)\n\n| A | B |\n\n| C |\n", encoding="utf-8")
    rc5, out5 = _run_validator(cp)
    checks.append((
        "TI5 tabel rusak di folder vendor skills/ dikecualikan -> validator tetap PASS",
        rc5 == 0 and "FI_RUSAK_SENGAJA" not in out5,
    ))

    # TI6 - berkas BUKTI HISTORIS: cacat tabel jadi PERINGATAN, bukan kegagalan (keputusan pemilik
    # 18 Sep 2026, opsi A; menutup temuan yang dilaporkan KETIGA hakim putaran 3 PR #74). Dua aturan
    # saling mengunci: penjaga tabel mewajibkan pipa di dalam sel di-escape, append-only melarang
    # suntingan riwayat. Yang menang append-only - bukti yang boleh dirapikan bukan bukti lagi.
    BUKTI = cp / "sistem" / "sistem-konten-kreator" / "ACCEPTANCE_TEST_LOG.md"
    assert BUKTI.is_file(), f"berkas bukti historis untuk TI6 tidak ada: {BUKTI}"
    rc6, out6 = _run_validator(cp)
    asli_bukti = BUKTI.read_text(encoding="utf-8")
    BUKTI.write_text(asli_bukti.rstrip("\n") + "\n\n| A | B |\n\n| C |\n", encoding="utf-8")
    rc6b, out6b = _run_validator(cp)
    checks.append((
        "TI6 cacat tabel di berkas bukti historis -> PERINGATAN (validator tetap PASS, append-only menang)",
        rc6 == 0 and "berkas bukti historis" in out6
        and rc6b == 0 and "berkas bukti historis" in out6b and "BARIS TABEL YATIM" in out6b,
    ))
    BUKTI.write_text(asli_bukti, encoding="utf-8")

    # TI7 - pengecualian itu SEMPIT: cacat yang sama di dokumen hidup/normatif tetap KEGAGALAN.
    # Tanpa uji ini TI6 bisa dibaca sebagai "penjaga tabel dilonggarkan untuk semua berkas".
    HIDUP = cp / "_meta" / "FI_RUSAK_SENGAJA.md"
    HIDUP.write_text("# tabel rusak sengaja di dokumen hidup (uji TI7)\n\n"
                     "| A | B | C |\n|---|---|---|\n| D | E |\n", encoding="utf-8")
    rc7, out7 = _run_validator(cp)
    baris7 = [l for l in out7.splitlines() if "FI_RUSAK_SENGAJA" in l and "kolom padahal header" in l]
    checks.append((
        "TI7 cacat yang sama di dokumen HIDUP (bukan bukti historis) -> tetap KEGAGALAN tanpa awalan WARNING",
        rc7 != 0 and baris7 and not any("WARNING" in l for l in baris7),
    ))
    HIDUP.unlink()
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
            # Penjaga kesegaran header (RP22, v1.34.0) membandingkan versi manifest yang tertulis di
            # baris `- **Segar pada:**` setiap log OPEN dengan manifest HIDUP, jadi skenario yang
            # mengubah versi manifest HARUS ikut menyelaraskan baris itu di salinan. Kalau tidak,
            # kontrol positif ini gagal karena penjaga BARU, bukan karena penjaga drift Status/Versi
            # yang sedang diuji - dan uji yang gagal karena sebab lain tidak membuktikan apa pun.
            # Angka FI dan tanggal di baris itu TIDAK diubah: skenario ini tidak menyentuh dokumen FI
            # maupun kronologi log, jadi keduanya tetap selaras.
            if versi_line is not None:
                _v = re.search(r"`([^`]+)`\s*$", versi_line).group(1)
                for _lg in sorted((cp / "_log-sesi").glob("LOG_SESI_*.md")):
                    _t = _lg.read_text(encoding="utf-8")
                    if not re.search(r"^- \*\*Keadaan:\*\*\s*`?OPEN`?", _t, re.M):
                        continue
                    _lg.write_text(re.sub(
                        r"(^- \*\*Segar pada:\*\* \d{4}-\d{2}-\d{2} \u00b7 FI \d+ "
                        r"\u00b7 manifest v)\d+\.\d+\.\d+",
                        lambda mo: mo.group(1) + _v, _t, flags=re.M), encoding="utf-8")
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

    # D-2 sebagai fungsi murni: diuji langsung, karena cacat #1 hakim putaran 3 justru berupa
    # pembanding yang TIDAK PERNAH DIJALANKAN. Uji perilaku, bukan keberadaan teks.
    _doc_m = "**Jumlah:** 100 skenario di master (60 sintetis + 40 unit nyata)\n"
    _doc_e = ("**Jumlah:** 100 skenario di master (60 sintetis + 40 unit nyata) 25 di ekstrak template "
              "(24 sintetis + 1 unit nyata benih)\n")
    _doc_e_ganda = _doc_e + " 25 di ekstrak template (24 sintetis + 1 unit nyata benih)\n"
    _komp_m = [("sintetis", 60), ("unit nyata", 40)]
    _komp_e = [("sintetis", 24), ("unit nyata", 1)]
    checks.append((
        "D-2 murni: dokumen sinkron dengan cetakan alat -> tidak ada kegagalan (master dan ekstrak)",
        bandingkan_jumlah_dokumen(_doc_m, _komp_m, 100, False) == []
        and bandingkan_jumlah_dokumen(_doc_e, _komp_e, 25, True) == [],
    ))
    checks.append((
        "D-2 murni: total dokumen salah -> kegagalan yang menyebut angka dokumen DAN angka alat",
        len(bandingkan_jumlah_dokumen(_doc_m, _komp_m, 101, False)) == 1
        and "100" in bandingkan_jumlah_dokumen(_doc_m, _komp_m, 101, False)[0]
        and "101" in bandingkan_jumlah_dokumen(_doc_m, _komp_m, 101, False)[0],
    ))
    checks.append((
        "D-2 murni: mode EKSTRAK membaca baris ekstrak, dan angka ekstrak salah -> terdeteksi "
        "(cacat nyata: 16 di dokumen vs 25 cetakan, dulu tak terjangkau)",
        len(bandingkan_jumlah_dokumen(_doc_e, _komp_e, 16, True)) == 1
        and len(bandingkan_jumlah_dokumen(
            _doc_e.replace("25 di ekstrak template (24 sintetis", "16 di ekstrak template (15 sintetis"),
            [("sintetis", 15), ("unit nyata", 1)], 25, True)) == 1,
    ))
    checks.append((
        "D-2c murni: klaim ekstrak TERGANDA -> kegagalan (dua angka di satu dokumen bisa saling membantah)",
        any("D-2c" in g for g in bandingkan_jumlah_dokumen(_doc_e_ganda, _komp_e, 25, True))
        and not any("D-2c" in g for g in bandingkan_jumlah_dokumen(_doc_e, _komp_e, 25, True)),
    ))
    checks.append((
        "D-2 murni: baris jumlah hilang / komponen tak berlabel -> menolak menebak, bukan lolos diam-diam",
        any("tidak ditemukan" in g for g in bandingkan_jumlah_dokumen("tanpa baris jumlah\n", _komp_m, 1, False))
        and any("komponen tidak ditemukan" in g
                for g in bandingkan_jumlah_dokumen(_doc_m, [("sintetis", 60), ("label asing", 1)], 100, False)),
    ))
    # D-2d: severity selisih jumlah skenario. Kunci aturan baru `selisih_populasi_dari_garis_lain`
    # — DITURUNKAN jadi peringatan hanya bila kelebihannya datang dari garis riwayat lain (merge),
    # dan tetap KERAS bila unitnya ditambahkan sesudah dokumen diperbarui di garis yang sama.
    class _GitPalsu:
        def __init__(self, doc_commit, tambah, leluhur):
            self.doc_commit, self.tambah, self.leluhur = doc_commit, tambah, leluhur
            self.dipanggil = []

        def __call__(self, *a):
            self.dipanggil.append(a)
            class R:
                returncode = 0
                stdout = ""
            r = R()
            if "--diff-filter=A" in a:
                r.stdout = self.tambah.get(a[-1], "")
            elif a[0] == "log":
                r.stdout = self.doc_commit
            elif a[0] == "merge-base":
                r.returncode = 0 if (a[2], a[3]) in self.leluhur else 1
            return r

    _doc_d2d = "**Jumlah:** 190 skenario di master (30 sintetis + 19 unit nyata + 14 regresi review PR-11)\n"
    _komp_d2d = [("sintetis", 30), ("unit nyata", 20), ("regresi review PR-11", 14)]
    _unit_d2d = ["sistem/a/_produksi-aktif/unit-lama/STATUS.md", "sistem/b/_produksi-aktif/unit-baru/STATUS.md"]
    _boleh, _alasan = selisih_populasi_dari_garis_lain(
        _doc_d2d, _komp_d2d, 191, _unit_d2d,
        _GitPalsu("DOC1", {"sistem/a/_produksi-aktif/unit-lama/STATUS.md": "A0",
                           "sistem/b/_produksi-aktif/unit-baru/STATUS.md": "M9"}, set()), True)
    checks.append((
        "D-2d unit dari GARIS LAIN (commit penambahnya menyimpang dari commit dokumen, ciri pohon hasil "
        "merge) -> selisih D-2 DITURUNKAN jadi peringatan beralasan, gerbang FI tidak merah di `main` "
        "sesudah merge (aturan C8; diukur nyata pada merge PR #74 di atas main 98d3cb7)",
        _boleh is True and "garis lain" in _alasan,
    ))
    _boleh2, _alasan2 = selisih_populasi_dari_garis_lain(
        _doc_d2d, _komp_d2d, 191, _unit_d2d,
        _GitPalsu("DOC1", {"sistem/a/_produksi-aktif/unit-lama/STATUS.md": "A0",
                           "sistem/b/_produksi-aktif/unit-baru/STATUS.md": "N2"},
                  {("DOC1", "N2")}), True)
    checks.append((
        "D-2d GIGI tetap ada: unit yang ditambahkan SESUDAH dokumen diperbarui di garis riwayat yang sama "
        "(penulisnya bisa dan wajib menghitungnya) -> selisih TIDAK diturunkan, D-2 tetap gagal keras",
        _boleh2 is False and "SESUDAH dokumen" in _alasan2,
    ))
    _boleh3, _alasan3 = selisih_populasi_dari_garis_lain(
        "**Jumlah:** 190 skenario di master (29 sintetis + 20 unit nyata + 14 regresi review PR-11)\n",
        [("sintetis", 30), ("unit nyata", 20), ("regresi review PR-11", 14)], 191, _unit_d2d,
        _GitPalsu("DOC1", {}, set()), True)
    checks.append((
        "D-2d selisih yang menyentuh komponen LAIN (sintetis ikut beda) tidak boleh disembunyikan sebagai "
        "efek merge -> tetap keras",
        _boleh3 is False and "bukan kelebihan populasi unit" in _alasan3,
    ))
    _boleh4, _alasan4 = selisih_populasi_dari_garis_lain(
        _doc_d2d, [("sintetis", 30), ("unit nyata", 18), ("regresi review PR-11", 14)], 189, _unit_d2d,
        _GitPalsu("DOC1", {}, set()), True)
    checks.append((
        "D-2d populasi MENYUSUT (alat mencetak lebih sedikit dari dokumen — skenario hilang) tidak pernah "
        "diturunkan jadi peringatan -> tetap keras",
        _boleh4 is False and "menyusut" in _alasan4,
    ))
    _boleh5, _alasan5 = selisih_populasi_dari_garis_lain(_doc_d2d, _komp_d2d, 191, _unit_d2d,
                                                         _GitPalsu("DOC1", {}, set()), False)
    checks.append((
        "D-2d tanpa .git asal-usul unit tidak bisa ditentukan -> penjaga gagal keras (fail-closed), "
        "tidak menebak bahwa selisihnya efek merge",
        _boleh5 is False and "tidak ada .git" in _alasan5,
    ))

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

    # Run 22 adds two real production units at repository root.  They are
    # deliberately appended after the registered-system sweep: this is an
    # explicit acceptance-artifact population, not a new registered system.
    run22_units = [ROOT / rel for rel in RUN22_REAL_PRODUCTION_UNITS]
    # A clean extracted template has no repository-root production state and
    # must retain its historical one-unit population.  In the master repo,
    # seeing either Run 22 unit opts into checking both; a missing sibling is
    # then a real failure rather than a silent count drop.
    if any(unit.is_dir() for unit in run22_units):
        for unit in run22_units:
            real.append((unit / "STATUS.md", root_production_unit_is_safe(unit)))
        for status_path, safe in real[len(real) - len(run22_units):]:
            checks.append((f"real production unit consistent: {status_path.relative_to(ROOT)}", safe))

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

    # TI1–TI5 integritas tabel Markdown (skipped when nested, same reason).
    ti_checks = []
    if not os.environ.get("FI_SKIP_NESTED"):
        with TemporaryDirectory() as d:
            ti_checks = table_integrity_scenarios(Path(d))
    checks += ti_checks

    # --- D-2 (temuan R2 review PR #74): penjaga sinkron jumlah skenario vs dokumen ---
    # Sebelumnya angka di _meta/FAILURE_INJECTION_TESTS.md adalah SALINAN TANGAN, sehingga
    # menambah satu sistem terdaftar (yang menaikkan "unit nyata") membuat dokumen tertinggal
    # TANPA terdeteksi alat apa pun. Sekarang selisihnya adalah kegagalan, bukan catatan.
    # Mode DIDETEKSI DARI KEADAAN, bukan dari variabel lingkungan: di ekstrak template ketiga
    # grup regresi tidak dijalankan, jadi ketiganya kosong. Versi pertama penjaga ini hanya
    # membandingkan angka master (74) dan membuat smoke extract GAGAL karena di sana jumlahnya 16.
    _di_ekstrak = not (reg or sc_checks or rp_checks or ti_checks)
    # Penjaga D-2/D-2b/D-2c jalan TANPA SYARAT — juga di mode ekstrak. Versi sebelumnya membungkus
    # seluruh pembanding di dalam `if not FI_SKIP_NESTED`, padahal satu-satunya pemanggil yang
    # menjalankan ekstrak (build_template.smoke_extract) justru menyetel FI_SKIP_NESTED=1; jadi cabang
    # ekstrak tidak pernah terjangkau dan angka ekstrak di dokumen boleh salah tanpa satu pun alat
    # protes (temuan #1 hakim putaran 3 PR #74: dokumen 16, cetakan ekstrak 25). Yang dilewati di
    # ekstrak hanyalah PEMBANGKIT grup regresi (butuh salinan repo), bukan pembandingnya.
    doc = ROOT / "_meta" / "FAILURE_INJECTION_TESTS.md"
    if not doc.is_file():
        print("FAILURE-INJECTION TESTS FAILED")
        print(f"- D-2: dokumen inventaris tidak ditemukan: {doc}")
        raise SystemExit(1)
    # Parsing PER KOMPONEN BERNAMEKA, bukan "ambil semua angka": versi pertama penjaga ini memakai
    # re.findall(r"\d+") dan ikut menangkap angka 11 dari label "regresi review PR-11", sehingga
    # penjaganya sendiri melaporkan selisih palsu. Tertangkap oleh uji pertamanya.
    komponen = [("sintetis", n_synth), ("unit nyata", len(real))]
    if not _di_ekstrak:
        komponen += [("regresi review PR-11", len(reg)),
                     ("regresi check_selfcontained", len(sc_checks)),
                     ("regresi review_prompt", len(rp_checks)),
                     ("regresi integritas tabel", len(ti_checks))]
    _gagal_d2 = bandingkan_jumlah_dokumen(doc.read_text(encoding="utf-8"), komponen,
                                          len(checks), _di_ekstrak)
    _peringatan_d2 = []
    if _gagal_d2 and not _di_ekstrak:
        def _git_root(*a):
            return subprocess.run(["git"] + list(a), cwd=str(ROOT), capture_output=True, text=True)
        _boleh_turun, _alasan_turun = selisih_populasi_dari_garis_lain(
            doc.read_text(encoding="utf-8"), komponen, len(checks),
            [p.relative_to(ROOT).as_posix() for p, _s in real], _git_root, (ROOT / ".git").exists())
        if _boleh_turun:
            _peringatan_d2 = [
                "D-2 DITURUNKAN jadi peringatan (" + _alasan_turun + "): " + _gagal_d2[0] +
                " Angka di dokumen ditulis pada pohon yang tidak memuat unit dari garis riwayat lain itu, "
                "jadi tidak mungkin benar di sini; salin angka dari cetakan alat pada commit berikutnya "
                "di garis riwayat ini."]
            _gagal_d2 = []
    for _pw in _peringatan_d2:
        print("PERINGATAN " + _pw)
    if _gagal_d2:
        print("FAILURE-INJECTION TESTS FAILED")
        for _g in _gagal_d2:
            print(f"- {_g}")
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
          f" + {len(rp_checks)} regresi review_prompt"
          f" + {len(ti_checks)} regresi integritas tabel)")


if __name__ == "__main__":
    run()
