#!/usr/bin/env python3
"""Build clean template from master blueprint.

Satisfies AT-10 and SYSTEM_MANIFEST gate "Template bersih dirilis".
Template must NOT contain:
- personal data
- production output
- audit internal (_meta/_internal/)
- domain example decisions (sistem-konten-kreator content, pilot outputs)

Template MUST contain:
- entry point and minimal contract
"""
from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib
import os
import re
import shutil
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "_meta" / "_internal" / "template_clean"
TEMPLATE_ZIP = ROOT / "_meta" / "_internal" / "template_clean.zip"

# Files to include in clean template.
# M-01 (audit 5 Sep 2026): the list used to be static and silently drifted —
# files added to _meta/ after v1.0.0 (PANDUAN_PENGGUNA_TEMPLATE, TEMPLATE_LOG_SESI)
# were missing from the template. INCLUDE is now the STATIC CORE inventory
# (obligation, checkpoint_core) UNION the derived repository glob: a new file
# ships automatically, and a deleted core file makes the build FAIL instead
# of silently disappearing (review finding F1).
import checkpoint_core as core

ROOT_META_EXCLUDE = ()  # no _meta file is excluded; empty = fail-loud default

def include_list():
    items = sorted(
        set(core.CORE_META_FILES)
        | {f"_meta/{p.name}" for p in (ROOT / "_meta").glob("*.md")}
    )
    items += [
        "PANDUAN_PENGGUNA.md",
        "PROMPT_ENTRI_UNIVERSAL.md",
        ".gitignore",
        ".gitattributes",
    ]
    items += sorted(
        set(core.CORE_TOOL_FILES)
        | {f"tools/{p.name}" for p in (ROOT / "tools").glob("*.py")}
    )
    return items

# Additional empty dirs to create
EMPTY_DIRS = [
    "_pegangan-kamu",
    "_cadangan-claude",
]

MANIFEST_BANNER = (
    "<!-- BANNER DITAMBAHKAN OLEH build_template.py (M-16, audit 5 Sep 2026):\n"
    "     Salinan dari master blueprint. Di repo HASIL-EKSTRAKSI ini, isi di bawah\n"
    "     adalah SEJARAH master, BUKAN manifest repo ini — manifest sistem-domain\n"
    "     repo baru dibuat dari _meta/SYSTEM_MANIFEST_TEMPLATE.md mulai versi 0.1.0.\n"
    "     Untuk meta-sistem repo ini sendiri, catat versi release di INDEKS. -->\n"
)


def current_meta_version() -> str:
    manifest = ROOT / "_meta" / "SYSTEM_MANIFEST.md"
    if not manifest.is_file():
        return "0.0.0"
    m = re.search(r"^- \*\*Versi:\*\* `([^`]+)`", manifest.read_text(encoding="utf-8"), re.MULTILINE)
    return m.group(1) if m else "0.0.0"


def source_sha(path: Path) -> str:
    return hashlib.sha1(path.read_bytes()).hexdigest()


