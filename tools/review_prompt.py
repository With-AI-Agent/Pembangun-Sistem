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
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PLACEHOLDER_PR = "<NOMOR PR>"
PLACEHOLDER_BASE = "<BASE SHA>"
PLACEHOLDER_HEAD = "<HEAD SHA>"
PLACEHOLDER_MERGE_BASE = "<MERGE-BASE SHA>"

# Kuorum hakim default: aturan pemilik 17 Sep 2026 ("Selagi ada yang merah, maka harus diperbaiki")
# dijalankan dengan 3 hakim independen. Dipakai hitung_putaran() untuk memutuskan apakah satu putaran
# masih berjalan; bisa diganti lewat --harapkan N.
KUORUM_HAKIM_DEFAULT = 3

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
    # Alasan di bawah ini DIPIN oleh uji regresi RP1 di tools/test_failure_injection.py
    # (tuple persis ("tools/review_prompt.py", True, "pembangkit prompt pengadil")).
    # 17 Sep 2026: string ini sempat diubah jadi "pembangkit prompt pengadil (kanal PR)"
    # untuk kejelasan, dan RP1 langsung MERAH. Yang dikembalikan adalah SUNTINGANNYA,
    # BUKAN pin-nya — menggeser pin agar cocok dengan suntingan kosmetik akan
    # menghancurkan alasan pin itu ada (mendeteksi perubahan diam-diam pada pengadil).
    "tools/review_prompt.py": "pembangkit prompt pengadil",
    # Ditambahkan 17 Sep 2026: mekanisme AUDIT ISI (kanal non-PR) lahir. Alat dan
    # protokolnya adalah pengadil juga — PR yang mengubahnya tidak boleh dieksekusi
    # oleh pengadil yang diubahnya. Daftar ini SELARAS dengan ARBITER_PATHS di
    # tools/audit_prompt.py; kalau salah satunya bertambah, yang lain WAJIB ikut
    # (dua sumber yang saling menunjuk; ketidaksinkronannya = temuan audit).
    "tools/audit_prompt.py": "pembangkit prompt pengadil (kanal audit isi)",
    "tools/ambil_verdict.py": "pengambil hasil pengadil dari GitHub",
    "_meta/PROTOKOL_AUDIT_ISI.md": "protokol audit isi",
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
        else:
            # Temuan hakim putaran 3 PR #74 (#6): semua cabang di atas hanya menerima `*.md` (plus apa
            # pun di bawah `tools/`), sehingga berkas non-Markdown di LUAR tools/ jatuh DIAM-DIAM dari
            # daftar wajib baca. Terukur pada PR ini: `_meta/_internal/uji/uji_upscaling.py` (skrip
            # pengukuran yang menopang klaim judul PR) dan
            # `sistem/sistem-undangan/_sistem/validate_system.py` (validator mandiri sistem baru) tidak
            # muncul di bagian 2 — 58 dari 60 berkas. Daftar baca yang tidak lengkap membuat hakim
            # merasa sudah membaca semuanya, jadi cabang terakhir ini WAJIB ada: tidak boleh ada berkas
            # yang berubah tanpa masuk daftar.
            relevan.append((rel, f"`{rel}` — berkas non-Markdown yang disentuh PR (baca isinya dan diff-nya)"))
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


def objek_diff(base_sha: str, head_sha: str, ujung_hidup: str | None = None) -> dict:
    """Tiga sha + dua daftar berkas, DIUKUR lokal. Fail-closed: kalau tidak bisa dihitung, katakan.

    Sebab fungsi ini ada (temuan **R3** review independen PR #74): prompt versi lama menyajikan
    `git diff <base sha> <head sha>` sebagai perintah wajib, sementara daftar berkasnya diambil dari
    **diff PR terhadap MERGE-BASE** (`gh api pulls/N/files`). Keduanya **berbeda** begitu base bergerak
    sejak branch dibuat - pada PR #74 reviewer mengukur selisih 4 berkas (53 vs 49 pada head saat
    itu; ANGKA INI HISTORIS dan bergerak setiap kali base/head bergerak, jadi ia SENGAJA TIDAK
    PERNAH dicetak ke prompt - prompt menghitung sendiri lewat `objek_diff()`). Reviewer menghabiskan tenaga
    mencurigai penghapusan bukti yang tidak pernah dilakukan penulis. Yang salah bukan datanya:
    **dua semantik berbeda disajikan sebagai satu objek.**
    """
    hasil: dict = {"merge_base": None, "nama_merge_base": None, "nama_langsung": None,
                   "nama_ujung_hidup": None, "ujung_hidup": None, "kesalahan": []}
    code, out, err = _run(["git", "merge-base", base_sha, head_sha])
    if code != 0 or not out.strip():
        hasil["kesalahan"].append(
            f"merge-base tidak bisa dihitung dari {base_sha[:12]} dan {head_sha[:12]} "
            f"(git keluar {code}): {(err or out).strip()[:200] or '(kosong)'} - "
            "kemungkinan objek tidak ada lokal (repo shallow / belum fetch). "
            "Prompt TIDAK boleh mengklaim selisih yang tidak terukur."
        )
        return hasil
    mb = out.strip()
    hasil["merge_base"] = mb
    for kunci, kiri in (("nama_merge_base", mb), ("nama_langsung", base_sha)):
        c2, o2, e2 = _run(["git", "diff", "--name-only", kiri, head_sha])
        if c2 != 0:
            hasil["kesalahan"].append(
                f"git diff --name-only {kiri[:12]} {head_sha[:12]} gagal (keluar {c2}): "
                f"{(e2 or o2).strip()[:200] or '(kosong)'}"
            )
        else:
            hasil[kunci] = sorted({ln.strip() for ln in o2.splitlines() if ln.strip()})
    # (B-hidup): selisih terhadap UJUNG BASE YANG SEBENARNYA, bukan terhadap base sha beku dari API.
    if ujung_hidup and ujung_hidup != base_sha:
        hasil["ujung_hidup"] = ujung_hidup
        c3, o3, e3 = _run(["git", "diff", "--name-only", ujung_hidup, head_sha])
        if c3 != 0:
            hasil["kesalahan"].append(
                f"objek ujung base terukur {ujung_hidup[:12]} tidak ada lokal, jadi (B-hidup) TIDAK "
                f"terukur (git keluar {c3}: {(e3 or o3).strip()[:160] or '(kosong)'}). Jalankan "
                "`git fetch origin <base ref>` lebih dulu lalu ukur sendiri — prompt ini tidak menebak.")
        else:
            hasil["nama_ujung_hidup"] = sorted({ln.strip() for ln in o3.splitlines() if ln.strip()})
    return hasil


