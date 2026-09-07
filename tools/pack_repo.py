#!/usr/bin/env python3
"""Bangkitkan SATU folder repo mandiri dari satu sistem domain di repo master.

Aturan normatifnya ada di `_meta/PAKET_REPO_MANDIRI.md`; file ini adalah
penegaknya. Kalau keduanya berbeda, dokumennya yang benar.

Pemakaian:
    python3 tools/pack_repo.py <sistem-x> [--out DIR] [--zip] [--check] [--versi V]

Sifat yang dijaga:

* **Tidak ada rewriting isi.** Selain TIGA suntingan yang diizinkan (tabel
  "Daftar Sistem" di salinan INDEKS, README root baru, PAKET_REPO.md +
  profil PAKET_REPO.json), setiap berkas disalin byte-per-byte.
* **Layout identik master.** `sistem-<nama>/` tetap subfolder — nol
  penulisan ulang path, `tools/validate_repo.py` bisa dipakai apa adanya.
* **Gagal = tidak ada paket.** Paket ditulis, lalu divalidasi DI DALAM
  hasil pack. Merah -> paket dihapus, exit non-nol, penyebabnya dicetak.
* **Deterministik.** Urutan berkas terurut path; tidak ada cap waktu run di
  mana pun (tanggal yang dipakai = tanggal commit sumber); dua run dari sha
  yang sama menghasilkan pohon identik.

Catatan desain — kenapa daftar `absent_refs_allowed` TIDAK diprediksi oleh
alat ini sendiri: alat ini membangun paket dengan daftar KOSONG lebih dulu,
menjalankan `tools/validate_repo.py` di dalamnya, lalu MEMBACA rujukan
menggantung yang benar-benar dilaporkan validator. Dengan begitu daftar
putih tidak pernah berasal dari tebakan paralel yang bisa melenceng dari
penegaknya; ia berasal dari penegaknya sendiri. Setiap rujukan menggantung
yang tidak masuk kategori sah (bagian 5 protokol) menjadi PEMBLOKIR.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import checkpoint_core as core

ROOT = Path(__file__).resolve().parents[1]

# --- Apa yang ikut (bagian 2 protokol) --------------------------------------
TOOLS_SUBSET = ["tools/checkpoint_core.py", "tools/validate_repo.py"]
ROOT_COPY_FILES = [
    "PANDUAN_PENGGUNA.md",
    "PROMPT_ENTRI_UNIVERSAL.md",
    ".gitignore",
    ".gitattributes",
]
# Dibangkitkan, bukan disalin (tiga suntingan + wadah log kosong).
GENERATED_ROOT = ["README.md", "PAKET_REPO.md", "LOG_SESI.md"]
PROFILE_REL = core.PROFILE_REL  # "_meta/PAKET_REPO.json"

# Berkas di DALAM folder sistem yang tetap tidak ikut: dokumen sejarah
# sesi-rekaman milik master (bagian 11 protokol).
SYSTEM_EXCLUDE_GLOBS = ("UJI_F7_CLEAN_RUN_*.md", "LOG_SESI_*.md")

JUNK_DIRS = {".git", "__pycache__", ".ipynb_checkpoints", ".pytest_cache"}
JUNK_NAMES = {".DS_Store"}
JUNK_SUFFIX = (".pyc",)

# Alat meta yang sengaja tinggal di master (kategori K2).
MASTER_ONLY_TOOLS = {
    "tools/backup_verify.py",
    "tools/build_template.py",
    "tools/test_failure_injection.py",
    "tools/pack_repo.py",
}
# Area artefak/arsip master (kategori K4).
MASTER_ARTIFACT_PREFIXES = (
    "_meta/_internal/",
    "dist/",
    "_cadangan-claude/",
    "_pegangan-kamu/",
    "backups/",
    "template_clean",
)
MASTER_ARTIFACT_NAME_RE = re.compile(r"^(LOG_SESI_.*|UJI_F7_CLEAN_RUN_.*)\.md$")

PILOT = core.EXACT_PILOT

# --- Pemindai rujukan (untuk closure `_meta/` saja) -------------------------
# Cerminan sengaja dari aturan di tools/validate_repo.py. Ia dipakai HANYA
# untuk memutuskan berkas `_meta/` mana yang ikut. Verdict resmi tetap milik
# validator yang dijalankan di dalam hasil pack; kalau cerminan ini meleset,
# validator itu yang menjatuhkan paketnya — melenceng diam-diam tidak mungkin.
REF_RE = re.compile(r"`([^`\n]+)`")
PATH_EXTENSIONS = (".md", ".py", ".zip", ".json")


def is_path_like(ref: str) -> bool:
    if "://" in ref or re.match(r"^[a-z][a-z0-9+.-]*:", ref, re.IGNORECASE):
        return False
    return (
        "/" in ref
        and not any(c in ref for c in ("[", "<", "*", " "))
        and not ref.startswith("/")
        and ref.lower().endswith(PATH_EXTENSIONS)
    )


def refs_of(path: Path):
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        for m in REF_RE.finditer(line):
            ref = m.group(1)
            if is_path_like(ref):
                out.append(ref)
    return out


SYSTEM_DOC_GLOBS = ("{n}/*.md", "{n}/_sistem/*.md", "{n}/panduan/*.md",
                    "{n}/_generator/*.md", "{n}/_template/*.md")


def system_active_docs(name: str):
    docs = []
    for pat in SYSTEM_DOC_GLOBS:
        docs += [p for p in ROOT.glob(pat.format(n=name)) if p.is_file()]
    return sorted(set(docs))


# --- Helper -----------------------------------------------------------------
def git(*args, cwd=ROOT):
    env = {**os.environ, "TZ": "UTC"}
    r = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True,
                       text=True, env=env)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


VERSI_RE = re.compile(r"^\s*-\s*\*\*Versi:\*\*\s*`?([^`\n]+?)`?\s*$", re.MULTILINE)


def manifest_versi(manifest: Path):
    m = VERSI_RE.search(manifest.read_text(encoding="utf-8"))
    return m.group(1).strip() if m else None


def is_junk(p: Path) -> bool:
    if any(part in JUNK_DIRS for part in p.parts):
        return True
    return p.name in JUNK_NAMES or p.suffix in JUNK_SUFFIX


def system_files(name: str):
    """Semua berkas folder sistem, utuh, kecuali sampah build dan dokumen
    sejarah sesi-rekaman milik master."""
    base = ROOT / name
    out = []
    for p in sorted(base.rglob("*")):
        if not p.is_file() or is_junk(p):
            continue
        rel = p.relative_to(ROOT).as_posix()
        if any(p.match(g) for g in SYSTEM_EXCLUDE_GLOBS):
            continue
        out.append(rel)
    return sorted(out)


# --- Subset `_meta/` (bagian 3 & 4 protokol) --------------------------------
def meta_subset(name: str):
    """Kembalikan (subset_md, kedalaman, internal_files, hilang).

    subset_md  : berkas `_meta/*.md` hasil transitive closure sampai fixpoint
    kedalaman  : peta berkas -> kedalaman tempat ia pertama masuk
    internal   : berkas `_meta/_internal/...` yang dirujuk LANGSUNG dok sistem
    hilang     : rujukan `_meta/` yang tidak ada berkasnya di master
    """
    seed, internal, hilang = set(), set(), set()
    # Benih = dokumen aktif sistem + berkas root yang ikut paket dan ikut
    # dipindai validator (pegangan pengguna). Keduanya adalah dokumen aktif
    # repo mandiri, jadi rujukan `_meta/` keduanya sama-sama mengikat.
    seed_docs = system_active_docs(name) + [
        ROOT / r for r in ROOT_COPY_FILES if (ROOT / r).suffix == ".md"
    ]
    for doc in seed_docs:
        for ref in refs_of(doc):
            if not ref.startswith("_meta/"):
                continue
            if ref.startswith("_meta/_internal/"):
                if (ROOT / ref).is_file():
                    internal.add(ref)
                # rujukan _internal yang tidak ada = artefak master, bukan
                # pemblokir: ia memang tidak pernah ikut paket.
                continue
            if (ROOT / ref).is_file():
                seed.add(ref)
            else:
                hilang.add(ref)

    # INDEKS selalu wajib: validator membacanya sebagai sumber daftar sistem.
    seed.add("_meta/INDEKS_SISTEM.md")

    depth = {f: 0 for f in seed}
    closure = set(seed)
    frontier, level = set(seed), 0
    while frontier:
        level += 1
        new = set()
        for f in sorted(frontier):
            for ref in refs_of(ROOT / f):
                if (ref.startswith("_meta/")
                        and not ref.startswith("_meta/_internal/")
                        and ref not in closure):
                    if (ROOT / ref).is_file():
                        new.add(ref)
                    else:
                        hilang.add(ref)
        for n in new:
            depth[n] = level
        closure |= new
        frontier = new
    return sorted(closure), depth, sorted(internal), sorted(hilang)


# --- Tiga suntingan yang diizinkan ------------------------------------------
PILOT_BULLET_RE = re.compile(r"^- \*\*`" + re.escape(PILOT) + r"/`\*\*")


def rewrite_indeks(text: str, name: str):
    """Suntingan #1: tabel 'Daftar Sistem' dipangkas jadi SATU baris (sistem
    yang di-pack) dan butir daftar fixture pilot dihapus. Tidak ada bagian
    lain yang disentuh."""
    lines = text.splitlines()
    out, in_table, kept_row, dropped = [], False, False, 0
    for line in lines:
        s = line.strip()
        if s.startswith("## "):
            in_table = s[3:].strip().lower().startswith("daftar sistem")
            out.append(line)
            continue
        if in_table and s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r"[-: ]*", c) for c in cells):
                out.append(line)          # separator
                continue
            if any("folder" in c.lower() for c in cells) and not kept_row and not dropped:
                out.append(line)          # header
                continue
            if len(cells) > 1 and cells[1] == f"`{name}/`":
                out.append(line)
                kept_row = True
            else:
                dropped += 1
            continue
        if PILOT_BULLET_RE.match(line):
            dropped += 1
            continue
        out.append(line)
    if not kept_row:
        raise RuntimeError(f"INDEKS_SISTEM: baris untuk `{name}/` tidak ditemukan")
    return "\n".join(out) + "\n", dropped


def render_readme(name, versi, sha, tanggal):
    judul = name.replace("sistem-", "").replace("-", " ").title()
    return f"""# {judul}