def write_seed_system() -> None:
    """Tambahkan benih sistem generik ke TEMPLATE COPY, bukan ke master.

    Benih ini sengaja self-contained sejak hari pertama: validator sistem ada
    di dalam foldernya, ada satu STATUS unit sehat, dan ada satu contoh salinan
    berlabel nyata dari berkas master yang memang ada.
    """
    name = "sistem-benih"
    root = TEMPLATE_DIR / name
    (root / "_sistem").mkdir(parents=True, exist_ok=True)
    (root / "_salinan-meta").mkdir(parents=True, exist_ok=True)
    (root / "runs" / "benih-001").mkdir(parents=True, exist_ok=True)

    (root / "README.md").write_text(
        "# Sistem Benih\n\n"
        "Folder ini dibuat otomatis oleh build_template.py sebagai titik awal sistem baru. "
        "Ia bukan contoh domain; isinya hanya rangka minimum agar kontrak folder mandiri bisa diuji.\n\n"
        "## Cara pakai\n\n"
        "- Isi identitas dan dokumen domain sesuai hasil Discovery Level-0.\n"
        "- Jalankan `python3 _sistem/validate_system.py` dari folder ini untuk cek rangka minimum.\n"
        "- Jalankan `python3 tools/check_selfcontained.py --sistem sistem-benih` dari root repo template untuk membuktikan folder ini dapat disalin sendiri.\n"
        "- Mekanisme `LOG_SESI` wajib diturunkan saat sistem mulai dipakai.\n\n"
        "## Contoh salinan berlabel\n\n"
        "Berkas `_salinan-meta/TEMPLATE_LOG_SESI.md` adalah contoh salinan berlabel nyata "
        "dengan sumber `_meta/TEMPLATE_LOG_SESI.md`. Jika pola ini dipakai untuk dokumen lain, "
        "tiga baris label wajib dipertahankan.\n",
        encoding="utf-8",
    )
    (root / "PROMPT_ENTRI_UNIVERSAL.md").write_text(
        "# Prompt Entri Universal — Sistem Benih\n\n"
        "Baca README.md, SYSTEM_MANIFEST.md, lalu tanya tujuan sesi. Jangan menulis isi domain sebelum tujuan dikonfirmasi.\n",
        encoding="utf-8",
    )
    (root / "PANDUAN_PENGGUNA.md").write_text(
        "# Panduan Pengguna — Sistem Benih\n\n"
        "agent_instruction: IGNORE for execution — USER GUIDE ONLY\n\n"
        "Gunakan folder ini sebagai rangka awal. Prompt pembuka ada di PROMPT_ENTRI_UNIVERSAL.md. "
        "Prompt penutup wajib menutup LOG_SESI, memastikan commit/push, dan mencatat pekerjaan tersisa.\n",
        encoding="utf-8",
    )
    (root / "SYSTEM_MANIFEST.md").write_text(
        "# System Manifest — Sistem Benih\n\n"
        "- **Nama sistem:** Sistem Benih\n"
        "- **Tujuan utama:** rangka minimum sistem baru dari template bersih\n"
        "- **Pengguna/consumer:** pemilik repo dan agent\n"
        "- **Pemilik keputusan:** pengguna\n"
        "- **Versi:** `0.1.0`\n"
        "- **Tahap:** `siap-pakai`\n"
        "- **Status:** `Seed`\n"
        "- **Dipakai via lmarena?** Ya\n\n"
        "## Warisan (Kontrak)\n\n"
        "| Butir | Status (diterapkan / override) | Letak di folder sistem | Override? |\n"
        "|---|---|---|---|\n"
        "| W-01 pegangan | diterapkan | PROMPT_ENTRI_UNIVERSAL.md + PANDUAN_PENGGUNA.md | |\n"
        "| W-02 LOG_SESI | diterapkan | README.md + panduan penutup | |\n"
        "| W-03 field checkpoint STATUS | diterapkan | runs/benih-001/STATUS.md | |\n"
        "| W-04 manifest | diterapkan | SYSTEM_MANIFEST.md | |\n"
        "| W-05 log keputusan | diterapkan | SYSTEM_MANIFEST.md | |\n"
        "| W-06 QA 3-lapis | diterapkan | _sistem/validate_system.py | |\n"
        "| W-07 fakta platform | diterapkan | bagian Dipakai via lmarena | |\n"
        "| W-08 approval bertingkat | diterapkan | keputusan pengguna sebelum isi domain | |\n"
        "| W-09 ringkasan cadangan | diterapkan | _cadangan-claude dibuat di root template | |\n\n"
        "## Log Keputusan\n\n"
        "| Tanggal | Perubahan | Alasan | Approval |\n"
        "|---|---|---|---|\n"
        "| 2026-09-08 | Benih dibuat otomatis oleh build_template.py | Sistem baru harus membawa validator dan contoh salinan berlabel sejak lahir | Keputusan pemilik PR A |\n",
        encoding="utf-8",
    )
    (root / "runs" / "benih-001" / "STATUS.md").write_text(
        "# STATUS — benih-001\n\n"
        "- **Status:** `in-progress`\n"
        "- **Pekerjaan belum tersimpan:** Tidak ada\n",
        encoding="utf-8",
    )
    (root / "_sistem" / "validate_system.py").write_text(
        "#!/usr/bin/env python3\n"
        "from pathlib import Path\n"
        "import re\n"
        "import sys\n\n"
        "ROOT = Path(__file__).resolve().parents[1]\n"
        "REQ = [\n"
        "    'README.md', 'SYSTEM_MANIFEST.md', 'PROMPT_ENTRI_UNIVERSAL.md',\n"
        "    'PANDUAN_PENGGUNA.md', '_sistem/validate_system.py',\n"
        "    '_salinan-meta/TEMPLATE_LOG_SESI.md', 'runs/benih-001/STATUS.md',\n"
        "]\n\n"
        "def field_values(text, label):\n"
        "    pat = re.compile(r'^[ \\t]*(?:[-*][ \\t]+)?\\*{0,2}\\s*' + re.escape(label) + r'\\s*[:：]\\s*\\*{0,2}\\s*(.*?)\\s*$', re.MULTILINE)\n"
        "    return [m.group(1).strip().strip('`').strip() for m in pat.finditer(text)]\n\n"
        "findings = []\n"
        "for rel in REQ:\n"
        "    if not (ROOT / rel).is_file():\n"
        "        findings.append(f'berkas wajib hilang: {rel}')\n"
        "status = ROOT / 'runs/benih-001/STATUS.md'\n"
        "if status.is_file():\n"
        "    vals = field_values(status.read_text(encoding='utf-8'), 'Pekerjaan belum tersimpan')\n"
        "    if vals != ['Tidak ada']:\n"
        "        findings.append('STATUS benih harus memuat Pekerjaan belum tersimpan: Tidak ada')\n"
        "manifest = ROOT / 'SYSTEM_MANIFEST.md'\n"
        "if manifest.is_file() and not field_values(manifest.read_text(encoding='utf-8'), 'Versi'):\n"
        "    findings.append('SYSTEM_MANIFEST.md: baris Versi tidak ada')\n"
        "print('VALIDATOR SISTEM BENIH')\n"
        "print('  root sistem:', ROOT.name + '/')\n"
        "print('  temuan:', len(findings))\n"
        "for item in findings:\n"
        "    print('  - ' + item)\n"
        "print('HASIL: ' + ('PASS' if not findings else 'FAIL'))\n"
        "sys.exit(0 if not findings else 1)\n",
        encoding="utf-8",
    )
    os.chmod(root / "_sistem" / "validate_system.py", 0o755)

    src_rel = "_meta/TEMPLATE_LOG_SESI.md"
    src = ROOT / src_rel
    label = (
        f"> Salinan turunan. Sumber: {src_rel} sha {source_sha(src)} tanggal 2026-09-08 versi-meta {current_meta_version()}\n"
        "> Perbedaan: tidak ada\n"
        "> Pemakaian: contoh salinan berlabel nyata untuk benih sistem baru\n"
    ).encode("utf-8")
    (root / "_salinan-meta" / "TEMPLATE_LOG_SESI.md").write_bytes(label + src.read_bytes())


