#!/usr/bin/env python3
"""audit_prompt.py — pembangkit prompt AUDIT ISI (repo/sistem/dokumen), bukan review PR.

KENAPA ALAT INI ADA
-------------------
Sebelum 17 Sep 2026 repo ini hanya punya `tools/review_prompt.py`, yang **terikat PR**:
anatomi prompt-nya mensyaratkan "nomor PR + SHA basis + SHA head", dan tanpa nomor PR alat
itu berhenti. Untuk **mengaudit ISI** (folder `_meta/`, `tools/`, sebuah sistem, atau sebuah
dokumen) tidak ada pembangkitnya — sehingga prompt audit harus **dikarang tangan**.

Itu masalah serius, dan persis yang `review_prompt.py` dibuat untuk mencegah: prompt yang
dikarang tangan berarti **pihak yang diaudit menulis instruksi untuk pengadilnya sendiri**.
Prinsip "Sumber prompt" di `PROTOKOL_REVIEW_INDEPENDEN.md` **tidak bisa ditaati** untuk
audit isi selama alatnya belum ada.

Ditemukan sebagai temuan X-04 pada audit 17 Sep 2026; diminta eksplisit oleh pemilik (T29):
*"yang aku maksud saat ini adalah mekanisme review isi repo, isi sistem, dan semua hal yang
perlu diperiksa. Bukan soal PR dan bukan soal merge."*

ATURAN PAKAI (baca sebelum menjalankan)
---------------------------------------
* Prompt audit **tidak boleh dikarang atau disunting** oleh sesi yang objeknya diaudit.
  Kalau auditor butuh konteks tambahan, konteks itu masuk ke **badan Issue**, bukan ke prompt.
* Objek **wajib ada** dan **di-pin ke satu sha**. Alat ini **menolak** mencetak prompt dengan
  sha kosong atau objek yang tidak ditemukan — pola fail-closed yang diwarisi dari
  `review_prompt.py` ("Nomor PR TIDAK ditebak").
* **INDUK JUGA OBJEK YANG SAH.** `--objek _meta` dan `--objek tools` sama sahnya dengan
  `--objek sistem/<nama>` — instruksi pemilik 17 Sep 2026: mekanisme ini harus tertanam di
  meta-sistem juga, bukan hanya di sistem yang dibangunnya.
* Hasil audit dikirim ke **GitHub Issue** (bukan PR) supaya sesi yang sedang berjalan bisa
  **mengambilnya sendiri** tanpa pemilik menyalin apa pun — lihat `tools/ambil_verdict.py`.

Pemakaian:
  python3 tools/audit_prompt.py --objek _meta
  python3 tools/audit_prompt.py --objek sistem/sistem-klinik --kedalaman mendalam
  python3 tools/audit_prompt.py --objek tools/check_manuals.py --pin <sha>
  python3 tools/audit_prompt.py --generic          # lihat bentuknya tanpa objek sungguhan
  python3 tools/audit_prompt.py --objek _meta --out /tmp/prompt-audit.md
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PLACEHOLDER_OBJEK = "<OBJEK>"
PLACEHOLDER_SHA = "<SHA PIN>"

LABEL_ISSUE = "audit-independen"
JUDUL_POLA = "AUDIT {objek} @{sha_pendek}"

KEDALAMAN = {
    "ringan": (
        "RINGAN — hanya baca objek + jalankan alat pemeriksa yang sudah ada. "
        "Cocok untuk: perubahan kecil, cek berkala, memastikan tidak ada regresi."
    ),
    "sedang": (
        "SEDANG — baca objek + dokumen yang dirujuk objek + jalankan alat + **verifikasi silang** "
        "klaim dokumen terhadap isi berkas. Cocok untuk: perubahan aturan, dokumen yang diwarisi sistem lain."
    ),
    "mendalam": (
        "MENDALAM — semua di atas + telusuri **preseden historis** (log sesi, arsip audit, Log Keputusan) "
        "+ uji klaim dengan menjalankan ulang bukti yang dikutip + periksa **propagasi** ke sistem lain. "
        "Cocok untuk: perubahan struktural `_meta/`, menaikkan versi aturan, klaim DONE/gate."
    ),
}

# Lensa audit diwarisi dari QUALITY_ASSURANCE_AND_EVOLUTION.md bagian "Lensa audit"
# (dikodifikasi 5 Sep 2026, temuan M-08). TIDAK dikarang ulang di sini: satu sumber.
LENSA = [
    ("Konsistensi rujukan silang", "apakah setiap rujukan menunjuk berkas/bagian yang benar-benar ada dan isinya cocok"),
    ("Kontradiksi antar-dokumen", "apakah dua dokumen aktif menyatakan hal yang bertentangan"),
    ("Klaim vs bukti eksekusi", "apakah setiap klaim 'sudah diverifikasi/PASS/selesai' punya bukti yang bisa dijalankan ulang"),
    ("Jalur gagal", "apa yang terjadi kalau langkah gagal — apakah ada langkah pertamanya, atau dibiarkan menggantung"),
    ("Kemudahan pakai (kacamata awam)", "cukup satu prompt? dokumen yang ditempel pengguna versi terbaru? kalimatnya bisa dipahami tanpa bertanya?"),
    ("Propagasi ke sistem masa depan", "apakah perubahan ini otomatis mengalir ke sistem yang dibangun berikutnya, atau berhenti di satu tempat"),
    ("Kesehatan repo", "validator/alat uji hijau? ada berkas yatim, duplikat, atau angka basi?"),
]

# Jalur pengadil: alat/protokol yang mengadili. Mengubahnya = konflik kepentingan.
# Daftar ini SELARAS dengan ARBITER_PATH_REASONS di tools/review_prompt.py — kalau
# salah satunya bertambah, yang lain wajib ikut (dua sumber, sengaja saling menunjuk).
ARBITER_PATHS = (
    "tools/review_prompt.py",
    "tools/audit_prompt.py",
    "tools/ambil_verdict.py",
    "tools/test_failure_injection.py",
    "_meta/PROTOKOL_REVIEW_INDEPENDEN.md",
    "_meta/PROTOKOL_AUDIT_ISI.md",
)


class ToolError(Exception):
    """Kegagalan yang harus terlihat sebagai exit non-zero + pesan spesifik."""


def _run(cmd: list[str]) -> tuple[int, str, str]:
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def head_sha() -> str:
    code, out, err = _run(["git", "rev-parse", "HEAD"])
    if code != 0:
        raise ToolError(
            f"gagal membaca sha HEAD (git rev-parse keluar {code}): {(err or out).strip()[:200]}\n"
            "  Pin sha manual: python3 tools/audit_prompt.py --objek <path> --pin <sha>"
        )
    sha = out.strip()
    if not re.fullmatch(r"[0-9a-f]{40}", sha):
        raise ToolError(f"sha HEAD tidak berbentuk 40 heksadesimal: {sha!r} — prompt TIDAK dicetak dengan sha kosong")
    return sha


def normalize_objek(objek: str) -> str:
    """Objek ditulis relatif terhadap root repo, tanpa './' dan tanpa trailing slash."""
    o = objek.strip().replace("\\", "/")
    while o.startswith("./"):
        o = o[2:]
    o = o.rstrip("/")
    if not o or o in {".", ".."}:
        raise ToolError("objek tidak boleh '.' atau kosong — sebut foldernya, mis. `_meta`, `tools`, `sistem/sistem-klinik`")
    if o.startswith("/"):
        raise ToolError(f"objek wajib relatif terhadap root repo, bukan absolut: {objek!r}")
    if ".." in o.split("/"):
        raise ToolError(f"objek tidak boleh keluar dari repo: {objek!r}")
    return o


def inventaris(objek: str) -> list[tuple[str, int]]:
    """(path_relatif, jumlah_baris) untuk berkas teks di bawah objek, terurut.

    Sengaja memakai INVENTARIS (kewajiban dari isi pohon kerja), bukan daftar yang
    diklaim penulis: kalau ada berkas yang disembunyikan dari daftar, ia tetap muncul di sini.
    """
    p = ROOT / objek
    suffix = {".md", ".py", ".json", ".yml", ".yaml", ".txt", ".sh", ".css", ".html", ".js", ".ts"}
    out: list[tuple[str, int]] = []
    if p.is_file():
        try:
            n = len(p.read_text(encoding="utf-8", errors="replace").splitlines())
        except OSError:
            n = -1
        return [(objek, n)]
    for f in sorted(p.rglob("*")):
        if not f.is_file() or f.suffix.lower() not in suffix:
            continue
        if any(bagian in {".git", "__pycache__", "node_modules"} for bagian in f.parts):
            continue
        try:
            n = len(f.read_text(encoding="utf-8", errors="replace").splitlines())
        except OSError:
            n = -1
        out.append((str(f.relative_to(ROOT)), n))
    return out


def objek_terkait_arbiter(objek: str, files: list[str]) -> list[str]:
    """Apakah objek audit ini MENCAKUP jalur pengadil (audit atas alat pengadil itu sendiri)."""
    kena = []
    for a in ARBITER_PATHS:
        if a == objek or a.startswith(objek.rstrip("/") + "/") or any(f == a for f in files):
            kena.append(a)
    return kena


def render(objek: str, sha: str, kedalaman: str, generic: bool) -> str:
    if generic:
        obj_disp, sha_disp = PLACEHOLDER_OBJEK, PLACEHOLDER_SHA
        files: list[tuple[str, int]] = []
        arbiter: list[str] = []
    else:
        obj_disp, sha_disp = objek, sha
        files = inventaris(objek)
        arbiter = objek_terkait_arbiter(objek, [f for f, _ in files])

    L: list[str] = []
    a = L.append

    a(f"# Prompt Audit Isi — {obj_disp}")
    a("")
    a("> Dibangkitkan `tools/audit_prompt.py` dari **isi pohon kerja pada sha yang di-pin** — bukan dari")
    a("> narasi pihak yang diaudit. Prompt ini **tidak boleh dikarang, ditambah, dipotong, atau disunting**")
    a("> oleh sesi yang objeknya sedang diaudit. Butuh menambah konteks? Tulis di **badan Issue**, bukan di sini.")
    a("")
    a("## 1. Siapa kamu")
    a("")
    a("Kamu **sesi audit independen**. Kamu tidak melanjutkan pekerjaan sesi lain, tidak memperbaikinya,")
    a("dan tidak mengeksekusi temuannya. Kamu **memeriksa dan melaporkan**.")
    a("")
    a("- Mulai **tanpa konteks** dari sesi mana pun: yang kamu percaya hanya artefak (isi berkas, git tree,")
    a("  keluaran alat). Klaim penulis/sesi sebelumnya = **objek pemeriksaan**, bukan bukti.")
    a("- **Read-only terhadap repo**: jangan commit, jangan push, jangan sunting berkas repo.")
    a("  Salinan kerja **hanya di `/tmp`**; jalankan alat di sana kalau perlu mengubah sesuatu untuk menguji.")
    a("- **Ini audit ISI, bukan review PR.** Tidak ada merge, tidak ada verdict atas PR, tidak ada tombol")
    a("  yang harus kamu tekan. Keluaranmu adalah **laporan temuan**.")
    a("")
    a("## 2. Objek ter-pin")
    a("")
    a("| Objek | Nilai |")
    a("|---|---|")
    a(f"| Jalur | `{obj_disp}` |")
    a(f"| SHA pin | `{sha_disp}` |")
    a(f"| Kedalaman | {KEDALAMAN[kedalaman].split(' — ')[0]} |")
    if not generic:
        a(f"| Berkas terinventaris | {len(files)} |")
    a("")
    a("Semua pemeriksaan dilakukan **pada sha itu**. Kalau pohon kerja sudah bergerak, **jangan** diam-diam")
    a("mengaudit versi lain: laporkan bahwa sha tidak cocok, dan sebut sha yang kamu temukan.")
    a("")
    if not generic and files:
        a("### Inventaris berkas (diambil dari pohon kerja, bukan dari klaim siapa pun)")
        a("")
        a("| Berkas | Baris |")
        a("|---|---|")
        for rel, n in files[:120]:
            a(f"| `{rel}` | {n if n >= 0 else '(tidak terbaca)' } |")
        if len(files) > 120:
            a(f"| … | {len(files) - 120} berkas lain tidak ditampilkan — **inventaris lengkap wajib kamu ambil sendiri** |")
        a("")
        a("**Berkas yang ada di pohon kerja tetapi TIDAK ada di tabel di atas = temuan.** Inventaris ini")
        a("dibatasi 120 baris supaya prompt tidak meledak; jangan perlakukan batas tampilan sebagai batas audit.")
        a("")
    a("## 3. Kedalaman pemeriksaan")
    a("")
    a(f"**{KEDALAMAN[kedalaman]}**")
    a("")
    a("Kedalaman mengikuti risiko (`QUALITY_ASSURANCE_AND_EVOLUTION.md` bagian \"Kedalaman pemeriksaan")
    a("berbasis risiko\"). **Jangan menaikkan kedalaman tanpa alasan** — audit yang lebih dalam dari risikonya")
    a("menghasilkan derau, bukan kebenaran. **Jangan menurunkannya diam-diam** — kalau kamu tidak sanggup")
    a("memenuhi kedalaman yang diminta, **katakan begitu di laporan**, jangan pura-pura sudah.")
    a("")
    a("## 4. Urutan baca (jangan dilewati)")
    a("")
    a("1. Dokumen aturan yang menaungi objek: `_meta/02_PRINSIP_UNIVERSAL.md`, `_meta/03_KONTRAK_WARISAN.md`,")
    a("   `_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md` (**termasuk bagian ATURAN CAKUPAN**), `_meta/PLATFORM_LMARENA.md`.")
    a("2. Isi objek itu sendiri, sesuai inventaris di atas.")
    a("3. Dokumen yang **dirujuk** oleh objek (rujukan silang = permukaan kontradiksi).")
    a("4. Kalau kedalaman MENDALAM: preseden historis — log sesi, arsip audit di `_meta/_internal/`, dan tabel")
    a("   Log Keputusan tiap dokumen hidup.")
    a("")
    a("## 5. Tujuh lensa audit (semua wajib dijalankan, bukan dipilih)")
    a("")
    a("| # | Lensa | Yang diperiksa |")
    a("|---|---|---|")
    for i, (nama, isi) in enumerate(LENSA, 1):
        a(f"| {i} | **{nama}** | {isi} |")
    a("")
    a("Lensa di atas **diwarisi** dari `QUALITY_ASSURANCE_AND_EVOLUTION.md` — satu sumber, tidak dikarang ulang.")
    a("Kalau sebuah lensa **tidak menghasilkan apa pun** untuk objek ini, tulis \"tidak ada temuan\" untuk lensa")
    a("itu. **Dilarang melewatkannya tanpa keterangan**: pembaca laporan tidak bisa membedakan \"sudah diperiksa,")
    a("bersih\" dari \"tidak diperiksa\".")
    a("")
    a("## 6. ATURAN CAKUPAN — bagian yang paling sering dilanggar")
    a("")
    a("> **Cakupan membatasi RENCANA PENCARIAN dan KLAIM. Cakupan TIDAK PERNAH membatasi LAPORAN.**")
    a("")
    a("- Objek yang di-pin di bagian 2 membatasi **apa yang kamu cari secara sistematis**, dan **apa yang boleh")
    a("  kamu klaim** sudah diperiksa.")
    a("- Objek itu **tidak** membatasi **apa yang boleh kamu laporkan**.")
    a("- **WAJIB**: temuan di luar objek/cakupan **tetap dilaporkan**, diberi label **\"di luar cakupan\"**,")
    a("  lengkap dengan klasifikasi + prioritas + dasar bukti.")
    a("- **DILARANG**: mengklaim cakupan lebih luas dari yang kamu kerjakan; membuang atau menghaluskan temuan")
    a("  karena tidak diminta; **bertindak/memperbaiki** atas temuan di luar cakupan tanpa mandat.")
    a("- **WAJIB**: kalau kamu menyadari telah membaca sesuatu di luar jalur yang diizinkan, **ungkapkan**")
    a("  (disclosure) di laporan. Jangan disembunyikan, jangan dipakai diam-diam sebagai dasar kesimpulan.")
    a("")
    a("## 7. Klasifikasi temuan (WAJIB — temuan tanpa klasifikasi tidak sah)")
    a("")
    a("| Kode | Arti |")
    a("|---|---|")
    a("| `B` | **Bug** — sesuatu yang salah dan bisa ditunjukkan salahnya |")
    a("| `A` | **Ambiguitas** — bisa dibaca dua arah, dan salah satu arah berbahaya |")
    a("| `G` | **Gap proses** — aturannya ada tapi tidak ditegakkan, atau belum ada aturannya |")
    a("| `N` | **Kebutuhan baru** — bukan cacat, tapi sesuatu yang ternyata diperlukan |")
    a("| `P` | **Preferensi/housekeeping** — kosmetik, rapikan kalau sempat |")
    a("")
    a("Setiap temuan **wajib** memuat: **klasifikasi** + **prioritas `P1`/`P2`/`P3`** + **dasar bukti**")
    a("(berkas:baris, atau perintah + keluarannya). **Temuan tanpa bukti terverifikasi dicatat sebagai")
    a("\"dugaan\"** dan tidak boleh langsung jadi perbaikan.")
    a("")
    a("## 8. Verifikasi adversarial — WAJIB sebelum menulis temuan")
    a("")
    a("Untuk **setiap** kandidat temuan, sebelum memasukkannya ke laporan:")
    a("")
    a("1. **Coba bantah sendiri.** Cari pembacaan lain yang membuat itu bukan cacat. Kalau bantahannya berhasil,")
    a("   **buang** — dan catat di bagian \"kandidat yang dicabut\" bersama alasannya.")
    a("2. **Baca di sumbernya.** Jangan memutuskan dari keluaran alat pemindai. Analisis statis mentah")
    a("   menghasilkan mayoritas positif palsu; pada audit 17 Sep 2026, **28 dari 43 kandidat (~65%) dicabut**")
    a("   setelah diverifikasi manusia.")
    a("3. **Jelaskan MENGAPA, bukan hanya BAHWA.** Temuan yang tidak menyebut akibatnya tidak bisa diprioritaskan.")
    a("4. **Bedakan build-time dan run-time.** Sesuatu yang gagal di lingkungan agent belum tentu gagal di")
    a("   produksi, dan sebaliknya (`PLATFORM_LMARENA.md` fakta #4: **waktu-pakai ≠ waktu-bangun**).")
    a("5. **Laporkan rasio sinyalmu sendiri.** Sebut berapa kandidat yang kamu periksa dan berapa yang kamu")
    a("   cabut. Itu yang membuat laporanmu bisa dinilai kejujurannya.")
    a("")
    a("**Dilarang** melaporkan kandidat mentah. Cry-wolf adalah alasan utama alat review ditinggalkan.")
    a("")
    a("## 9. Batas anti-recursion dan KONDISI BERHENTI")
    a("")
    a("- **Kondisi berhenti:** audit ini **satu putaran**. Kamu melaporkan, lalu berhenti.")
    a("- **Jangan mengaudit mekanisme audit ini** sebagai bagian dari audit objek, kecuali objeknya memang")
    a("  mekanisme itu. Audit atas mekanisme dilakukan saat ada bukti masalah atau perubahan besar.")
    a("- **Maksimal 2 putaran** untuk keseluruhan proses (putaran 2 = verifikasi atas tanggapan). Putaran ke-2")
    a("  gagal = **eskalasi ke pemilik**, bukan putaran ke-3.")
    a("- **Batas 2 putaran membatasi LOOP, BUKAN cakupan laporan.** Putaran boleh habis; temuan di luar")
    a("  cakupan tetap wajib dilaporkan (bagian 6).")
    a("")
    a("## 10. Cara menyerahkan hasil (WAJIB — tanpa ini audit dianggap belum diserahkan)")
    a("")
    if generic:
        judul = JUDUL_POLA.format(objek=PLACEHOLDER_OBJEK, sha_pendek="<7 SHA>")
        sha_ref = PLACEHOLDER_SHA
    else:
        judul = JUDUL_POLA.format(objek=objek, sha_pendek=sha[:7])
        sha_ref = sha
    a("Hasil audit diserahkan lewat **salah satu dari dua kanal**. Judulnya **berpola tetap** supaya sesi")
    a("yang sedang berjalan bisa **menemukannya sendiri** tanpa diberi tahu nomornya.")
    a("")
    a("### KANAL A — berkas ter-commit (PAKAI INI; yang lain terbukti terblokir di lingkungan ini)")
    a("")
    a("**Terverifikasi 17 Sep 2026:** `gh issue create` ditolak **HTTP 403 `Resource not accessible by")
    a("integration (createIssue)`**, dan `permissions` API repo menunjukkan **semua izin false**. Sebaliknya")
    a("`git push` **berhasil**. Jadi kanal git yang dipakai. Tulis laporanmu ke:")
    a("")
    a("```")
    a("_meta/_internal/audit/AUDIT_<objek-dengan-garis-bawah>_<sha7>.md")
    a("```")
    a("")
    a("Baris **pertama** berkas wajib berpola persis (baris inilah yang dibaca alat, bukan nama berkasnya):")
    a("")
    a("```")
    a(f"# {judul}")
    a("```")
    a("")
    a("Lalu **commit + push**. Folder itu sengaja di bawah `_meta/_internal/` karena **tidak ikut ke ekstrak")
    a("template**, jadi artefak audit tidak bocor ke sistem anak.")
    a("")
    a("### KANAL B — GitHub Issue (alternatif; hidup kalau izin `issues:write` kelak diberikan)")
    a("")
    a("```bash")
    a(f"gh issue create --title \"{judul}\" \\")
    a(f"  --label \"{LABEL_ISSUE}\" \\")
    a('  --body-file /tmp/hasil-audit.md')
    a("```")
    a("")
    a("Kalau ini mengembalikan **403**, itu **bukan kesalahanmu** dan **bukan alasan menyimpulkan audit gagal**:")
    a("pindah ke Kanal A, dan **catat 403-nya di dalam laporan** supaya sesi berikutnya tidak mengulang")
    a("penemuan yang sama. Label `audit-independen` **sudah dibuat** di repo ini (17 Sep 2026).")
    a("")
    a("Badan Issue **wajib** memuat, berurutan:")
    a("")
    a(f"1. **VERDICT** satu baris: `BERSIH` / `ADA TEMUAN` / `TIDAK BISA DISIMPULKAN` + sha `{sha_ref}`.")
    a("2. **Ringkasan angka**: berapa berkas diperiksa, berapa kandidat, berapa dicabut sebagai positif palsu.")
    a("3. **Tabel temuan**: ID · kelas (`B`/`A`/`G`/`N`/`P`) · prioritas · berkas:baris · satu kalimat · bukti.")
    a("4. **Temuan DI LUAR CAKUPAN** — bagian tersendiri, jangan dicampur, jangan dibuang.")
    a("5. **Kandidat yang DICABUT** beserta alasannya (bagian 8 butir 5).")
    a("6. **Batasan audit**: apa yang **tidak** diperiksa — supaya laporan tidak terbaca lebih luas dari kenyataannya.")
    a("")
    a("**Append-only:** kalau ada putaran kedua, **tambahkan**, jangan menghapus atau menyunting temuan")
    a("putaran pertama, dan **jangan menghaluskan**. Kanal Issue = komentar baru. Kanal berkas = **berkas baru**")
    a("dengan sha baru, atau bagian `## Putaran 2` di bawah — **jangan menimpa** isi putaran 1.")
    a("(Catatan jujur: di kanal berkas aturan append-only ini **belum ditegakkan alat** — baru imbauan.)")
    a("")
    a("Sesi yang diaudit kemudian mengambil hasilnya sendiri — **mencari di kedua kanal sekaligus**:")
    a("")
    a("```bash")
    a("python3 tools/ambil_verdict.py --terbaru")
    a("```")
    a("")
    a("Pemilik **tidak perlu menyalin apa pun** — cukup bilang \"audit sudah selesai\".")
    a("")
    a("## 11. Pengecualian pengadil")
    a("")
    if arbiter:
        a("**BERLAKU untuk audit ini.** Objeknya **mencakup alat/protokol pengadil**:")
        a("")
        for rel in arbiter:
            a(f"- `{rel}`")
        a("")
        a("Mengaudit alat pengadil memakai alat pengadil adalah **rekursi yang sah untuk dilaporkan tetapi")
        a("tidak untuk diputuskan sendiri**. Karena itu: laporkan temuanmu, **tetapi jangan menyatakan")
        a("mekanisme pengadil itu sendiri sahih atau tidak sahih** — itu keputusan pemilik, dan sebaiknya")
        a("diperiksa oleh pengadil dari keluarga model yang berbeda.")
    else:
        a("Objek ini **tidak** mencakup alat/protokol pengadil, jadi bagian 10 berlaku normal.")
        a("")
        a("Kalau pemeriksaanmu sendiri ternyata menyentuh salah satu dari ini:")
        for rel in ARBITER_PATHS:
            a(f"- `{rel}`")
        a("")
        a("maka **berhenti menyatakan kesimpulan tentang mekanisme pengadil**, laporkan sebagai temuan, dan")
        a("serahkan keputusannya ke pemilik. Pengadil tidak mengesahkan perubahan atas dirinya sendiri.")
    a("")
    a("## 12. Batas publikasi (aturan 6d)")
    a("")
    a("Kalau kamu menemukan **jendela uji yang sedang terbuka** (log sesi berkeadaan `OPEN` yang menyebut")
    a("acceptance test / prosedur uji yang belum ditutup), maka **artefak yang kamu publikasikan tidak boleh")
    a("memuat rumusan jawaban atau kriteria yang belum tertutup uji itu**. Rujuk lewat **pointer SHA+baris**,")
    a("jangan salin isinya ke Issue, komentar, log, atau branch mana pun.")
    a("")
    a("## 13. Yang tidak pernah boleh kamu lakukan")
    a("")
    a("- **Memperbaiki sendiri** temuanmu — versi, wording, pin, transkrip, atau isi berkas pihak yang diaudit.")
    a("  Auditor yang menambal temuannya sendiri sudah berhenti jadi auditor.")
    a("- **Merge, push, commit, atau menyunting berkas repo.** Read-only.")
    a("- **Melebihi-lebihkan cakupan** — menulis seolah memeriksa lebih dari yang kamu periksa.")
    a("- **Menghaluskan atau membuang** temuan karena tidak diminta, karena tidak enak, atau karena di luar objek.")
    a("- **Menyatakan kelulusan kemudahan-pakai atas nama orang awam.** Kamu bukan orang awam. Lensa #5 hanya")
    a("  bisa kamu nilai sebagian; sisanya **wajib** diuji manusia (`PANDUAN_PENGGUNA_TEMPLATE.md` Syarat 4).")
    a("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--objek", help="jalur relatif dari root repo: `_meta`, `tools`, `sistem/<nama>`, atau satu berkas")
    ap.add_argument("--pin", help="sha yang di-pin (default: HEAD pohon kerja)")
    ap.add_argument("--kedalaman", choices=sorted(KEDALAMAN), default="sedang",
                    help="kedalaman berbasis risiko (default: sedang)")
    ap.add_argument("--generic", action="store_true",
                    help="cetak bentuk prompt dengan placeholder, tanpa objek sungguhan")
    ap.add_argument("--out", help="tulis prompt ke berkas ini, bukan ke stdout")
    a = ap.parse_args()

    try:
        if a.generic:
            teks = render("", "", a.kedalaman, generic=True)
        else:
            if not a.objek:
                raise ToolError(
                    "tidak ada --objek dan tidak ada --generic.\n"
                    "  Audit isi WAJIB menyebut objeknya: python3 tools/audit_prompt.py --objek <path>\n"
                    "  Contoh objek yang sah: `_meta` (induk), `tools`, `sistem/sistem-klinik`, satu berkas.\n"
                    "  Objek TIDAK ditebak dari branch atau dari riwayat — menebak objek berarti mengaudit\n"
                    "  sesuatu yang tidak diminta siapa pun."
                )
            objek = normalize_objek(a.objek)
            if not (ROOT / objek).exists():
                raise ToolError(
                    f"objek `{objek}` TIDAK ADA di root repo. Prompt TIDAK dicetak untuk objek yang tidak ada.\n"
                    "  Periksa ejaannya, atau lihat daftar sistem: `_meta/INDEKS_SISTEM.md`."
                )
            sha = a.pin or head_sha()
            if not re.fullmatch(r"[0-9a-f]{7,40}", sha):
                raise ToolError(f"sha pin tidak sah: {sha!r} — prompt TIDAK dicetak dengan sha kosong/tak berbentuk")
            teks = render(objek, sha, a.kedalaman, generic=False)
    except ToolError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    if a.out:
        Path(a.out).write_text(teks, encoding="utf-8")
        print(f"prompt audit ditulis ke {a.out} ({len(teks.splitlines())} baris)")
    else:
        print(teks)
    return 0


if __name__ == "__main__":
    sys.exit(main())