Repo ini berisi **satu** sistem kerja: `{name}/` (versi `{versi}`).

Ia dibangkitkan dari repo master meta-sistem sebagai **paket repo mandiri** —
isi dokumennya tidak ditulis ulang, dan layout foldernya sengaja sama persis
dengan master supaya setiap rujukan di dalam dokumen tetap valid.

## Mulai dari mana

1. Baca `PANDUAN_PENGGUNA.md` (pegangan pengguna: prompt pembuka universal +
   prompt penutup sesi). Kalau hanya butuh prompt pembukanya, ada di
   `PROMPT_ENTRI_UNIVERSAL.md`.
2. Untuk agent: masuk ke `{name}/` dan ikuti dokumen navigasinya.
3. `LOG_SESI.md` di root sengaja kosong — repo ini memulai log sesinya sendiri.

## Memeriksa repo ini masih sehat

```
python3 tools/validate_repo.py
cd {name} && python3 _sistem/validate_system.py
```

Keduanya harus PASS. Perintah pertama memeriksa struktur repo dan rujukan
antardokumen; perintah kedua memeriksa isi sistemnya sendiri dan berjalan
tanpa bergantung pada `_meta/` maupun `tools/`.

## Isi repo

| Bagian | Keterangan |
|---|---|
| `{name}/` | sistem itu sendiri — utuh, termasuk fixture dan folder produksi |
| `_meta/` | HANYA dokumen meta yang benar-benar dirujuk sistem ini |
| `tools/` | dua alat: pemeriksa struktur repo + parser bersamanya |
| `PAKET_REPO.md` | berita acara paket: asal, apa yang dikecualikan, sha256 tiap berkas |