def ujung_base_hidup(base_ref: str, slug: str | None = None) -> dict:
    """Ujung branch base YANG SEBENARNYA saat ini + waktu pengukurannya. Fail-closed.

    **Sebab fungsi ini ada (temuan hakim putaran 3 PR #74, #7).** Prompt mencetak baris
    "**Base sha — ujung base SEKARANG**" dari `.base.sha` API. Nilai itu **BEKU sejak PR dibuat**:
    pada 18 Sep 2026 `main` bergerak ke `26147e1` (PR lain di-merge 13:35Z) sementara `.base.sha`
    PR #74 tetap `c1d00c3`, sehingga prompt menulis "hanya di (B): 0 berkas" padahal selisih terhadap
    ujung `main` yang sebenarnya memuat 11 berkas tambahan. Melabeli nilai beku sebagai "SEKARANG"
    adalah kebalikan dari kenyataan, dan bagian 3a justru dibuat untuk MENAMPAKKAN pergerakan base.
    """
    hasil: dict = {"sha": None, "sumber": None, "waktu_utc": None, "kesalahan": []}
    hasil["waktu_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if not base_ref or base_ref.startswith("<"):
        hasil["kesalahan"].append(
            "base ref tidak terbaca (mode --generic?) — ujung base yang sebenarnya TIDAK DIUKUR")
        return hasil
    code, out, err = _run(["git", "ls-remote", "origin", f"refs/heads/{base_ref}"])
    if code == 0 and out.strip():
        hasil["sha"] = out.split()[0].strip()
        hasil["sumber"] = f"git ls-remote origin refs/heads/{base_ref}"
        return hasil
    slug = slug or repo_slug()
    if slug and "/" in slug and "<" not in slug:
        c2, o2, _ = _run(["gh", "api", f"repos/{slug}/branches/{base_ref}", "--jq", ".commit.sha"])
        if c2 == 0 and o2.strip():
            hasil["sha"] = o2.strip()
            hasil["sumber"] = f"gh api repos/{slug}/branches/{base_ref}"
            return hasil
    hasil["kesalahan"].append(
        f"ujung branch `{base_ref}` tidak terbaca (git ls-remote keluar {code}: "
        f"{(err or '').strip()[:160] or '(kosong)'}) — TIDAK diklaim sama dengan base sha PR")
    return hasil


def baris_ujung_base(base_pr: str, ujung: dict | None) -> tuple[list[str], list[str]]:
    """(baris tabel, peringatan) soal base. MURNI — tidak menyentuh git/jaringan, jadi bisa diuji.

    Tidak pernah melabeli base sha dari API sebagai "sekarang"; kalau ujung yang sebenarnya tidak
    terukur, ia menyatakan itu dan memberi perintah ukurnya (fail-closed), bukan menyamakan keduanya.
    """
    tabel: list[str] = []
    peringatan: list[str] = []
    tabel.append(f"| Base sha yang tercatat di PR (**BEKU sejak PR dibuat** — BUKAN ujung base sekarang) "
                 f"| `{base_pr}` |")
    if not ujung or not ujung.get("sha"):
        alasan = "; ".join((ujung or {}).get("kesalahan") or []) or "tidak terukur"
        tabel.append("| Ujung branch base TERUKUR saat prompt dibangkitkan | **TIDAK TERUKUR** |")
        peringatan.append(f"> **Fail-closed:** ujung branch base yang sebenarnya TIDAK TERUKUR ({alasan}).")
        peringatan.append("> Prompt ini karena itu TIDAK mengklaim base tidak bergerak, dan angka (B) di")
        peringatan.append("> bawah — kalau ada — dihitung terhadap base sha yang beku. Ukur sendiri:")
        peringatan.append("> `git ls-remote origin <base ref>` lalu `git diff --name-only <ujung itu> <head sha>`.")
        return tabel, peringatan
    sha = ujung["sha"]
    waktu = ujung.get("waktu_utc") or "(waktu pengukuran tidak tercatat)"
    sumber = ujung.get("sumber") or "git ls-remote"
    tabel.append(f"| **Ujung branch base TERUKUR** saat prompt dibangkitkan ({waktu}, lewat `{sumber}`) "
                 f"| `{sha}` |")
    if sha == base_pr:
        peringatan.append(f"> Ujung base terukur **sama** dengan base sha yang tercatat di PR (`{sha[:12]}`) pada")
        peringatan.append("> saat prompt ini dibangkitkan. Itu TIDAK menjamin base diam sesudah prompt dibaca:")
        peringatan.append("> ukur ulang (`git ls-remote origin <base ref>`) sebelum menyimpulkan apa pun dari (B).")
    else:
        peringatan.append(f"> **BASE SUDAH BERGERAK** sejak PR dibuat: yang tercatat di PR `{base_pr[:12]}`, ujung")
        peringatan.append(f"> terukur saat prompt dibangkitkan `{sha[:12]}`. Akibatnya diff **(B) yang dicetak prompt")
        peringatan.append("> ini bisa MENGERDILKAN keadaan** — ia dihitung terhadap base sha yang beku. Kalau angka")
        peringatan.append("> '(B-hidup)' ada di bawah, itulah selisih terhadap ujung terukur; kalau tidak ada,")
        peringatan.append("> **wajib ukur sendiri sebelum menyimpulkan:**")
        peringatan.append(f"> `git fetch origin <base ref> && git diff --name-only {sha[:12]} <head sha>`, lalu sebut")
        peringatan.append("> angka pengukuranmu sendiri di verdict — bukan angka prompt ini.")
    return tabel, peringatan


def head_sha_of_worktree() -> str:
    code, out, _ = _run(["git", "rev-parse", "HEAD"])
    return out.strip() if code == 0 else "(tidak terbaca)"


# --------------------------------------------------------------------------
# Render
# --------------------------------------------------------------------------
def repo_slug() -> str:
    """`owner/repo` tempat PR ini hidup, untuk mencetak perintah tempel verdict yang benar.

    Fail-closed ke placeholder: prompt yang mencetak slug karangan lebih berbahaya daripada prompt
    yang menyuruh pembaca mengisinya sendiri.
    """
    code, out, _err = _run(["gh", "repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"])
    slug = (out or "").strip()
    return slug if code == 0 and "/" in slug else "<OWNER>/<REPO>"


def hitung_putaran(data: dict, kuorum: int = KUORUM_HAKIM_DEFAULT, head_sha: str | None = None) -> int:
    """Putaran yang HARUS dinamai prompt — dihitung dari kanal PR. MURNI: tidak menyentuh jaringan.

    **Sebab aturan ini ada (temuan hakim putaran 3 PR #74, #2, P1).** Versi sebelumnya selalu
    mengembalikan `max(putaran yang tertempel) + 1`. Akibatnya begitu SATU hakim putaran 3 menempel
    verdictnya, setiap pembangkitan ulang pada head yang SAMA menamai putaran yang sedang berjalan
    sebagai "putaran 4" — padahal pemilik membuka putaran 3 dan dua hakim lain masih bekerja di bawah
    teks yang menulis "putaran 3". Karena prompt menyuruh hakim menyalin angka itu apa adanya, catatan
    putaran di kanal jadi bercampur.

    Putaran R dinyatakan **MASIH BERJALAN** selama salah satu dari ini benar:
      (a) jumlah slot hakim yang menamai R **kurang dari kuorum** — hakim yang belum menyerahkan
          laporan bukan hakim yang puas; atau
      (b) head PR **belum bergerak** sejak verdict R tertempel (sha head disebut di dalam verdict itu)
          — artinya koreksi belum dibuat, jadi belum ada objek baru untuk diadili.
    Hanya kalau keduanya tidak berlaku, putaran berikutnya = R + 1. Arah kegagalannya sengaja
   konservatif: lebih baik menamai putaran yang sama dua kali daripada melompati satu putaran.
    """
    tools_dir = str(Path(__file__).resolve().parent)
    if tools_dir not in sys.path:
        sys.path.insert(0, tools_dir)
    import ambil_verdict as av                      # definisi "slot hakim" DIPINJAM, bukan diduplikasi

    per_putaran: dict[int, int] = {}
    menyebut_head: set[int] = set()
    pendek = (head_sha or "")[:7]
    for kelompok in ("comments", "reviews"):
        for k in data.get(kelompok) or []:
            teks = (k or {}).get("body") or ""
            if not av.slot_hakim(teks):
                continue
            m = re.search(r"putaran\s+(\d+)", teks, re.I)
            if not m:
                continue
            r = int(m.group(1))
            per_putaran[r] = per_putaran.get(r, 0) + 1
            if pendek and (head_sha in teks or pendek in teks):
                menyebut_head.add(r)
    if not per_putaran:
        return 1
    R = max(per_putaran)
    if per_putaran[R] < max(1, int(kuorum or 1)):
        return R                                    # (a) kuorum putaran R belum lengkap
    if head_sha and R in menyebut_head:
        return R                                    # (b) head belum bergerak sejak verdict R
    return R + 1


def next_round(number: int, kuorum: int = KUORUM_HAKIM_DEFAULT, head_sha: str | None = None) -> int | None:
    """Hitung nomor putaran review BERIKUTNYA dari verdict yang sudah tertempel di kanal PR.

    Sebab: prompt versi lama menyuruh hakim MENEBAK ("ganti `putaran 1` dengan angka putaran yang
    sebenarnya") dan menyebut "maksimal 2 putaran" sebagai fakta tetap. Keduanya salah begitu pemilik
    membuka putaran tambahan (18 Sep 2026: PR #74 putaran 3 dibuka pemilik sesudah 13 temuan gabungan
    putaran 2 ditutup). Nomor putaran adalah DATA yang ada di kanal, jadi dihitung di sini — dan
    definisi "slot hakim" DIPINJAM dari `ambil_verdict.py` supaya tidak ada dua definisi yang bisa
    saling bertentangan.

    Fail-closed: kalau kanal tidak terbaca, kembalikan None. Prompt lalu menyuruh hakim menghitung
    sendiri secara eksplisit dan TIDAK mencetak angka yang bisa salah.
    """
    tools_dir = str(Path(__file__).resolve().parent)
    if tools_dir not in sys.path:
        sys.path.insert(0, tools_dir)
    try:
        import ambil_verdict as av
        data = av.ambil_pr(number)
    except Exception:
        return None
    return hitung_putaran(data, kuorum, head_sha)


def render(pr: dict | None, files: list[str], generic: bool,
           objek: dict | None = None,
           putaran: int | None = None,
           ujung_base: dict | None = None) -> tuple[str, list[str]]:
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
    # R3: tiga sha, bukan dua. Merge-base = titik branch dibuat; base sha yang TERCATAT DI PR beku
    # sejak PR dibuat, dan ujung base yang SEBENARNYA diukur terpisah lewat ujung_base_hidup()
    # (temuan #7 hakim putaran 3: melabeli nilai beku sebagai "SEKARANG" adalah kebalikan kenyataan).
    if generic:
        mb = PLACEHOLDER_MERGE_BASE
        daftar_a: list[str] | None = None
        daftar_b: list[str] | None = None
        daftar_hidup: list[str] | None = None
        err_objek = ["mode --generic: tidak ada PR, jadi merge-base dan selisihnya tidak bisa diukur"]
    else:
        objek = objek or {}
        mb = objek.get("merge_base") or "TIDAK TERHITUNG"
        daftar_a = objek.get("nama_merge_base")
        daftar_b = objek.get("nama_langsung")
        daftar_hidup = objek.get("nama_ujung_hidup")
        err_objek = list(objek.get("kesalahan") or [])

    a("## 3. Objek ter-pin")
    a("")
    a("| Objek | Nilai |")
    a("|---|---|")
    a(f"| PR | {pr_ref} — {title} |")
    a(f"| Base ref | `{base_ref}` |")
    _tabel_base, _peringatan_base = baris_ujung_base(base, ujung_base)
    for _b in _tabel_base:
        a(_b)
    a(f"| **Merge-base sha — titik branch ini dibuat** | `{mb}` |")
    a(f"| Head ref | `{head_ref}` |")
    a(f"| **Head sha — OBJEK YANG HENDAK DIPUTUSKAN** | `{head}` |")
    a(f"| Berkas menurut data PR (semantik merge-base) | {len(files)} |")
    a("")
    for _p in _peringatan_base:
        a(_p)
    a("")
    a("**Verdict wajib menyebut head sha di atas.** Head bisa bergerak selama review berjalan; verdict")
    a("yang tidak menyebut sha tidak bisa dipetakan ke keadaan mana pun dan diperlakukan sebagai belum")
    a('terverifikasi (protokol review independen, bagian "Beberapa hakim sekaligus").')
    a("")
    a("### 3a. Dua diff yang BERBEDA — jangan ditukar")
    a("")
    a("**Sebab bagian ini ada:** prompt versi lama menyajikan `git diff <base sha> <head sha>` sebagai")
    a("perintah wajib, sementara daftar berkasnya berasal dari **diff PR terhadap merge-base**. Keduanya")
    a("**berbeda** begitu base bergerak sejak branch dibuat. Selisihnya **DIHITUNG dan DICETAK di bawah** —")
    a("prompt ini sengaja TIDAK mengutip angka dari PR mana pun, karena angka yang dibekukan di kode akan")
    a("membantah pengukurannya sendiri begitu base atau head bergerak (itu terjadi, dan jadi temuan review).")
    a("")
    a("```bash")
    a("# (A) PERUBAHAN YANG DIPERKENALKAN PR — semantik daftar berkas di bagian 3b. PAKAI INI untuk menilai isi PR.")
    a(f"git diff --stat {mb} {head}")
    a(f"git diff --numstat {mb} {head}")
    a("")
    a("# (B) SELISIH LANGSUNG ujung base ke head — IKUT memuat perubahan yang masuk ke base SESUDAH branch dibuat.")
    a(f"git diff --stat {base} {head}")
    a("```")
    a("")
    a("**Aturan pakai:** cek *kelengkapan vs isi PR* dan *append-only* dilakukan pada **(A)**. Kalau kamu")
    a("memakai (B) lalu menemukan delesi pada berkas yang tidak ada di (A), itu **BUKAN penghapusan oleh")
    a("penulis PR** — itu base yang bergerak. **Nyatakan di verdict-mu diff mana yang kamu pakai.**")
    a("")
    if err_objek:
        a("**Yang TIDAK bisa diukur, dinyatakan (fail-closed — jangan disimpulkan sendiri):**")
        a("")
        for e in err_objek:
            a(f"- {e}")
        a("")
    if daftar_a is not None and daftar_b is not None:
        hanya_b = [x for x in daftar_b if x not in set(daftar_a)]
        hanya_a = [x for x in daftar_a if x not in set(daftar_b)]
        a(f"**Selisih terukur (A) vs (B) — angka, bukan perkiraan, diukur saat prompt dibangkitkan:**")
        a(f"(A) {len(daftar_a)} berkas, (B) {len(daftar_b)} berkas — (B) dihitung terhadap base sha yang")
        a("**tercatat di PR (beku)**, bukan terhadap ujung branch base yang sebenarnya.")
        a("")
        if daftar_hidup is not None:
            hanya_hidup = [x for x in daftar_hidup if x not in set(daftar_a)]
            a(f"**(B-hidup) terhadap ujung base TERUKUR `{(objek or {}).get('ujung_hidup', '')[:12]}`: "
              f"{len(daftar_hidup)} berkas, {len(hanya_hidup)} di antaranya hanya ada di (B-hidup)** —")
            a("inilah selisih yang sesungguhnya kalau base sudah bergerak. Sebut angka ini (atau hasil")
            a("pengukuranmu sendiri) di verdict, dan JANGAN memakai '0 berkas hanya di (B)' dari prompt")
            a("versi lama sebagai fakta.")
            for rel in hanya_hidup[:15]:
                a(f"  - `{rel}`")
            if len(hanya_hidup) > 15:
                a(f"  - … dan {len(hanya_hidup) - 15} berkas lagi (ukur sendiri untuk daftar lengkap)")
            a("")
        a(f"- **hanya di (B), jadi BUKAN perubahan PR ini: {len(hanya_b)} berkas**"
          + (" — berkas-berkas ini masuk ke base SESUDAH branch ini dibuat" if hanya_b else ""))
        for rel in hanya_b[:15]:
            a(f"  - `{rel}`")
        if len(hanya_b) > 15:
            a(f"  - … dan {len(hanya_b) - 15} lainnya")
        a(f"- hanya di (A): {len(hanya_a)} berkas")
        for rel in hanya_a[:15]:
            a(f"  - `{rel}`")
        a("")
        sama = "SAMA" if sorted(files) == daftar_a else "BERBEDA"
        a(f"**Konsistensi daftar:** data PR lewat API menyebut **{len(files)}** berkas; diff lokal (A)")
        a(f"menyebut **{len(daftar_a)}** berkas → **{sama}**."
          + ("" if sama == "SAMA" else
             " Selisihnya wajib dinyatakan di verdict, jangan dipilih salah satu diam-diam."))
        a("")
    a("### 3b. Berkas yang di-declare berubah oleh data PR (semantik diff A)")
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
    a("2. **Append-only** — `git diff --numstat <merge-base> <head>` (diff **A**, lihat bagian 3a) untuk")
    a("   berkas log/bukti (`LOG_SESI_*.md`,")
    a("   `ACCEPTANCE_TEST_LOG.md`, dokumen bukti): kolom delesi **harus 0** — KECUALI blok header")
    a("   \"Keadaan Sesi\" pada `LOG_SESI_*.md`. Blok itu WAJIB disegarkan saat penutupan sesi (header")
    a("   `OPEN` menjadi `CLOSED`, ringkasan keadaan diperbarui), jadi perubahan baris DI DALAM blok itu")
    a("   SAH dan bukan temuan. Batas blok = awal berkas sampai baris `## Kronologi` (atau penanda setara);")
    a("   perubahan di ATAS batas = wajar bila hanya di blok header; perubahan di BAWAH batas (entri")
    a("   kronologi) = **BLOCKER**. Entri lama yang diedit/dihapus/dihaluskan = **BLOCKER**, bukan catatan")
    a("   kecil. (Penyelarasan 15 Sep 2026: aturan segarkan-header ada di `_meta/TEMPLATE_LOG_SESI.md` dan")
    a("   `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` — tanpa pengecualian ini dua aturan saling mengunci.)")
    a("   Pengecualian redaksi 6d: delesi/edit di bawah batas `## Kronologi` adalah SAH (bukan BLOCKER) jika")
    a("   dan hanya jika 4 syarat ini terpenuhi: (i) dideklarasikan di body PR per berkas + nomor baris persis;")
    a("   (ii) pola edit = penggantian pemetaan run/sisi/verdict/state-fixture menjadi pointer netral (pola 6d;")
    a("   preseden: ACCEPTANCE_TEST_LOG.md \"Sanitasi 6 Sep\" + Rencana re-run); (iii) fakta proses yang bukan")
    a("   pola tersebut dipertahankan byte-exact; (iv) otorisasi pemilik tercatat di body PR + log sesi penulis.")
    a("   Artefak newline-EOF: \"delesi\" teks yang byte-identik yang terjadi semata karena baris terakhir berkas")
    a("   tidak punya newline pengakhir (append memberikannya) BUKAN delesi konten dan bukan temuan; syarat")
    a("   \"kolom delesi = 0\" diukur atas konten entri kronologi.")
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
    a("python3 tools/validate_repo.py          # harus PASS; baris 'WARNINGS: N' dikutip apa adanya")
    a("#   warning tier HANYA sah untuk berkas bukti historis yang append-only (keputusan pemilik")
    a("#   18 Sep 2026: riwayat tidak disunting demi kosmetika tabel). Warning di dokumen HIDUP")
    a("#   = MERAH. Syarat lama (lulus tanpa satu pun peringatan) dilaporkan tidak terukur oleh")
    a("#   hakim putaran 4, lalu dicabut penulis PR atas izin pemilik (giliran 22) berdasar warning")
    a("#   tier keputusan pemilik 18 Sep 2026 - hakim melaporkan, pemilik memutuskan, penulis")
    a("#   melaksanakan. (Atribusi ini dibetulkan 19 Sep 2026, temuan #2 hakim putaran 5.)")
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
    if arbiter:
        a("**PERHATIAN — PR INI MENYENTUH ALAT PENGADIL: perintah merge di bagian ini DIGANTI LARANGAN.**")
        a("Rinciannya di bagian 7. Ringkasnya: **`gh pr merge` DILARANG untuk PR ini, sekalipun semua cek")
        a("hijau** — pengadil tidak mengeksekusi perubahan atas dirinya sendiri, jadi penggabungan adalah")
        a("keputusan pemilik langsung. Tugasmu berhenti pada **melaporkan**.")
        a("")
        a("**Semua cek hijau, tanpa satu pun BLOCKER:** JANGAN merge. Jalankan ulang dua alat ini di `main`")
        a("terbaru, **tempel keluaran persisnya** di komentar verdict-mu, dan tulis verdict **HIJAU** dengan")
        a("format bagian 6a:")
        a("")
        a("```bash")
        a("python3 tools/validate_repo.py")
        a("python3 tools/test_failure_injection.py")
        a("```")
    else:
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
    if putaran:
        a(f"- Review ini **putaran {putaran}** — angkanya DIHITUNG alat dari verdict yang sudah tertempel di")
        a("  kanal PR ini (definisi slot hakim dipinjam dari `ambil_verdict.py`), bukan ditebak. Aturan default:")
        a("  maksimal 2 putaran lalu eskalasi ke pemilik; **pemilik boleh membuka putaran tambahan secara")
        a("  eksplisit** (preseden 18 Sep 2026, PR #74: 13 temuan putaran 2 ditutup lebih dulu, lalu pemilik")
        a("  memutuskan membuka putaran 3).")
    else:
        a("- Sebut **putaran ke berapa** review ini — HITUNG dari verdict yang sudah tertempel di kanal PR,")
        a("  jangan menebak. Aturan default: maksimal 2 putaran lalu eskalasi ke pemilik; pemilik boleh")
        a("  membuka putaran tambahan secara eksplisit (aturan 7 protokol).")
    a("- PR dibiarkan `OPEN`.")
    a("")
    a("## 6a. Format komentar verdict — WAJIB persis, karena dibaca ALAT bukan manusia")
    a("")
    a(f"Verdict-mu dikumpulkan pemilik dengan `python3 tools/ambil_verdict.py --pr {merge_num} --harapkan 3`.")
    a("Alat itu **tidak membaca prosa**: keputusan diambil dari **BARIS BERPARKAH PERTAMA** (judul Markdown,")
    a("atau baris diawali `-`/`*`/`>` lalu `**VERDICT:**`) dan hanya kata putusan tertentu yang dihitung.")
    a("Kalau formatmu melenceng sedikit saja, komentarmu **tidak terhitung sebagai slot hakim** dan kuorum")
    a("gagal **diam-diam**: tidak ada pesan error, PR hanya terbaca kekurangan hakim. **Batas klaim (preseden")
    a("di repo ini, BUKAN diagnosis PR yang sedang kamu hadapi):** pada satu PR, dua verdict putaran pertama")
    a("**tidak pernah ditempel sama sekali** — itu modus kegagalan yang BERBEDA dan tidak disembuhkan oleh format.")
    a("Yang disembuhkan format adalah verdict yang **sudah ditulis tetapi tidak terbaca** oleh alat. Periksa kanal")
    a("PR INI untuk tahu mana yang sedang terjadi; **jangan mewarisi diagnosis PR lain** (prompt ini pernah")
    a("membekukan angka dan riwayat satu PR sehingga tercetak untuk semua PR — itu temuan review, sudah ditutup).")
    a("")
    a("**Baris PERTAMA komentar PR-mu harus persis berbentuk ini** (satu baris, TANPA pagar kode):")
    a("")
    if putaran:
        a(f"## Review independen PR #{merge_num} — putaran {putaran} — VERDICT: MERAH")
        a("")
        a(f"**Angka putaran {putaran} di atas DIHITUNG ALAT** dari verdict yang sudah tertempel di kanal PR ini —")
        a("**salin apa adanya, jangan diubah.** Untuk putusan hijau, ganti kata `MERAH` dengan `HIJAU`.")
    else:
        a(f"## Review independen PR #{merge_num} — putaran 1 — VERDICT: MERAH")
        a("")
        a("**Ganti `putaran 1` dengan angka putaran yang sebenarnya** — jangan disalin mentah. Kanal PR tidak")
        a("terbaca saat prompt ini dibangkitkan, jadi **hitung sendiri**: buka daftar komentar PR, cari verdict")
        a("hakim yang sudah tertempel, pakai angka berikutnya. Untuk putusan hijau, ganti `MERAH` jadi `HIJAU`.")
    a("Lalu di")
    a("badan komentar, tulis sekali lagi sebagai baris berpemarkah:")
    a("")
    a("- **VERDICT:** MERAH — jangan merge; jumlah temuan: N (lalu uraikan satu per satu di bawahnya)")
    a("")
    a("**Cara menempelkannya — dan ini WAJIB ditempel, bukan disimpan di sesi.** Pada satu putaran")
    a("sebelumnya di repo ini, dua dari tiga verdict **tidak pernah sampai ke GitHub** dan kuorum gagal")
    a("tanpa pesan error; kerjanya hilang karena tidak ada yang menempel. Pakai jalur REST:")
    a("")
    a("```bash")
    a("# 1) tulis verdictmu ke berkas, lalu bungkus jadi JSON dengan satu kunci bernama body")
    a(f"# 2) tempel sebagai komentar PR (slug repo ini: {repo_slug()})")
    a(f"gh api repos/{repo_slug()}/issues/{merge_num}/comments --input /tmp/verdict.json")
    a("# 3) VERIFIKASI tertempel — WAJIB, jangan mengandalkan exit code:")
    a(f"gh api repos/{repo_slug()}/issues/{merge_num}/comments --jq '.[-1] | .body[0:90]'")
    a("```")
    a("")
    a(f"`gh pr comment {merge_num}` **jangan diandalkan di lingkungan seperti ini**: keluarga perintah")
    a("`gh pr` memakai GraphQL, dan `gh pr edit` terukur GAGAL di repo ini (field `projectCards` sudah")
    a("didepresiasi) dengan gejala menipu — perintah keluar membawa pesan, tetapi body **tidak berubah**.")
    a("Kalau perintahmu keluar dengan pesan galat atau keluar tanpa efek, **baca ulang dari API** sebelum")
    a("menyimpulkan berhasil.")
    a("")
    a("**Syarat keras — semuanya diukur dari alatnya, bukan selera:**")
    a("")
    a("1. Baris pertama **harus judul Markdown** (diawali `#`) dan **harus memuat** salah satu kata putusan:")
    a("   `MERAH`, `HIJAU`, `BERSIH`, `ADA TEMUAN`, `TIDAK BISA DISIMPULKAN`, `APPROVE`, `REQUEST_CHANGES`.")
    a("   Menyertakan `review independen` + `putaran N` di baris yang sama membuat penggolongan slot kokoh.")
    a("2. Baris pertama **TIDAK BOLEH memuat** kata `penulis`, `koreksi terbuka`, atau `tanggapan penulis` —")
    a("   alat menggolongkan baris semacam itu sebagai komentar penulis PR dan **membuangnya** dari kuorum.")
    a("3. **JANGAN menaruh baris judul atau baris VERDICT di dalam pagar kode**: alat mengosongkan isi pagar")
    a("   kode lebih dulu, jadi verdict di dalamnya tidak terbaca. Contoh di atas sengaja tidak dipagari —")
    a("   salin sebagai teks biasa.")
    a("4. Kata putusan di dalam **prosa tidak dihitung**; hanya baris berpemarkah yang dibaca.")
    a("5. Fail-closed: kalau kamu tidak bisa menyimpulkan, tulis `TIDAK BISA DISIMPULKAN` — itu **menahan**")
    a("   merge, dan memang begitu seharusnya. Jangan mengosongkan verdict, jangan menutup sesi tanpa komentar.")
    a("6. **Jangan mengutip prompt ini ke dalam komentar PR.** Contoh judul di atas adalah teks hidup: kalau")
    a("   ikut tersalin, alat bisa membacanya sebagai verdict dan kuorum jadi palsu.")
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
# RP12 (18 Sep 2026): BLOK SERAH TERIMA — path absolut + link, DICETAK ALAT, bukan ditulis tangan.
# Sebab (aturan tetap pemilik, giliran 19): "Setiap menyiapkan review independen dan pemeriksaan
# menyeluruh independen, agent harus beri link nya." Sebelumnya prompt diserahkan dengan menyebut
# nama berkas saja; pemilik — yang menyatakan tidak punya basic coding — harus mencari sendiri
# berkasnya dan bingung. Link yang ditulis tangan bisa salah atau ketinggalan: itu kelas cacat yang
# sama dengan angka beku yang ditutup RP9/RP10, jadi link DIRANGKAI DARI DATA TERUKUR dan alatnya
# sendiri yang meneriakkannya ke stderr supaya agent tidak bisa "lupa".
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# T-48 (18 Sep 2026): link ke BERKAS PROMPT ITU SENDIRI, bukan hanya link ke PR.
# Koreksi pemilik giliran 20: *"Apakah kamu paham bahwa yang aku maksud adalah link ke file prompt
# perintah untuk sesi hakim dan reviewer/pemeriksa nya? Bukan hanya file PR nya."* Path di mesin kerja
# agent (`/home/user/...`) tidak bisa dibuka pemilik, dan tidak bisa dibuka teman yang membuka sesi
# hakim — jadi yang dibutuhkan adalah URL. Prompt ditempel ke kanal PR sebagai KOMENTAR PENULIS dan
# permalink-nya dicetak di blok serah terima.
# --------------------------------------------------------------------------
def bangun_komentar_pengumuman(teks_prompt: str, number: int | None = None,
                               head_sha: str | None = None, out_path: str | None = None) -> str:
    """Badan komentar PR yang memuat prompt, berlabel KOMENTAR PENULIS (bukan verdict).

    Dua pengaman, keduanya TERUKUR (bukan diasumsikan):
      1. baris judul menyebut `penulis` — `slot_hakim()` di `ambil_verdict.py` memeriksa `PENULIS_RE`
         LEBIH DULU daripada token laporan, jadi komentar ini tidak pernah jadi slot hakim;
      2. seluruh prompt dipagari pagar backtick yang LEBIH PANJANG dari pagar terpanjang di dalam
         prompt, dan `strip_code_fences()` mengosongkan isi pagar sebelum penggolongan (terbukti juga
         untuk pagar 4-backtick), sehingga contoh judul verdict di dalam prompt tidak terbaca.
    """
    runs = re.findall(r"`+", teks_prompt or "")
    pagar = "`" * max(4, max((len(r) for r in runs), default=0) + 1)
    b: list[str] = []
    a = b.append
    a("## Komentar penulis PR — BUKAN verdict: prompt review independen siap salin")
    a("")
    a("Komentar ini dari **penulis PR** (agent yang pekerjaannya sedang dinilai), ditempel oleh")
    a("`tools/review_prompt.py --umumkan` atas aturan tetap pemilik 18 Sep 2026: *setiap menyiapkan")
    a("review independen atau pemeriksaan menyeluruh independen, agent wajib menyerahkan path berkas")
    a("DAN link-nya* — dan yang dimaksud pemilik (koreksi giliran 20) adalah **link ke berkas prompt")
    a("itu sendiri**, bukan hanya link ke PR, supaya siapa pun yang membuka sesi hakim bisa membuka")
    a("dan menyalin teksnya tanpa perlu akses ke mesin kerja agent.")
    a("")
    a("**Ini BUKAN verdict dan BUKAN laporan review.** `tools/ambil_verdict.py` menggolongkannya")
    a("sebagai komentar penulis karena baris judul di atas menyebut `penulis` (diperiksa lebih dulu")
    a("daripada token laporan), dan seluruh isi prompt dipagari sehingga contoh judul verdict di")
    a("dalamnya tidak bisa terbaca sebagai verdict. Kalau penggolongan itu gagal, alat **menghapus")
    a("komentar ini lagi** dan tidak mencetak link (fail-closed).")
    a("")
    if number and number > 0:
        a(f"- PR: #{number}")
    if head_sha:
        a(f"- Prompt ini pin ke head `{head_sha}`. Kalau head PR sudah bergerak, prompt ini **BASI** —")
        a("  bangkitkan ulang, jangan dipakai.")
    if out_path:
        a(f"- Berkas di mesin kerja agent: `{Path(out_path).resolve()}` (tidak bisa dibuka orang lain —")
        a("  itu sebabnya link ini ada)")
    a("- Bangkitkan ulang: `python3 tools/review_prompt.py --pr "
      f"{number if number and number > 0 else '<N>'} --out <path> --umumkan`")
    a("")
    a("**Cara memakai:** buka sesi hakim baru, lalu salin SELURUH isi di dalam pagar di bawah ini")
    a("(tanpa ikut pagarnya) sebagai satu pesan.")
    a("")
    a(pagar)
    a((teks_prompt or "").rstrip("\n"))
    a(pagar)
    a("")
    return "\n".join(b) + "\n"


def umumkan_prompt(number: int, teks_prompt: str, slug: str | None = None,
                   head_sha: str | None = None, out_path: str | None = None):
    """Tempel prompt ke kanal PR sebagai komentar penulis; kembalikan (permalink, catatan).

    Fail-closed tiga lapis — lebih baik tidak ada link daripada link palsu atau kuorum palsu:
      1. slug repo tak terbaca            -> tidak menempel, tidak mencetak link;
      2. POST gagal / respons tak terbaca -> tidak mencetak link;
      3. komentar TETAP terbaca sebagai slot hakim oleh `ambil_verdict.slot_hakim()` -> DIHAPUS lagi.
    """
    if slug is None:
        slug = repo_slug()
    if not slug or "/" not in slug or "<" in slug:
        return None, f"slug repo tidak terbaca ({slug!r}) — prompt tidak ditempel, link tidak dicetak"
    badan = bangun_komentar_pengumuman(teks_prompt, number, head_sha, out_path)
    r = subprocess.run(
        ["gh", "api", "-X", "POST", f"repos/{slug}/issues/{number}/comments", "--input", "-"],
        input=json.dumps({"body": badan}), capture_output=True, text=True)
    if r.returncode != 0:
        return None, f"POST komentar gagal: {((r.stderr or r.stdout) or '').strip()[:200]}"
    try:
        data = json.loads(r.stdout)
        url, cid = data.get("html_url"), data.get("id")
    except Exception as exc:
        return None, f"respons POST tidak terbaca sebagai JSON ({exc}) — link tidak dicetak"
    if not url or not cid:
        return None, "respons POST tidak memuat html_url/id — link tidak dicetak"
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import ambil_verdict as av
        terbaca_slot = bool(av.slot_hakim(badan))
    except Exception as exc:
        subprocess.run(["gh", "api", "-X", "DELETE", f"repos/{slug}/issues/comments/{cid}"],
                       capture_output=True, text=True)
        return None, f"verifikasi penggolongan gagal ({exc}) — komentar DIHAPUS lagi (fail-closed)"
    if terbaca_slot:
        subprocess.run(["gh", "api", "-X", "DELETE", f"repos/{slug}/issues/comments/{cid}"],
                       capture_output=True, text=True)
        return None, ("komentar TERBACA sebagai slot hakim oleh ambil_verdict.slot_hakim() — "
                      "DIHAPUS lagi supaya kuorum tidak palsu")
    return url, "tertempel dan terverifikasi BUKAN slot hakim"


def verifikasi_berkas_prompt(path) -> str:
    """RP18: klaim "berkas prompt ada" wajib DIUKUR sesudah ditulis, bukan diasumsikan dari argumen.

    Mengembalikan satu baris verifikasi untuk ditempel ke akhir berkas oleh pemanggil. Fail-closed:
    kalau berkasnya tidak ada, barisnya menyatakan GAGAL — bukan diam, dan bukan klaim sukses.
    Cacat yang ditutup: `handoff_block()` pernah mencetak "TIDAK ditulis ke berkas" padahal
    berkasnya ditulis (temuan #1 hakim C putaran 5 PR #74) — pernyataan palsu di alat pengadil,
    tepat di blok yang menjalankan aturan tetap pemilik "serahkan path + link".
    """
    p = Path(path).resolve()
    if not p.exists():
        return ("- **Verifikasi sesudah ditulis:** GAGAL — berkas TIDAK ADA di disk sesudah "
                "penulisan. Jangan serahkan path ini ke pemilik; periksa alatnya.")
    ukuran = p.stat().st_size
    baris = len(p.read_text(encoding="utf-8").splitlines())
    return (f"- **Verifikasi sesudah ditulis (diukur, bukan diklaim):** berkas ADA di disk — "
            f"{ukuran:,} byte / {baris:,} baris, diukur sesudah penulisan dan sebelum baris "
            f"verifikasi ini ditambahkan.")


def handoff_block(number: int | None = None, head_sha: str | None = None,
                  out_path: str | None = None, slug: str | None = None,
                  objek: str | None = None,
                  jenis: str = "review independen",
                  permalink: str | None = None) -> str:
    """Blok serah terima untuk PEMILIK: di mana berkasnya, dan link apa saja yang bisa diklik.

    Fail-closed: kalau slug repo atau sha head tidak terbaca, blok ini TIDAK mencetak link karangan.
    Link palsu lebih berbahaya daripada tidak ada link — pemilik akan mengkliknya dan mendapat 404,
    lalu kehilangan kepercayaan pada semua link berikutnya.
    """
    if slug is None:
        slug = repo_slug()
    slug_ok = bool(slug) and "/" in slug and "<" not in slug
    sha_ok = bool(head_sha) and len(head_sha or "") >= 7 and "<" not in (head_sha or "")
    b: list[str] = []
    a = b.append
    a("")
    a("---")
    a("")
    a("## BLOK SERAH TERIMA — untuk pemilik dan agent yang menyiapkan; BUKAN bagian tugas hakim")
    a("")
    a("Hakim/auditor boleh melewati bagian ini. Ia ada karena pemilik menetapkan aturan tetap")
    a("(18 Sep 2026): *setiap menyiapkan review independen atau pemeriksaan menyeluruh")
    a("independen, agent wajib menyerahkan path berkas DAN link-nya*, bukan hanya nama berkas.")
    a(f"Yang diserahkan kali ini: **{jenis}**.")
    a("")
    _akar = Path(__file__).resolve().parent.parent   # root repo, BUKAN folder kerja sekarang
    if out_path:
        p = Path(out_path).resolve()
        a(f"- **Berkas prompt (path absolut — salin persis):** `{p}`")
        a(f"- **Nama berkas:** `{p.name}` · **di dalam folder:** `{p.parent}`")
        # RP18 (temuan #1 hakim C putaran 5 PR #74): blok ini dirangkai SEBELUM alat menulis
        # berkas, jadi ia tidak boleh mengklaim keberadaan berkas. Yang diklaim di sini hanya
        # path tujuannya; keberadaannya DIUKUR sesudah penulisan dan ditempel ke akhir berkas
        # oleh pemanggil (lihat `verifikasi_berkas_prompt`).
        # RP21 (ditemukan sendiri 19 Sep 2026 saat membangkitkan ulang prompt putaran 6 PR #74):
        # cabang lama `if p.exists(): "ADA di disk, N byte"` MENGUKUR SEBELUM MENULIS. Ketika path
        # tujuan masih berisi berkas dari pembangkitan sebelumnya, angka yang tercetak adalah ukuran
        # berkas LAMA — lalu berkas itu ditimpa, sehingga angka yang diserahkan ke pemilik tidak sama
        # dengan berkas yang diserahkan (terukur: blok mencetak 27.678 byte, `ls -l` hasil penulisan
        # 27.598 byte). Blok ini dirangkai sebelum penulisan, jadi ia TIDAK BOLEH mengklaim ukuran
        # sama sekali; klaim yang benar hanya ada di baris verifikasi yang ditempel SESUDAH penulisan
        # (`verifikasi_berkas_prompt`). Keberadaan berkas lama dinyatakan apa adanya: akan ditimpa.
        a("- **Verifikasi berkas:** diukur SESUDAH alat menulisnya — baris verifikasi terukur")
        a("  ditambahkan alat ke akhir berkas. Blok ini dirangkai sebelum penulisan, jadi ia")
        a("  tidak boleh mendahului pengukuran; periksa dengan `ls -l` sesudah alat selesai.")
        if p.exists():
            a(f"- **Berkas lama akan DITIMPA:** `{p.name}` sudah ada di path itu sebelum penulisan,")
            a("  dan ukuran apa pun pada berkas lama BUKAN ukuran berkas yang diserahkan — alat ini")
            a("  sengaja tidak mencetak angka yang diukur sebelum berkasnya ditulis (RP21).")
    else:
        a("- **Berkas prompt:** TIDAK ditulis ke berkas (keluar ke stdout). Jalankan ulang dengan")
        a("  `--out <path>` supaya ada berkas yang bisa diberi path dan link.")
    if permalink:
        a(f"- **LINK KE PROMPT INI (tahan lama, bisa dibuka siapa pun):** {permalink}")
        a("  Komentar **penulis PR**, BUKAN verdict: alat pengumpul verdict menggolongkannya"
          " sebagai komentar penulis dan isinya dipagari, jadi contoh judul verdict di dalamnya"
          " tidak bisa terbaca. Ini link yang diserahkan ke pemilik dan ke siapa pun yang"
          " membuka sesi hakim — path di atas hanya ada di mesin kerja agent.")
    if objek:
        a(f"- **Objek yang diperiksa:** `{objek}` (relatif dari root repo)")
        if slug_ok and sha_ok:
            _o = _akar / objek
            if _o.exists():
                _macam = "tree" if _o.is_dir() else "blob"
                a(f"- **Objek itu pada sha yang di-pin:** "
                  f"https://github.com/{slug}/{_macam}/{head_sha}/{objek}")
            else:
                a(f"- **Objek itu pada sha yang di-pin:** TIDAK DICETAK — `{objek}` tidak ditemukan")
                a("  di root repo. Link karangan lebih buruk daripada tidak ada link.")
    if number and number > 0 and slug_ok:
        a(f"- **PR yang dinilai:** https://github.com/{slug}/pull/{number}")
        a(f"- **Daftar berkas yang berubah:** https://github.com/{slug}/pull/{number}/files")
        if sha_ok:
            a(f"- **Head yang di-pin (permalink permanen):** https://github.com/{slug}/commit/{head_sha}")
            a(f"- **Isi repo pada head itu:** https://github.com/{slug}/tree/{head_sha}")
        else:
            a(f"- **Head yang di-pin:** TIDAK TERBACA dari API. Jangan menulis sha dari ingatan —")
            a(f"  baca ulang `gh api repos/{slug}/pulls/{number} --jq .head.sha` sampai cocok,")
            a("  baru serahkan prompt-nya ke pemilik.")
    elif number and number > 0:
        a(f"- **Link PR: TIDAK DICETAK** karena slug repo tidak terbaca (terbaca: `{slug}`).")
        a("  Ambil slugnya dengan `gh repo view --json nameWithOwner -q .nameWithOwner`, rangkai")
        a("  `https://github.com/<slug>/pull/<N>`, lalu serahkan link itu ke pemilik.")
    elif objek:
        a("- **Link PR:** tidak ada — pemeriksaan menyeluruh (audit isi) tidak menunjuk PR;")
        a("  kanal penyerahannya Issue atau berkas ter-commit (`_meta/PROTOKOL_AUDIT_ISI.md`).")
    else:
        a("- **Link PR:** tidak dicetak — mode `--generic` tidak menunjuk PR tertentu.")
    tujuan = out_path or "<path>"
    if number and number > 0:
        a(f"- **Regenerasi kalau berkasnya hilang:** `python3 tools/review_prompt.py --pr {number}"
          f" --out {tujuan}`")
        a(f"- **Kumpulkan verdict sesudah hakim selesai:** `python3 tools/ambil_verdict.py"
          f" --pr {number} --harapkan <jumlah hakim>`")
    elif objek:
        a(f"- **Regenerasi kalau berkasnya hilang:** `python3 tools/audit_prompt.py"
          f" --objek {objek} --out {tujuan}`")
        a("- **Kumpulkan hasil sesudah auditor selesai:**"
          " `python3 tools/ambil_verdict.py --terbaru`")
    a("- **Sebelum diserahkan, agent WAJIB memverifikasi (bukan mengandalkan ingatan):**")
    if number and number > 0:
        a("  1. sha head di dalam prompt == sha head PR dari API;")
        a("  2. nomor putaran dicetak alat, bukan ditebak;")
    elif objek:
        a("  1. sha pin di dalam prompt == sha HEAD dari git (`git rev-parse HEAD`);")
        a("  2. objek yang disebut di prompt == objek yang diminta pemilik, bukan ditebak;")
    else:
        a("  1. prompt ini versi placeholder — JANGAN diserahkan sebagai prompt kerja;")
        a("  2. jalankan ulang dengan `--pr <N>` (review) atau `--objek <path>` (audit isi);")
    a("  3. setiap link di atas benar-benar terbuka;")
    a("  4. path absolut di atas benar-benar ada di disk (`ls -l`).")
    a("")
    return "\n".join(b) + "\n"


# --------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="review_prompt.py",
        description="Bangkitkan prompt review independen dari data PR yang nyata.",
    )
    ap.add_argument("--pr", type=int, default=None, help="nomor PR")
    ap.add_argument("--generic", action="store_true", help="cetak versi placeholder (tanpa memanggil GitHub)")
    ap.add_argument("--out", default="-", help="'-' (default, stdout) atau path berkas")
    ap.add_argument("--harapkan", type=int, metavar="N", default=KUORUM_HAKIM_DEFAULT,
                    help=f"kuorum hakim untuk memutuskan apakah satu putaran masih berjalan "
                         f"(default {KUORUM_HAKIM_DEFAULT})")
    ap.add_argument("--umumkan", action="store_true",
                    help="tempel prompt ke kanal PR sebagai komentar penulis (BUKAN verdict) "
                         "lalu cetak permalink-nya di blok serah terima")
    args = ap.parse_args(argv)

    # RP12: kedua nilai ini yang dipakai blok serah terima. Default None supaya mode --generic
    # (tanpa GitHub) tidak pernah mencetak nomor PR atau sha karangan.
    number: int | None = None
    head_sha: str | None = None

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
            # R3: objek diff DIUKUR sebelum prompt dicetak, bukan diserahkan ke reviewer untuk ditebak.
            head_sha = data["headRefOid"]  # RP12: sha untuk permalink di blok serah terima
            # Temuan #7: ujung base yang SEBENARNYA diukur, bukan diambil dari base sha beku di API.
            ujung_base = ujung_base_hidup(data["baseRefName"])
            # R3: objek diff DIUKUR sebelum prompt dicetak, bukan diserahkan ke reviewer untuk ditebak.
            objek = objek_diff(data["baseRefOid"], head_sha, ujung_hidup=(ujung_base or {}).get("sha"))
            # Temuan #2: putaran dihitung dari kanal + kuorum + head, supaya putaran yang sedang
            # berjalan tidak dinamai sebagai putaran berikutnya.
            putaran = next_round(data["number"], args.harapkan, head_sha)
            text, windows = render(data, files, generic=False, objek=objek, putaran=putaran,
                                   ujung_base=ujung_base)
    except ToolError as exc:
        print(f"review_prompt: GAGAL — {exc}", file=sys.stderr)
        return 2

    # RP12: blok serah terima ditempel ke prompt DAN diteriakkan ke stderr. Dua kanal, bukan satu:
    # berkasnya memuat link untuk pemilik, stderr memaksa agent yang menjalankan alat melihatnya.
    # T-48: tempel prompt ke kanal PR lebih dulu (isi komentarnya = prompt murni, tanpa blok
    # serah terima), lalu permalink-nya masuk ke blok serah terima di berkas.
    permalink: str | None = None
    if args.umumkan:
        if not number or number <= 0:
            print("--umumkan butuh nomor PR (pakai --pr N); prompt generic tidak punya kanal PR",
                  file=sys.stderr)
        else:
            permalink, catatan = umumkan_prompt(
                number, text, head_sha=head_sha,
                out_path=None if args.out == "-" else args.out)
            print(f"pengumuman: {catatan}" + (f" -> {permalink}" if permalink else ""),
                  file=sys.stderr)

    teks_serah = handoff_block(number, head_sha, None if args.out == "-" else args.out,
                               permalink=permalink)
    text = text + "\n" + teks_serah

    if args.out == "-":
        print(text)
    else:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        # RP18: bukti keberadaan berkas diukur SESUDAH ditulis, lalu ditempel ke berkas itu sendiri
        # supaya klaim di blok serah terima didukung pengukuran, bukan urutan kode.
        _baris_verif = verifikasi_berkas_prompt(args.out)
        with Path(args.out).open("a", encoding="utf-8") as _fverif:
            _fverif.write(_baris_verif + "\n")
        _pverif = Path(args.out).resolve()
        print(f"ditulis: {_pverif} ({_pverif.stat().st_size:,} byte sesudah verifikasi ditempel)",
              file=sys.stderr)
    print(teks_serah, file=sys.stderr)

    if windows:
        print(
            "PERINGATAN: jendela uji terbuka → rumusan hasil disembunyikan "
            f"({len(windows)} pointer SHA+baris dipakai sebagai gantinya)",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