def smoke_extract() -> bool:
    with TemporaryDirectory() as d:
        ex = Path(d) / "extract"
        ex.mkdir()
        with zipfile.ZipFile(TEMPLATE_ZIP) as zf:
            zf.extractall(ex)
        git = shutil.which("git")
        if git:
            subprocess.run([git, "init", "-q"], cwd=ex, capture_output=True)
        commands = [
            ("python3 tools/validate_repo.py", [sys.executable, "tools/validate_repo.py"], {}),
            ("python3 tools/test_failure_injection.py", [sys.executable, "tools/test_failure_injection.py"], {"FI_SKIP_NESTED": "1"}),
            ("python3 tools/check_selfcontained.py --semua", [sys.executable, "tools/check_selfcontained.py", "--semua"], {}),
        ]
        ok = True
        print("--- SMOKE EXTRACT ---")
        for label, cmd, extra_env in commands:
            print(f"$ {label}")
            proc = subprocess.run(
                cmd,
                cwd=ex,
                capture_output=True,
                text=True,
                env={**os.environ, **extra_env, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            if proc.stdout:
                print(proc.stdout.rstrip())
            if proc.stderr:
                print("[stderr]")
                print(proc.stderr.rstrip())
            print(f"exit={proc.returncode}")
            if proc.returncode != 0:
                ok = False
        print("--- SMOKE EXTRACT " + ("PASSED" if ok else "FAILED") + " ---")
        return ok


def build():
    if TEMPLATE_DIR.exists():
        shutil.rmtree(TEMPLATE_DIR)
    TEMPLATE_DIR.mkdir(parents=True)

    missing = [rel for rel in include_list() if not (ROOT / rel).is_file()]
    if missing:
        print(f"TEMPLATE BUILD FAILED: required source missing: {missing}")
        return False

    for rel in include_list():
        src = ROOT / rel
        dst = TEMPLATE_DIR / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    # M-16: the shipped master manifest is history/reference, not the new
    # repo's identity — mark it so a fresh agent cannot mistake it for one.
    manifest_copy = TEMPLATE_DIR / "_meta/SYSTEM_MANIFEST.md"
    if manifest_copy.is_file():
        body = manifest_copy.read_text(encoding="utf-8")
        manifest_copy.write_text(MANIFEST_BANNER + body, encoding="utf-8")

    # F5 (review PR #11, 5 Sep 2026): template self-containment transforms.
    # Two active instructions in the shipped master docs point at files the
    # template deliberately does not ship (the handoff doc, and the
    # konten-kreator user guide). Rewrite them in the TEMPLATE COPIES only —
    # the master keeps its operational references. An anchor that no longer
    # matches means the source doc changed: fail the build, do not ship a
    # template with a silently stale bootstrap.
    def transform(rel, pairs):
        path = TEMPLATE_DIR / rel
        t = path.read_text(encoding="utf-8")
        for old, new in pairs:
            # Idempotent: re-running on an already-templated repo is a no-op;
            # a doc that has NEITHER the anchor NOR the target text has
            # drifted — fail the build.
            if old in t:
                t = t.replace(old, new)
            elif new not in t:
                return (f"transform anchor not found in {rel}: {old[:70]!r} "
                        "(dan teks target tidak ada — dokumen berubah?)")
        path.write_text(t, encoding="utf-8")
        return None

    for err in (
        transform("_meta/NEXT_SESSION_PROMPT.md", [
            ("6. Baca `_meta/_internal/HANDOFF_NEXT_SESSION.md`.",
             "6. Kalau `_meta/_internal/HANDOFF_NEXT_SESSION.md` ada, bacanya. "
             "Di repo baru dari template file ini TIDAK ada — lewati tanpa konflik "
             "(handoff dibuat sesi terakhir di repo asal; ketiadaannya bukan cacat)."),
            ("9. Verifikasi bahwa path dan artefak yang disebut handoff benar-benar ada.",
             "9. Verifikasi bahwa path dan artefak yang disebut handoff (kalau ada) "
             "benar-benar ada."),
        ]),
        transform("PANDUAN_PENGGUNA.md", [
            ("Untuk istilah teknis lain (branch, PR, merge, commit) — lihat "
             "`sistem-konten-kreator/panduan/PANDUAN_PENGGUNA.md`, penjelasannya sama "
             "berlaku di sini.",
             "Istilah teknis singkat: **branch** = salinan kerja; **commit** = snapshot "
             "tersimpan; **PR** = usulan penggabungan kerja; **merge** = penggabungan "
             "usulan yang sudah disetujui. Tiap sistem di repo ini juga punya "
             "PANDUAN_PENGGUNA.md miliknya sendiri (kontrak W-01) dengan istilah yang "
             "disesuaikan."),
        ]),
    ):
        if err:
            print(f"TEMPLATE BUILD FAILED: {err}")
            return False

    # M-01 guard: every core _meta file (obligation) that is referenced
    # (bare filename or _meta/path) from any active _meta document must ship
    # in the template — this is what silently broke for
    # PANDUAN_PENGGUNA_TEMPLATE.md and TEMPLATE_LOG_SESI.md. The core list is
    # checked even for files that no longer exist on disk (F1).
    import re

    ref_re = re.compile(r"`([^`\n]+\.md)`")
    meta_files = {
        Path(f).name: ROOT / f
        for f in (set(core.CORE_META_FILES)
                  | {f"_meta/{p.name}" for p in (ROOT / "_meta").glob("*.md")})
    }
    drifted = []
    for doc in meta_files.values():
        for line in doc.read_text(encoding="utf-8").splitlines():
            for m in ref_re.finditer(line):
                ref = m.group(1).split("/")[-1]
                if ref in meta_files and not (TEMPLATE_DIR / "_meta" / ref).is_file():
                    drifted.append(f"{doc.name} -> {ref}")
    if drifted:
        print("TEMPLATE BUILD FAILED: referenced _meta file not in template: "
              + ", ".join(sorted(set(drifted))))
        return False

    write_seed_system()

    for d in EMPTY_DIRS:
        (TEMPLATE_DIR / d).mkdir(parents=True, exist_ok=True)
        (TEMPLATE_DIR / d / ".gitkeep").write_text("", encoding="utf-8")

    # Clean INDEKS_SISTEM.md to remove example systems and register the seed
    indeks_path = TEMPLATE_DIR / "_meta/INDEKS_SISTEM.md"
    if indeks_path.is_file():
        # Write minimal index with the generated seed system
        indeks_path.write_text(
            "# Indeks Sistem\n\n"
            "### Daftar semua sistem yang ada di repo ini, dengan status dan tanggal terakhir disentuh. Dicatat MANUAL oleh agent setiap kali selesai kerja di suatu sistem — TIDAK mengandalkan pembacaan git history. Dibaca di awal sesi untuk menentukan apakah perlu menawarkan audit sebelum lanjut kerja (lihat `00_CARA_KERJA_META.md`).\n\n"
            "---\n\n"
            "## Cara pakai\n\n"
            "- **Sebelum mulai kerja di suatu sistem:** cek baris sistem itu di tabel bawah. Kalau \"Terakhir Disentuh\" sudah lama (pengguna yang menilai apa itu \"lama\" — tidak ada angka pasti, tergantung konteks), tawarkan audit dulu.\n"
            "- **Setelah selesai kerja di suatu sistem (apapun jenis kerjanya):** update baris sistem itu — tanggal hari ini, dan status terbaru.\n"
            "- **Sistem baru:** tambah baris baru begitu `00_RENCANA_KERANGKA.md`-nya sudah di-merge ke `main` (lihat `01_DISCOVERY_LEVEL_0.md`).\n\n"
            "---\n\n"
            "## Daftar Sistem\n\n"
            "| Nama Sistem | Folder | Status | Terakhir Disentuh | Catatan |\n"
            "|---|---|---|---|---|\n"
            "| Sistem Benih | `sistem-benih/` | Seed self-contained | 2026-09-08 | Rangka minimum; jalankan `python3 tools/check_selfcontained.py --sistem sistem-benih` setelah ekstrak |\n\n"
            "---\n\n"
            "## Legenda Status\n\n"
            "- **Kerangka dibuat, isi belum** — `00_RENCANA_KERANGKA.md` sudah ada dan di-merge, tapi dokumen-dokumen isinya belum mulai digali\n"
            "- **Sedang dibangun** — sebagian dokumen sudah digali/ditulis, belum semua selesai\n"
            "- **Selesai, belum diaudit** — semua dokumen yang direncanakan sudah ditulis, tapi belum melalui audit menyeluruh\n"
            "- **Selesai, teraudit [n]x** — sudah melalui audit menyeluruh sebanyak n kali, siap dipakai\n"
            "- **Aktif dipakai** — sedang dipakai untuk kerja produksi/operasional sehari-hari (bukan lagi tahap pembangunan)\n",
            encoding="utf-8",
        )

    # Create zip
    if TEMPLATE_ZIP.exists():
        TEMPLATE_ZIP.unlink()
    with zipfile.ZipFile(TEMPLATE_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for p in TEMPLATE_DIR.rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(TEMPLATE_DIR))

    print(f"TEMPLATE CLEAN BUILT: {TEMPLATE_DIR}")
    print(f"TEMPLATE ZIP: {TEMPLATE_ZIP} ({TEMPLATE_ZIP.stat().st_size} bytes)")

    # Verify AT-10: no internal audit, no pilot, no konten-kreator.
    # Definisi "area yang tidak boleh keluar dari master" hidup di
    # checkpoint_core.master_only_reason() — SATU definisi, dipakai juga oleh
    # tools/check_selfcontained.py supaya tidak ada alat yang menawarkan
    # salinan berlabel untuk path yang verifikasi ini tolak (PR A2, 9 Sep 2026).
    bad = []
    for p in TEMPLATE_DIR.rglob("*"):
        rel = p.relative_to(TEMPLATE_DIR).as_posix()
        head = ""
        if p.is_file() and p.suffix == ".md":
            try:
                head = p.read_text(encoding="utf-8")[:400]
            except (OSError, UnicodeDecodeError):
                head = ""
        reason = core.master_only_reason(rel, head)
        if reason == core.REFERENCE_ONLY_REASON:
            bad.append(f"{rel} (reference_only historical doc)")
        elif reason:
            bad.append(rel)
    if bad:
        print(f"TEMPLATE VERIFY FAILED: should not contain: {bad}")
        return False
    print("TEMPLATE VERIFY PASSED: no personal data, no production output, no internal audit, no domain example, no reference_only historical doc")
    if not smoke_extract():
        return False
    return True

if __name__ == "__main__":
    ok = build()
    if not ok:
        raise SystemExit(1)
    print("TEMPLATE CLEAN BUILD PASSED")