## Asal-usul

- Commit sumber: `{sha}`
- Tanggal commit sumber (UTC): {tanggal}
- Rincian lengkap + perintah verifikasi: `PAKET_REPO.md`
"""


EXCLUDE_REASONS = [
    ("Sistem domain lain", "satu paket = satu sistem; itu seluruh gunanya"),
    (f"{PILOT}/", "fixture uji meta-sistem, bukan sistem domain — tidak pernah terdaftar sebagai sistem"),
    ("_meta/_internal/ (selain yang dirujuk langsung sistem)", "audit & handoff historis = referensi master, bukan instruksi aktif repo ini"),
    ("_meta/_internal/backups/, template_clean, template_clean.zip", "artefak build; di master pun tidak di-commit"),
    ("tools/backup_verify.py, tools/build_template.py, tools/test_failure_injection.py, tools/pack_repo.py", "alat pemelihara MASTER (template bersih, backup, injeksi kegagalan meta, pembangkit paket). Di repo ini mereka akan menunjuk struktur yang tidak ada. Tetap tinggal di master — tidak ikut bukan berarti dihapus"),
    ("LOG_SESI_*.md master", "log sesi repo master; repo ini memulai lognya sendiri"),
    ("UJI_F7_CLEAN_RUN_*.md dan dokumen sejarah sesi-rekaman", "catatan peristiwa master, bukan aturan sistem"),
    ("dist/ dan berkas zip hasil pack", "keluaran, bukan sumber"),
    ("_cadangan-claude/, _pegangan-kamu/", "arsip/berkas milik pemilik di master; repo ini tidak memerlukannya untuk berfungsi"),
]


def render_paket_repo(name, versi, sha, dirty, tanggal, edits, absent, digests, meta_files, internal_files):
    lines = []
    A = lines.append
    A(f"# Paket Repo Mandiri — {name}")
    A("")
    A(f"Berita acara paket. Dibangkitkan `tools/pack_repo.py` sesuai `_meta/PAKET_REPO_MANDIRI.md` di repo master.")
    A("")
    A("## Asal")
    A("")
    A("| | |")
    A("|---|---|")
    A(f"| Sistem | `{name}/` |")
    A(f"| Versi sistem | `{versi}` (diambil dari baris Versi manifest sistem, tidak dikarang) |")
    A(f"| Commit sumber (sha) | `{sha}` |")
    A(f"| Pohon kerja sumber | {'**KOTOR — ada perubahan belum di-commit saat paket dibuat**' if dirty else 'bersih'} |")
    A(f"| Tanggal commit sumber (UTC) | {tanggal} |")
    A("")
    A("Tanggal di atas adalah tanggal **commit sumber**, bukan cap waktu run. Paket "
      "sengaja tidak memuat cap waktu run di mana pun supaya dua run dari sha yang "
      "sama menghasilkan pohon yang identik.")
    A("")
    A("## Yang sengaja TIDAK ikut, beserta alasannya")
    A("")
    A("| Tidak ikut | Alasan |")
    A("|---|---|")
    for what, why in EXCLUDE_REASONS:
        A(f"| {what} | {why} |")
    A("")
    A("## Suntingan yang dilakukan (dan HANYA ini)")
    A("")
    A("Selain tiga butir di bawah, setiap berkas disalin **byte-per-byte** dari master.")
    A("")
    A("| # | Berkas | Suntingan |")
    A("|---|---|---|")
    for i, (f, what) in enumerate(edits, start=1):
        A(f"| {i} | `{f}` | {what} |")
    A("")
    A("Tambahan yang bukan suntingan atas isi apa pun: `LOG_SESI.md` dibangkitkan "
      "sebagai berkas KOSONG (0 byte) — wadah supaya repo ini memulai log sesinya sendiri.")
    A("")
    A(f"## Subset `_meta/` yang ikut ({len(meta_files)} berkas)")
    A("")
    A("Ditentukan dari rujukan nyata dokumen sistem (transitive closure sampai "
      "fixpoint), bukan dari inventaris inti penuh master.")
    A("")
    for f in meta_files:
        A(f"- `{f}`")
    if internal_files:
        A("")
        A("Dirujuk langsung dokumen sistem, dibawa sebagai lampiran (tidak direkursi):")
        A("")
        for f in internal_files:
            A(f"- `{f}`")
    A("")
    A("## `absent_refs_allowed` — rujukan yang memang tidak ada di repo ini")
    A("")
    if absent:
        A("Daftar ini eksplisit dan tertutup: rujukan menggantung yang TIDAK ada di "
          "sini adalah error, dan entri yang tidak lagi cocok dengan rujukan nyata "
          "juga error (anti pembusukan daftar putih).")
        A("")
        A("| Rujukan | Kategori | Alasan |")
        A("|---|---|---|")
        for item in absent:
            A(f"| `{item['ref']}` | {item['kategori']} | {item['alasan']} |")
    else:
        A("(kosong — tidak ada rujukan menggantung sama sekali)")
    A("")
    A("## sha256 tiap berkas")
    A("")
    A("```text")
    for rel, dg in digests:
        A(f"{dg}  {rel}")
    A("PAKET_REPO.md  (berkas ini sendiri — tidak dapat memuat sha256 dirinya)")
    A("```")
    A("")
    A("## Empat perintah verifikasi untuk dijalankan di repo baru")
    A("")
    A("```bash")
    A("# 1. struktur repo + rujukan antardokumen (harus PASS, 0 warning)")
    A("python3 tools/validate_repo.py")
    A("")
    A("# 2. isi sistem itu sendiri (harus PASS)")
    A(f"cd {name} && python3 _sistem/validate_system.py && cd ..")
    A("")
    A("# 3. jadikan repo git dan sambungkan ke GitHub")
    A("git init && git add -A && git commit -m \"" + f"{name} {versi} — paket repo mandiri dari master {sha[:7]}" + "\"")
    A("git branch -M main && git remote add origin git@github.com:<akun>/<nama-repo>.git")
    A("")
    A("# 4. kirim")
    A("git push -u origin main")
    A("```")
    A("")
    A("Paket ini **tidak** di-commit ke repo master. Master adalah satu-satunya "
      "sumber kebenaran; paket selalu bisa dibangkitkan ulang dari sha di atas.")
    A("")
    return "\n".join(lines) + "\n"


# --- Kategorisasi rujukan menggantung (bagian 5 protokol) -------------------
def categorize(ref: str, name: str, master_systems):
    top = ref.split("/")[0]
    if top.startswith("sistem-"):
        if top == name:
            return None
        if top == PILOT:
            return ("K3", "fixture uji meta-sistem di master, bukan sistem domain")
        return ("K1", "dokumen sistem domain lain di master; satu paket = satu sistem")
    if ref in MASTER_ONLY_TOOLS:
        return ("K2", "alat pemelihara master yang sengaja tidak ikut paket")
    if ref.startswith(MASTER_ARTIFACT_PREFIXES) or MASTER_ARTIFACT_NAME_RE.match(Path(ref).name):
        return ("K4", "artefak/arsip milik master; di master pun bukan sumber")
    # Rujukan relatif dokumen master yang di master hanya resolve di dalam
    # folder sistem LAIN (mis. dokumen `_sistem/` milik sistem lain).
    for other in master_systems:
        if other != name and (ROOT / other / ref).is_file():
            return ("K1", f"rujukan relatif dokumen master ke isi sistem lain ({other}/)")
    return None


UNRESOLVED_RE = re.compile(r"MANDIRI unresolved reference: ([^\s]+): `([^`]+)`")


def purge_pycache(pack: Path):
    """Jalankan-validator meninggalkan __pycache__ kalau interpreter menulis
    bytecode. Paket harus deterministik dan bersih, jadi sisa itu dibuang."""
    for d in sorted(pack.rglob("__pycache__"), reverse=True):
        shutil.rmtree(d, ignore_errors=True)


# Bytecode tidak boleh ditulis ke dalam paket: ia tidak deterministik dan
# bukan bagian dari isi paket.
CLEAN_ENV = {"FI_SKIP_NESTED": "1", "PYTHONDONTWRITEBYTECODE": "1"}


def run_validator(pack: Path):
    r = subprocess.run([sys.executable, "-B", str(pack / "tools" / "validate_repo.py")],
                       capture_output=True, text=True,
                       env={**os.environ, **CLEAN_ENV})
    purge_pycache(pack)
    return r


def run_system_validator(pack: Path, name: str):
    r = subprocess.run([sys.executable, "-B", "_sistem/validate_system.py"],
                       cwd=str(pack / name), capture_output=True, text=True,
                       env={**os.environ, **CLEAN_ENV})
    purge_pycache(pack)
    return r


# --- Pembangun paket --------------------------------------------------------
def build(name, versi, out: Path, sha, dirty, tanggal):
    """Tulis pohon paket ke `out` (harus belum ada / dibersihkan pemanggil).
    Kembalikan (copied_rels, meta_md, meta_internal, edits)."""
    meta_md, depth, meta_internal, hilang = meta_subset(name)
    if hilang:
        raise RuntimeError("rujukan `_meta/` menunjuk berkas yang tidak ada di master: "
                           + ", ".join(sorted(hilang)))

    copied = system_files(name) + meta_md + meta_internal + TOOLS_SUBSET + ROOT_COPY_FILES
    copied = sorted(set(copied))

    for rel in copied:
        src, dst = ROOT / rel, out / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    # Suntingan #1 — tabel Daftar Sistem + butir pilot.
    idx = out / "_meta" / "INDEKS_SISTEM.md"
    new_idx, dropped = rewrite_indeks(idx.read_text(encoding="utf-8"), name)
    idx.write_text(new_idx, encoding="utf-8")

    # Suntingan #2 — README root baru.
    (out / "README.md").write_text(render_readme(name, versi, sha, tanggal), encoding="utf-8")

    # Wadah log kosong (bukan suntingan atas isi apa pun).
    (out / "LOG_SESI.md").write_text("", encoding="utf-8")

    edits = [
        ("_meta/INDEKS_SISTEM.md",
         f"tabel \"Daftar Sistem\" dipangkas jadi satu baris (`{name}/`) + butir daftar fixture pilot dihapus "
         f"({dropped} baris dibuang). Bagian lain berkas ini utuh"),
        ("README.md", "berkas BARU — master tidak punya README root; halaman muka repo ini"),
        ("PAKET_REPO.md + _meta/PAKET_REPO.json",
         "berkas BARU — berita acara paket + profil repo (kewajiban file & daftar putih rujukan)"),
    ]
    return copied, meta_md, depth, meta_internal, edits


def write_profile(out: Path, name, versi, sha, tanggal, meta_md, meta_internal, absent):
    profile = {
        "schema": "paket-repo/1",
        "sistem": name,
        "versi": versi,
        "sumber_commit": sha,
        "tanggal": tanggal,
        "meta_subset": sorted(meta_md + meta_internal),
        "tools_subset": sorted(TOOLS_SUBSET),
        "root_files": sorted(ROOT_COPY_FILES + GENERATED_ROOT),
        "absent_refs_allowed": absent,
    }
    (out / PROFILE_REL).parent.mkdir(parents=True, exist_ok=True)
    (out / PROFILE_REL).write_text(
        json.dumps(profile, indent=2, ensure_ascii=False, sort_keys=False) + "\n",
        encoding="utf-8")
    return profile


def all_pack_files(out: Path):
    return sorted(p.relative_to(out).as_posix() for p in out.rglob("*")
                  if p.is_file() and not is_junk(p))


def produce(name, versi, out: Path, sha, dirty, tanggal, master_systems, verbose=True):
    """Bangun paket lengkap di `out`, dua-pass. Kembalikan (info, blockers)."""
    blockers = []
    copied, meta_md, depth, meta_internal, edits = build(name, versi, out, sha, dirty, tanggal)

    # Pass 1 — profil dengan daftar putih KOSONG; validator yang memberi tahu
    # rujukan mana yang benar-benar menggantung.
    write_profile(out, name, versi, sha, tanggal, meta_md, meta_internal, [])
    (out / "PAKET_REPO.md").write_text("(pass 1)\n", encoding="utf-8")
    r1 = run_validator(out)
    found = []
    seen = set()
    for line in (r1.stdout + r1.stderr).splitlines():
        m = UNRESOLVED_RE.search(line)
        if m and m.group(2) not in seen:
            seen.add(m.group(2))
            found.append((m.group(2), m.group(1)))

    absent = []
    for ref, where in sorted(found):
        cat = categorize(ref, name, master_systems)
        if cat is None:
            blockers.append(
                f"rujukan menggantung TIDAK terkategori: `{ref}` (mis. di {where}). "
                "Ini rujukan baru yang benar-benar putus — perbaiki di master, "
                "bukan dengan menambahkannya ke daftar putih")
            continue
        absent.append({"ref": ref, "kategori": cat[0], "alasan": cat[1]})
    absent.sort(key=lambda d: d["ref"])

    # Pass 2 — profil final + berita acara.
    write_profile(out, name, versi, sha, tanggal, meta_md, meta_internal, absent)
    digests = [(rel, sha256_of(out / rel)) for rel in all_pack_files(out)
               if rel != "PAKET_REPO.md"]
    (out / "PAKET_REPO.md").write_text(
        render_paket_repo(name, versi, sha, dirty, tanggal, edits, absent,
                          digests, meta_md, meta_internal),
        encoding="utf-8")

    info = {
        "copied": copied, "meta_md": meta_md, "depth": depth,
        "meta_internal": meta_internal, "edits": edits, "absent": absent,
        "files": all_pack_files(out),
    }
    return info, blockers


def preflight(name, master_systems, index_folders):
    """Pemblokir yang bisa diketahui sebelum apa pun dibangun."""
    blockers = []
    if not (ROOT / name).is_dir():
        blockers.append(f"folder `{name}/` tidak ada di master")
        return blockers
    if name == PILOT:
        blockers.append(f"`{name}/` adalah fixture uji meta-sistem, bukan sistem domain — tidak di-pack")
    if name not in index_folders:
        blockers.append(f"`{name}/` tidak terdaftar di tabel 'Daftar Sistem' `_meta/INDEKS_SISTEM.md`")
    if not (ROOT / name / "SYSTEM_MANIFEST.md").is_file():
        blockers.append(f"`{name}/SYSTEM_MANIFEST.md` tidak ada")
    for rel in core.SYSTEM_REQUIRED_FILES:
        if not (ROOT / name / rel).is_file():
            blockers.append(
                f"`{name}/{rel}` tidak ada — sistem tanpa validator mandiri tidak bisa "
                "di-pack (syarat ii 'siap di-upload')")
    for rel in TOOLS_SUBSET + ROOT_COPY_FILES:
        if not (ROOT / rel).is_file():
            blockers.append(f"berkas master wajib hilang: `{rel}`")
    return blockers


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Bangkitkan satu folder repo mandiri dari satu sistem domain.")
    ap.add_argument("sistem", help="nama folder sistem, mis. sistem-contoh")
    ap.add_argument("--out", default=None, help="folder tujuan (default dist/<sistem>-repo-<versi>/)")
    ap.add_argument("--zip", action="store_true", dest="do_zip", help="buat juga arsip zip")
    ap.add_argument("--check", action="store_true", help="jangan tulis apa pun; cetak rencana + pemblokir")
    ap.add_argument("--versi", default=None, help="paksa nomor versi (default: dari manifest sistem)")
    args = ap.parse_args(argv)

    name = args.sistem.rstrip("/")
    index_text = (ROOT / "_meta" / "INDEKS_SISTEM.md").read_text(encoding="utf-8")
    index_folders, index_errors = core.parse_index(index_text)
    master_systems = sorted(p.name for p in ROOT.glob("sistem-*/") if p.is_dir())

    blockers = [f"INDEKS_SISTEM: {e}" for e in index_errors]
    blockers += preflight(name, master_systems, index_folders)

    versi = args.versi
    if versi is None and (ROOT / name / "SYSTEM_MANIFEST.md").is_file():
        versi = manifest_versi(ROOT / name / "SYSTEM_MANIFEST.md")
        if versi is None:
            blockers.append(
                f"baris Versi tidak ditemukan di `{name}/SYSTEM_MANIFEST.md` — "
                "versi tidak dikarang; pakai --versi kalau memang disengaja")
    if versi is None:
        versi = "tanpa-versi"

    rc, sha, _ = git("rev-parse", "HEAD")
    if rc != 0:
        sha = "(tanpa-git)"
    _, porcelain, _ = git("status", "--porcelain")
    dirty = bool(porcelain.strip())
    rc, tanggal, _ = git("show", "-s", "--format=%cd", "--date=format:%Y-%m-%d", "HEAD")
    if rc != 0 or not tanggal:
        tanggal = "(tanpa-git)"

    if blockers:
        print(f"PACK {name} — PEMBLOKIR ({len(blockers)}):")
        for b in blockers:
            print(f"  - {b}")
        print("PACK DIBATALKAN: perbaiki pemblokir di master lebih dulu.")
        return 1

    out = Path(args.out) if args.out else (ROOT / "dist" / f"{name}-repo-{versi}")
    out = out.resolve()

    if args.check:
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d) / "pack"
            info, blk = produce(name, versi, tmp, sha, dirty, tanggal, master_systems)
            v = run_validator(tmp)
            s = run_system_validator(tmp, name)
            if v.returncode != 0:
                blk.append(f"`tools/validate_repo.py` di dalam calon paket GAGAL (exit {v.returncode})")
            elif "WARNINGS: 0" not in v.stdout:
                blk.append("`tools/validate_repo.py` di dalam calon paket tidak 0-warning")
            if s.returncode != 0:
                blk.append(f"validator sistem di dalam calon paket GAGAL (exit {s.returncode})")
            print_check(name, versi, out, sha, dirty, tanggal, info, blk, v, s)
            return 1 if blk else 0

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    info, blk = produce(name, versi, out, sha, dirty, tanggal, master_systems)

    v = run_validator(out)
    s = run_system_validator(out, name)
    print(f"PACK {name} -> {out}")
    print(f"  berkas: {len(info['files'])} | subset _meta: {len(info['meta_md']) + len(info['meta_internal'])} "
          f"| absent_refs_allowed: {len(info['absent'])}")
    print("--- python3 tools/validate_repo.py (DI DALAM hasil pack) ---")
    print(v.stdout.rstrip() or v.stderr.rstrip())
    print(f"exit={v.returncode}")
    print(f"--- python3 _sistem/validate_system.py (DI DALAM {name}/) ---")
    print(s.stdout.rstrip() or s.stderr.rstrip())
    print(f"exit={s.returncode}")

    fail = list(blk)
    if v.returncode != 0:
        fail.append(f"validate_repo.py GAGAL di dalam hasil pack (exit {v.returncode})")
    elif "WARNINGS: 0" not in v.stdout:
        fail.append("validate_repo.py di dalam hasil pack tidak 0-warning")
    if s.returncode != 0:
        fail.append(f"validate_system.py GAGAL di dalam hasil pack (exit {s.returncode})")
    if fail:
        shutil.rmtree(out, ignore_errors=True)
        print("PACK GAGAL — hasil pack DIHAPUS (pack yang gagal = tidak ada pack):")
        for f in fail:
            print(f"  - {f}")
        return 1

    if args.do_zip:
        archive = shutil.make_archive(str(out), "zip", root_dir=str(out.parent),
                                      base_dir=out.name)
        print(f"ZIP: {archive}")

    print(f"PACK OK: {out}")
    print(f"  berita acara: {out / 'PAKET_REPO.md'}")
    print("  paket ini TIDAK di-commit ke master (master = satu-satunya sumber kebenaran)")
    return 0


def print_check(name, versi, out, sha, dirty, tanggal, info, blockers, v, s):
    print(f"PACK CHECK — {name} (versi `{versi}`)")
    print(f"  commit sumber : {sha}{' (POHON KERJA KOTOR)' if dirty else ''}")
    print(f"  tanggal commit: {tanggal}")
    print(f"  tujuan (kalau dijalankan tanpa --check): {out}")
    print()
    print(f"(a) DAFTAR FILE YANG AKAN IKUT — {len(info['files'])} berkas")
    generated = set(GENERATED_ROOT) | {PROFILE_REL}
    for rel in info["files"]:
        tag = "dibangkitkan" if rel in generated else ("disunting" if rel == "_meta/INDEKS_SISTEM.md" else "salinan")
        print(f"  [{tag:>12}] {rel}")
    print()
    print(f"(b) SUBSET _meta — {len(info['meta_md'])} dokumen + {len(info['meta_internal'])} lampiran _internal")
    for f in info["meta_md"]:
        print(f"  d{info['depth'].get(f, '?')} {f}")
    for f in info["meta_internal"]:
        print(f"  L0 {f}   (lampiran, tidak direkursi)")
    print()
    print(f"(c) absent_refs_allowed — {len(info['absent'])} entri")
    if not info["absent"]:
        print("  (kosong)")
    for item in info["absent"]:
        print(f"  [{item['kategori']}] {item['ref']}")
        print(f"        {item['alasan']}")
    print()
    print(f"(d) DAFTAR PEMBLOKIR — {len(blockers)}")
    if not blockers:
        print("  (kosong — siap di-pack)")
    for b in blockers:
        print(f"  - {b}")
    print()
    print("verifikasi kering di calon paket:")
    print(f"  validate_repo.py exit={v.returncode} | "
          + next((l for l in v.stdout.splitlines() if l.startswith("WARNINGS:")), "(tanpa baris WARNINGS)"))
    print(f"  validate_system.py exit={s.returncode}")
    print("CHECK HIJAU" if not blockers else "CHECK MERAH")


if __name__ == "__main__":
    raise SystemExit(main())
