#!/usr/bin/env python3
"""Pembangkit PROMPT REVIEW INDEPENDEN dari data PR yang nyata.

Masalah yang dipecahkan (8 Sep 2026): prompt review selama ini dikarang oleh
sesi yang membuka PR — pihak yang direview menulis instruksi bagi pengadilnya,
dan pemilik harus menunggu sesi perantara supaya punya prompt sama sekali.
Alat ini memutus ketergantungan itu: SEMUA angka yang dicetak (nomor PR, base
sha, head sha, daftar berkas) berasal dari `gh`/`git`, bukan dari narasi.

Sifat yang dijaga (kontrak alat):
- DETERMINISTIK untuk data PR yang sama: tidak ada waktu-sekarang, tidak ada
  urutan acak, tidak ada pembacaan chat. Satu-satunya sumber adalah data PR +
  isi pohon kerja.
- TIDAK PERNAH MENULIS FILE kecuali diminta `--out <path>`.
- FAIL-CLOSED: PR tidak ada / tidak bisa dibaca / sha kosong => exit != 0 dan
  TIDAK ada prompt yang dicetak. Prompt setengah jadi lebih berbahaya daripada
  tidak ada prompt, karena reviewer akan mengira sha kosong itu sengaja.
- 6d (jendela uji): kalau ada `LOG_SESI_*.md` berkeadaan OPEN yang menyebut
  jendela uji/run acceptance berjalan, bagian yang biasanya mengutip rumusan
  acceptance test diganti pointer "SHA+baris" dan alat mencetak peringatan.

Pemakaian:
    python3 tools/review_prompt.py --pr 24
    python3 tools/review_prompt.py --generic
    python3 tools/review_prompt.py --pr 24 --out -        # stdout (default)
    python3 tools/review_prompt.py --pr 24 --out /tmp/p.md
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PLACEHOLDER_PR = "<NOMOR PR>"
PLACEHOLDER_BASE = "<BASE SHA>"
PLACEHOLDER_HEAD = "<HEAD SHA>"

# Pin regresi hanya dihitung bila sebuah tools/*.py benar-benar MENDEFINISIKAN
# konstanta yang dipin. Mencari nama konstanta sebagai substring membuat alat
# ini sendiri terlihat seolah-olah memuat pin hanya karena daftar marker ditulis
# di sumbernya.
PINNED_CONSTANTS = ("EXPECTED_TEMPLATE_WARNINGS", "CORE_REQUIRED", "SYSTEM_REQUIRED_FILES")
PIN_DEFINITION_RE = re.compile(
    r"^(?:[A-Z_]+\s*=\s*)?(?:" + "|".join(PINNED_CONSTANTS) + r")\s*=",
    re.MULTILINE,
)

# PR yang menyentuh salah satu dari ini = PR yang mengubah alat pengadil.
# Pengadil yang diubah tidak boleh mengeksekusi perubahan atas dirinya.
ARBITER_PATH_REASONS = {
    "tools/test_failure_injection.py": "alat injeksi kegagalan dan pin regresi",
    "_meta/PROTOKOL_REVIEW_INDEPENDEN.md": "protokol review independen",
    "tools/review_prompt.py": "pembangkit prompt pengadil",
}
ARBITER_PATHS = tuple(ARBITER_PATH_REASONS)

# Dokumen mekanisme yang selalu pelindung, terlepas dari isi PR.
STATIC_GUARDED_DOCS = (
    "_meta/TEMPLATE_RELEASE.md",
)

# Nomor dokumen aturan sistem domain yang tidak boleh berubah diam-diam.
GUARDED_SISTEM_PREFIXES = ("00", "05", "06")

# Folder yang berisi state produksi/fixture (bukan aturan, tapi bukti hidup).
PRODUCTION_DIR_HINTS = ("_produksi-aktif/", "deck-aktif/", "unit-aktif/")

# Folder tempat LOG_SESI hidup: root (konvensi lama, sebelum v1.13.0) dan
# `_log-sesi/` (konvensi berlaku sejak 9 Sep 2026 — v1.13.0).
LOG_SESI_DIRS = ("", "_log-sesi")

# `gh pr view --json files` berhenti di 100 berkas (T-2, temuan review PR #55).
# Dipakai hanya untuk mendeteksi ketidakkonsistenan; daftar lengkap datang dari
# `gh api --paginate`.
PR_FILES_VIEW_CAP = 100



class ToolError(Exception):
    """Kegagalan yang harus terlihat sebagai exit non-zero + pesan spesifik."""


# --------------------------------------------------------------------------
# Sumber data
# --------------------------------------------------------------------------
def _run(cmd: list[str]) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise ToolError(f"perintah tidak tersedia: {cmd[0]} ({exc})") from exc
    return proc.returncode, proc.stdout, proc.stderr


def fetch_pr(number: int) -> dict:
    """Baca data PR dari GitHub. Fail-closed: sha kosong = error, bukan prompt."""
    fields = "number,title,baseRefName,headRefName,headRefOid,files,body,isDraft"
    code, out, err = _run(["gh", "pr", "view", str(number), "--json", fields])
    if code != 0:
        raise ToolError(
            f"PR #{number} tidak bisa dibaca dari GitHub (gh pr view keluar {code}).\n"
            f"  keluaran gh: {(err or out).strip().splitlines()[0] if (err or out).strip() else '(kosong)'}\n"
            "  Periksa nomor PR-nya dan bahwa `gh auth status` sehat. "
            "Alat ini sengaja TIDAK mencetak prompt dengan sha kosong."
        )
    try:
        data = json.loads(out)
    except json.JSONDecodeError as exc:
        raise ToolError(f"jawaban `gh pr view` bukan JSON yang sah: {exc}") from exc

    # `baseRefOid` tidak tersedia di semua versi gh; base sha diambil dari API
    # REST supaya angkanya tetap berasal dari GitHub, bukan dari tebakan lokal.
    base_sha = fetch_base_sha(number)
    data["baseRefOid"] = base_sha

    for key in ("number", "baseRefName", "headRefName", "headRefOid", "baseRefOid"):
        if not data.get(key):
            raise ToolError(
                f"data PR #{number} tidak lengkap: field `{key}` kosong. "
                "Prompt tidak dicetak (fail-closed)."
            )
    if not re.fullmatch(r"[0-9a-f]{40}", str(data["headRefOid"])):
        raise ToolError(f"head sha PR #{number} bukan sha 40-heksadesimal: {data['headRefOid']!r}")
    if not re.fullmatch(r"[0-9a-f]{40}", str(data["baseRefOid"])):
        raise ToolError(f"base sha PR #{number} bukan sha 40-heksadesimal: {data['baseRefOid']!r}")
    return data


def fetch_base_sha(number: int) -> str:
    code, out, err = _run(
        ["gh", "api", f"repos/{{owner}}/{{repo}}/pulls/{number}", "--jq", ".base.sha"]
    )
    if code != 0 or not out.strip():
        raise ToolError(
            f"base sha PR #{number} tidak bisa dibaca (gh api keluar {code}): "
            f"{(err or out).strip()[:200] or '(kosong)'}"
        )
    return out.strip()


def files_command(number: int) -> list[str]:
    """argv `gh api` untuk daftar berkas PR — dipaginasi (T-2).

    Dipisah menjadi fungsi sendiri supaya paginasinya bisa diuji sebagai nilai
    yang benar-benar dipakai `fetch_pr_files`, bukan sekadar teks di sumber.
    """
    return [
        "gh",
        "api",
        f"repos/{{owner}}/{{repo}}/pulls/{number}/files",
        "--paginate",
        "--jq",
        ".[].filename",
    ]


def fetch_pr_files(number: int) -> list[str]:
    """Daftar berkas PR yang LENGKAP — fail-closed.

    `gh pr view --json files` berhenti di 100 berkas (terverifikasi pada PR #55:
    283 berkas, hanya 100 yang dilaporkan). Daftar ini yang menentukan apakah
    berkas pelindung tersentuh, jadi pemotongan itu bisa membuat deteksi buta.
    Karena itu diambil lewat `gh api --paginate` supaya semua halaman ikut.
    """
    code, out, err = _run(files_command(number))
    if code != 0:
        raise ToolError(
            f"daftar berkas PR #{number} tidak bisa dibaca (gh api keluar {code}): "
            f"{(err or out).strip()[:200] or '(kosong)'}\n"
            "  Prompt tidak dicetak tanpa daftar berkas yang lengkap (fail-closed)."
        )
    return sorted({line.strip() for line in out.splitlines() if line.strip()})


def resolve_pr_files(number: int, data: dict) -> list[str]:
    """Daftar berkas PR lengkap + konsistensi dengan `gh pr view` (T-2)."""
    files = fetch_pr_files(number)
    viewed = data.get("files") or []
    if len(viewed) < PR_FILES_VIEW_CAP and len(viewed) != len(files):
        raise ToolError(
            f"daftar berkas PR #{number} tidak konsisten: `gh pr view` melapor "
            f"{len(viewed)} berkas, `gh api --paginate` mengembalikan {len(files)}. "
            "Prompt tidak dicetak (fail-closed)."
        )
    return files


def detect_pr_from_branch() -> int:
    """Deteksi PR yang head-nya branch aktif. Tidak menebak: 0 atau >1 = gagal."""
    code, out, _ = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    branch = out.strip() if code == 0 else ""
    if not branch.startswith("arena/"):
        raise ToolError(
            "tidak ada --pr dan branch aktif bukan `arena/*` "
            f"(branch: {branch or 'tidak terbaca'}).\n"
            "  Tulis nomornya manual: python3 tools/review_prompt.py --pr <NOMOR PR>"
        )
    code, out, err = _run(
        ["gh", "pr", "list", "--state", "open", "--head", branch, "--json", "number", "--limit", "10"]
    )
    if code != 0:
        raise ToolError(
            f"gagal mencari PR untuk branch `{branch}` (gh pr list keluar {code}): "
            f"{(err or out).strip()[:200]}\n"
            "  Tulis nomornya manual: python3 tools/review_prompt.py --pr <NOMOR PR>"
        )
    try:
        rows = json.loads(out or "[]")
    except json.JSONDecodeError as exc:
        raise ToolError(f"jawaban `gh pr list` bukan JSON yang sah: {exc}") from exc
    if len(rows) != 1:
        raise ToolError(
            f"deteksi otomatis gagal: ditemukan {len(rows)} PR terbuka dengan head `{branch}` "
            "(dibutuhkan tepat satu). Nomor PR TIDAK ditebak.\n"
            "  Tulis perintah lengkapnya manual:\n"
            "      python3 tools/review_prompt.py --pr <NOMOR PR>"
        )
    return int(rows[0]["number"])


# --------------------------------------------------------------------------
# Turunan dari pohon kerja (dihitung, tidak ditulis manual)
# --------------------------------------------------------------------------
def sistem_folders() -> list[str]:
    dirs = [p.relative_to(ROOT).as_posix() for p in (ROOT / "sistem").glob("sistem-*") if p.is_dir()]
    if not dirs:
        dirs = [p.name for p in ROOT.glob("sistem-*") if p.is_dir()]
    return sorted(dirs)


def pin_bearing_tools() -> list[str]:
    hits = []
    for path in sorted((ROOT / "tools").glob("*.py")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        if PIN_DEFINITION_RE.search(text):
            hits.append(f"tools/{path.name}")
    return hits


def guarded_sistem_docs() -> list[str]:
    out = []
    for folder in sistem_folders():
        sysdir = ROOT / folder / "_sistem"
        if not sysdir.is_dir():
            continue
        for doc in sorted(sysdir.glob("*.md")):
            if doc.name[:2] in GUARDED_SISTEM_PREFIXES:
                out.append(f"{folder}/_sistem/{doc.name}")
    return out


def production_paths_touched(files: list[str]) -> list[str]:
    return sorted(f for f in files if any(h in f for h in PRODUCTION_DIR_HINTS))


def guarded_inventory(files: list[str]) -> list[tuple[str, bool, str]]:
    """(path, disentuh_PR, alasan) — daftar dihitung, penanda dari diff."""
    touched = set(files)
    rows: list[tuple[str, bool, str]] = []
    for rel in pin_bearing_tools():
        rows.append((rel, rel in touched, "memuat pin regresi"))
    for rel, reason in ARBITER_PATH_REASONS.items():
        if (ROOT / rel).exists():
            rows.append((rel, rel in touched, reason))
    for rel in STATIC_GUARDED_DOCS:
        if (ROOT / rel).exists():
            rows.append((rel, rel in touched, "dokumen mekanisme rilis"))
    for rel in guarded_sistem_docs():
        rows.append((rel, rel in touched, "aturan sistem domain (00/05/06)"))
    for rel in production_paths_touched(files):
        rows.append((rel, True, "state produksi/fixture yang tersentuh PR"))
    seen, uniq = set(), []
    for row in rows:
        if row[0] in seen:
            continue
        seen.add(row[0])
        uniq.append(row)
    return uniq


def arbiter_touched(files: list[str]) -> list[str]:
    touched = set(files)
    hits = [p for p in ARBITER_PATHS if p in touched]
    hits += [p for p in pin_bearing_tools() if p in touched and p not in hits]
    return sorted(hits)


def reading_order(files: list[str]) -> list[str]:
    """Urutan baca: tetap dulu, lalu setiap berkas PR yang perlu dibaca, tanpa kembar."""
    base = [
        "`LOG_SESI_*.md` yang masih berkeadaan `OPEN` (seluruhnya, dari yang terlama)",
        "`_meta/00_CARA_KERJA_META.md`",
        "`_meta/PROTOKOL_REVIEW_INDEPENDEN.md` (seluruhnya)",
    ]
    base_paths = {"_meta/00_CARA_KERJA_META.md", "_meta/PROTOKOL_REVIEW_INDEPENDEN.md"}
    relevan: list[tuple[str, str]] = []
    for rel in files:
        if rel in base_paths:
            continue
        if Path(rel).name.startswith("LOG_SESI_") and rel.endswith(".md"):
            relevan.append((rel, f"`{rel}` — log sesi penulis PR"))
        elif rel.startswith("_meta/") and rel.endswith(".md"):
            relevan.append((rel, f"`{rel}` — disentuh PR"))
        elif rel.startswith("tools/"):
            if (ROOT / rel).exists():
                item = f"`{rel}` — alat yang disentuh PR (baca kodenya, jangan hanya diff-nya)"
            else:
                item = f"`{rel}` — alat yang dihapus PR (baca diff penghapusannya dan rujukan pensiunnya)"
            relevan.append((rel, item))
        elif rel.endswith(".md") and "/" in rel:
            relevan.append((rel, f"`{rel}` — dokumen sistem yang disentuh PR"))
        elif rel.endswith(".md"):
            relevan.append((rel, f"`{rel}` — dokumen root yang disentuh PR"))
    seen, dedup = set(), []
    for rel, item in relevan:
        if rel in seen:
            continue
        seen.add(rel)
        dedup.append(item)
    return base + dedup


LOG_STATUS_RE = re.compile(
    r"^\s*(?:[-*]\s+)?(?:\*\*)?\s*"
    r"(?:Keadaan(?:\s+Sesi)?|Status(?:\s+Sesi)?)"
    r"\s*(?:\*\*)?\s*[:：]\s*(?:\*\*)?\s*`?(OPEN|CLOSED)\b`?",
    re.IGNORECASE,
)


def latest_log_status(lines: list[str]) -> str:
    statuses = [m.group(1).upper() for line in lines if (m := LOG_STATUS_RE.match(line))]
    return statuses[-1] if statuses else "OPEN"


def session_log_files() -> list[Path]:
    """Semua `LOG_SESI_*.md` yang wajib dipindai: root DAN `_log-sesi/`.

    Sebelum 15 Sep 2026 pemindaian hanya `ROOT.glob("LOG_SESI_*.md")`, sehingga
    buta total sejak seluruh log pindah ke `_log-sesi/` — cacat C-1 yang
    ditemukan review independen PR #56 (0 berkas di root, 38 di `_log-sesi/`).
    """
    found: list[Path] = []
    for rel in LOG_SESI_DIRS:
        base = ROOT if rel == "" else ROOT / rel
        found.extend(sorted(base.glob("LOG_SESI_*.md")))
    return found


def log_pointer(log: Path) -> str:
    """Path log relatif terhadap ROOT (pointer SHA+baris butuh path ini)."""
    try:
        return log.relative_to(ROOT).as_posix()
    except ValueError:
        return log.name


def open_test_window(files: list[str] | None = None) -> tuple[list[str], list[str]]:
    """LOG_SESI terbuka yang menyebut jendela uji berjalan.

    Status sesi diambil dari kemunculan OPEN/CLOSED terakhir di seluruh berkas,
    bukan hanya header. Jika tidak ada status yang bisa dibaca, fail-closed:
    log dianggap masih OPEN. Return: (blocking_pointers, writer_log_pointers).
    Log penulis PR sendiri tetap dipointerkan, tetapi tidak memicu
    penyembunyian rumusan acceptance.
    """
    blocking: list[str] = []
    writer_hits: list[str] = []
    # Path PR kini berawalan `_log-sesi/`, jadi penanda log penulis dicocokkan
    # dari NAMA berkas, bukan awalan path (bagian dari cacat C-1).
    writer_logs = {
        f for f in (files or [])
        if Path(f).name.startswith("LOG_SESI_") and f.endswith(".md")
    }
    pattern = re.compile(
        r"jendela uji|jendela run|run acceptance|acceptance run|"
        r"belum dijalankan|sedang berjalan|dijadwalkan, belum",
        re.IGNORECASE,
    )
    for log in session_log_files():
        try:
            lines = log.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        if latest_log_status(lines) != "OPEN":
            continue
        rel = log_pointer(log)
        for idx, line in enumerate(lines, start=1):
            if pattern.search(line):
                ptr = f"{rel}:{idx}"
                if rel in writer_logs:
                    writer_hits.append(ptr)
                else:
                    blocking.append(ptr)
                break
    return blocking, writer_hits


def head_sha_of_worktree() -> str:
    code, out, _ = _run(["git", "rev-parse", "HEAD"])
    return out.strip() if code == 0 else "(tidak terbaca)"


# --------------------------------------------------------------------------
# Render
# --------------------------------------------------------------------------
def render(pr: dict | None, files: list[str], generic: bool) -> tuple[str, list[str]]:
    if generic:
        num, base, head = PLACEHOLDER_PR, PLACEHOLDER_BASE, PLACEHOLDER_HEAD
        title = "<JUDUL PR>"
        base_ref, head_ref = "<BASE REF>", "<HEAD REF>"
        draft_note = ""
    else:
        assert pr is not None
        num = f"#{pr['number']}"
        base, head = pr["baseRefOid"], pr["headRefOid"]
        title = pr.get("title") or "(tanpa judul)"
        base_ref, head_ref = pr["baseRefName"], pr["headRefName"]
        draft_note = "\n> **PR ini berstatus DRAFT** — perlakukan sebagai belum diserahkan.\n" if pr.get("isDraft") else ""

    guarded = guarded_inventory(files)
    arbiter = arbiter_touched(files)
    windows, writer_windows = open_test_window(files if not generic else [])
    pr_ref = num if num.startswith("#") else num
    merge_num = pr["number"] if pr else PLACEHOLDER_PR

    L: list[str] = []
    a = L.append

    a(f"# Prompt Review Independen — PR {pr_ref}")
    a("")
    a(f"> Dibangkitkan `tools/review_prompt.py` dari data PR di GitHub. Semua nomor, sha, dan daftar berkas di bawah")
    a("> berasal dari data itu + isi pohon kerja — bukan dari narasi pihak yang direview.")
    a(draft_note.rstrip("\n") if draft_note else "")
    a("")
    a("## 1. Siapa kamu")
    a("")
    a("Kamu **sesi review independen**. Kamu tidak mengerjakan PR ini, tidak melanjutkannya, dan tidak")
    a("memperbaikinya. Kamu memutuskan.")
    a("")
    a("- Mulai **tanpa konteks** dari sesi mana pun: yang kamu percaya hanya artefak (git tree, commit, log, API).")
    a("- **Read-only** terhadap repo dan terhadap branch orang lain: jangan commit, jangan push, jangan sunting berkas repo.")
    a("- Salinan kerja **hanya di `/tmp`** (mis. `git clone`/`git archive` ke `/tmp/review-<nomor>`); jalankan alat di sana.")
    a("- Klaim penulis PR = **objek pemeriksaan**, bukan bukti.")
    a("")
    a("## 2. Urutan baca (jangan dilewati)")
    a("")
    for i, item in enumerate(reading_order(files), start=1):
        a(f"{i}. {item}")
    a("")
    a("## 3. Objek ter-pin")
    a("")
    a("| Objek | Nilai |")
    a("|---|---|")
    a(f"| PR | {pr_ref} — {title} |")
    a(f"| Base ref | `{base_ref}` |")
    a(f"| Base sha | `{base}` |")
    a(f"| Head ref | `{head_ref}` |")
    a(f"| Head sha | `{head}` |")
    a(f"| Berkas berubah | {len(files)} |")
    a("")
    a("Semua pemeriksaan dilakukan **pada dua sha itu**, bukan pada \"main terbaru\" atau pada branch yang bergerak:")
    a("")
    a("```bash")
    a(f"git diff --stat {base} {head}")
    a(f"git diff --numstat {base} {head}")
    a("```")
    a("")
    a("Berkas yang di-declare berubah oleh data PR:")
    a("")
    if files:
        for rel in files:
            a(f"- `{rel}`")
    else:
        a("- (data PR tidak mencantumkan berkas — itu sendiri temuan; verifikasi lewat `git diff --name-only`)")
    a("")
    a("## 4. Cek standar (semua wajib, semua harus bisa direproduksi)")
    a("")
    a("1. **Kelengkapan vs isi PR** — setiap hal yang dijanjikan body PR benar-benar ada di diff; setiap hal di diff")
    a("   punya penjelasan di body. Selisih dua arah = temuan.")
    a("2. **Append-only** — `git diff --numstat <base> <head>` untuk berkas log/bukti (`LOG_SESI_*.md`,")
    a("   `ACCEPTANCE_TEST_LOG.md`, dokumen bukti): kolom delesi **harus 0** — KECUALI blok header")
    a("   \"Keadaan Sesi\" pada `LOG_SESI_*.md`. Blok itu WAJIB disegarkan saat penutupan sesi (header")
    a("   `OPEN` menjadi `CLOSED`, ringkasan keadaan diperbarui), jadi perubahan baris DI DALAM blok itu")
    a("   SAH dan bukan temuan. Batas blok = awal berkas sampai baris `## Kronologi` (atau penanda setara);")
    a("   perubahan di ATAS batas = wajar bila hanya di blok header; perubahan di BAWAH batas (entri")
    a("   kronologi) = **BLOCKER**. Entri lama yang diedit/dihapus/dihaluskan = **BLOCKER**, bukan catatan")
    a("   kecil. (Penyelarasan 15 Sep 2026: aturan segarkan-header ada di `_meta/TEMPLATE_LOG_SESI.md` dan")
    a("   `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` — tanpa pengecualian ini dua aturan saling mengunci.)")
    a("3. **Klaim luar diverifikasi lewat API** — status PR/rilis/komentar/merge dicek dengan `gh api`, bukan dibaca")
    a("   dari body PR. Kalau body menyebut angka rilis/ID/URL, panggil API-nya sendiri.")
    a("4. **Angka direproduksi sendiri** — setiap angka yang dikutip di bukti (jumlah skenario, jumlah warning, jumlah")
    a("   rujukan, sha) kamu hitung ulang di salinan `/tmp` pada head sha. Angka yang tidak kamu reproduksi = belum diverifikasi.")
    a("5. **Disiplin klaim** — tidak boleh ada gerbang/gate yang dinyatakan tertutup oleh pihak yang tidak berhak")
    a("   menutupnya. Cari kalimat berstatus (\"LULUS\", \"DITUTUP\", \"selesai\", \"terpenuhi\") dan tanyakan: siapa yang")
    a("   menutup, dengan bukti apa, dan apakah dia berwenang.")
    a("6. **Skala** — perubahan apa pun di luar yang dideklarasikan body PR = temuan, sekecil apa pun dan sebaik apa pun niatnya.")
    a("7. **Tidak terverifikasi = MERAH.** Bukan \"kemungkinan besar benar\", bukan \"tampaknya wajar\".")
    a("")
    a("Regresi wajib dijalankan di salinan `/tmp` pada head sha:")
    a("")
    a("```bash")
    a("python3 tools/validate_repo.py          # harus PASS, 0 warning")
    a("python3 tools/test_failure_injection.py # harus PASS; jumlah skenario = _meta/FAILURE_INJECTION_TESTS.md")
    a("```")
    a("")
    a("## 5. Berkas pelindung (dihitung dari pohon + diff, bukan ditulis manual)")
    a("")
    a("Aturan untuk **setiap** berkas di tabel ini: kalau PR menyentuhnya **tanpa declare eksplisit di body → temuan**;")
    a("kalau yang disentuh adalah **pin** → **JANGAN merge, laporkan ke pemilik**.")
    a("")
    a("| Berkas pelindung | Disentuh PR ini? | Kenapa dilindungi |")
    a("|---|---|---|")
    for rel, touched, reason in guarded:
        a(f"| `{rel}` | {'**YA**' if touched else 'tidak'} | {reason} |")
    if not guarded:
        a("| (tidak ada berkas pelindung terdeteksi di pohon ini) | — | — |")
    a("")
    if not generic:
        prod = production_paths_touched(files)
        if prod:
            a("State produksi/fixture yang tersentuh PR ini (perlakukan sebagai bukti hidup, bukan teks bebas):")
            for rel in prod:
                a(f"- `{rel}`")
            a("")
    a("## 6. Aturan keputusan")
    a("")
    a("**Semua cek hijau, tanpa satu pun BLOCKER:**")
    a("")
    a("```bash")
    a(f"gh pr merge {merge_num} --merge")
    a("```")
    a("")
    a("lalu jalankan ulang di `main` terbaru dan **tempel keluaran persisnya** di komentar review:")
    a("")
    a("```bash")
    a("python3 tools/validate_repo.py")
    a("python3 tools/test_failure_injection.py")
    a("```")
    a("")
    a("**Ada satu saja MERAH:** jangan menggabungkan apa pun. Tulis komentar terstruktur:")
    a("")
    a("- **temuan** (satu kalimat, tanpa hedging) → **bukti** (perintah + keluaran + sha/baris) → **perintah perbaikan**")
    a("  (apa yang harus diubah, oleh siapa).")
    a("- Sebut **putaran ke berapa** review ini (maksimal 2 putaran; putaran ke-2 gagal = eskalasi ke pemilik).")
    a("- PR dibiarkan `OPEN`.")
    a("")
    a("**Tidak pernah, dalam keadaan apa pun:** memperbaiki sendiri versi, wording, pin, transkrip, atau isi berkas")
    a("penulis. Reviewer yang menambal temuannya sendiri sudah berhenti jadi reviewer.")
    a("")
    a("## 7. Pengecualian pengadil (baca sebelum menyentuh tombol merge)")
    a("")
    if arbiter:
        a("**BERLAKU untuk PR ini.** PR ini menyentuh alat pengadil:")
        a("")
        for rel in arbiter:
            a(f"- `{rel}`")
        a("")
        a("Karena itu: **JANGAN melakukan merge apa pun**, sekalipun semua cek hijau. Tugasmu berhenti pada")
        a("**melaporkan**. PR yang mengubah alat pengadil tidak boleh dieksekusi oleh pengadil yang diubahnya —")
        a("penggabungan adalah keputusan pemilik langsung.")
    else:
        a("PR ini **tidak** menyentuh alat pengadil eksplisit, berkas pemuat pin, maupun")
        a("protokol review independen, jadi aturan merge normal di bagian 6 berlaku.")
        a("")
        a("Kalau ternyata pemeriksaanmu sendiri menemukan salah satu berkas itu tersentuh (data PR bisa saja basi):")
        a("**berhenti, jangan merge, laporkan** — pengadil tidak mengeksekusi perubahan atas dirinya sendiri.")
    a("")
    a("## 8. Batas publikasi (6d)")
    a("")
    if windows:
        a("**Jendela uji sedang terbuka.** Rumusan acceptance test / prosedur uji sengaja TIDAK dikutip di prompt ini.")
        a("Rujuk lewat pointer, jangan salin isinya ke komentar/log/branch mana pun:")
        a("")
        for ptr in windows:
            a(f"- pointer SHA+baris: `{head}` → `{ptr}`")
    else:
        a("Tidak terdeteksi `LOG_SESI` berkeadaan `OPEN` dari sesi lain yang menyebut jendela uji berjalan. Aturan 6d tetap berlaku:")
        a("kalau kamu menemukan jendela terbuka saat membaca, ganti kutipan rumusan jawaban/kriteria dengan pointer")
        a("SHA+baris di semua artefak yang kamu publikasikan.")
    if writer_windows:
        a("")
        a("Pointer log penulis PR yang tidak memicu penyembunyian (tetap dibaca sebagai konteks, bukan sebagai jendela sesi lain):")
        for ptr in writer_windows:
            a(f"- pointer SHA+baris: `{head}` → `{ptr}`")
    a("")
    if generic:
        a("---")
        a("")
        a(f"jalankan: `python3 tools/review_prompt.py --pr {PLACEHOLDER_PR}` untuk mengisi otomatis")
        a("")
    return "\n".join(line for line in L if line is not None), windows


# --------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="review_prompt.py",
        description="Bangkitkan prompt review independen dari data PR yang nyata.",
    )
    ap.add_argument("--pr", type=int, default=None, help="nomor PR")
    ap.add_argument("--generic", action="store_true", help="cetak versi placeholder (tanpa memanggil GitHub)")
    ap.add_argument("--out", default="-", help="'-' (default, stdout) atau path berkas")
    args = ap.parse_args(argv)

    try:
        if args.generic:
            if args.pr is not None:
                raise ToolError("--generic dan --pr tidak bisa dipakai bersamaan.")
            text, windows = render(None, [], generic=True)
        else:
            number = args.pr if args.pr is not None else detect_pr_from_branch()
            if number <= 0:
                raise ToolError(f"nomor PR tidak masuk akal: {number}")
            data = fetch_pr(number)
            files = resolve_pr_files(number, data)
            text, windows = render(data, files, generic=False)
    except ToolError as exc:
        print(f"review_prompt: GAGAL — {exc}", file=sys.stderr)
        return 2

    if args.out == "-":
        print(text)
    else:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"ditulis: {args.out}", file=sys.stderr)

    if windows:
        print(
            "PERINGATAN: jendela uji terbuka → rumusan hasil disembunyikan "
            f"({len(windows)} pointer SHA+baris dipakai sebagai gantinya)",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
