#!/usr/bin/env python3
"""Small dependency-free structural regression check for the master blueprint.

Reworked during the 5 Sep 2026 full meta audit, hardened 5 Sep 2026 after the
independent review of PR #11 (findings F1–F16):
- M-01 + review F1: required files = STATIC CORE inventory (obligation,
  checkpoint_core.CORE_REQUIRED) UNION derived glob lists. A deleted core
  file now fails loudly (before it silently shrank the requirement set); a
  new active file is still auto-required.
- M-02/M-03 + review F4: checkpoint field and unit status parsing live in
  the SHARED fail-closed parser (checkpoint_core): line-anchored (quoted
  examples don't count), code-fence contents ignored, duplicate/ambiguous
  field = NOT safe, protocol formats recognized.
- Review F2: STRICT 'Daftar Sistem' parsing — a row is valid only with an
  exact backticked `sistem-<nama>/` folder cell; an unregistered `sistem-*/`
  folder is an error (the old `"pilot" in name` substring exception even
  matched `sistem-autopilot-data`).
- Review F3: registered systems are EXPECTED to have at least one unit
  STATUS.md (any layout); zero discovered no longer passes — it fails
  (warning only when the manifest declares `Tahap: kerangka`).
- Review F8: STATUS templates must parse to the exact safe value with the
  same shared parser (guidance text inside the field value = defect).
- Review F9: Warisan enforcement — all ten items W-01..W-10 present in the
  system manifest; an 'override' row exempts the mechanical check of that
  item only with the full approval trail (alasan/dampak/tanggal/approval).
- Review F13/F14: path-reference resolution is scoped per document (a doc
  inside a system resolves within its own system + _meta + root; master-level
  docs stay cross-system by design), and URIs are not repository paths.
- 7 Sep 2026 (_meta/PAKET_REPO_MANDIRI.md), retained obligation:
  every REGISTERED system must ship its own self-contained validator
  (checkpoint_core.SYSTEM_REQUIRED_FILES) — a static obligation list in
  the same style as CORE_REQUIRED; absence is an error, downgraded to a
  warning only by the SAME `Tahap: kerangka` lifecycle that already
  relaxes W-01..W-03 (a skeleton system has nothing to validate yet).
- 8 Sep 2026: standalone-pack mode was retired by owner decision. This
  validator no longer reads repo profiles, absent-reference whitelists, or
  generated package metadata; it validates the master blueprint and clean
  template extracts only. Folder deliverability is checked by
  tools/check_selfcontained.py.
"""
from pathlib import Path
import re
import sys

import checkpoint_core as core

ROOT = Path(__file__).resolve().parents[1]

errors = []
stage_warnings = []  # kerangka-stage relaxations (F9) — warning tier

# --- Required files ---------------------------------------------------------
_derived = (
    {f"_meta/{p.name}" for p in (ROOT / "_meta").glob("*.md")}
    | {f"tools/{p.name}" for p in (ROOT / "tools").glob("*.py")}
)
required = sorted(set(core.CORE_REQUIRED) | _derived | set(core.CORE_ROOT_FILES))

for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

for p in ROOT.rglob("*.md"):
    if ".git" in p.parts:
        continue
    text = p.read_text(encoding="utf-8")
    if any(marker in text for marker in ("<<<<<<<", ">>>>>>>")):
        errors.append(f"merge conflict marker: {p.relative_to(ROOT)}")
    if text.count("```") % 2:
        errors.append(f"unpaired code fence: {p.relative_to(ROOT)}")

# --- Integritas tabel Markdown: SEMUA artefak repo, bukan hanya register & ledger -------------
# Diperluas 18 Sep 2026 (T-47) sesudah **14 temuan nyata** ditemukan DI LUAR dua berkas yang dijaga
# versi sebelumnya: dua baris Log Evolusi `_meta/SYSTEM_MANIFEST.md` yatim di tengah prosa (masuk
# dari commit `1361f2f` dan `e78f59f` — pekerjaan agent ini sendiri, bentuknya 2 sel di tabel 5 sel),
# empat baris register "Sudah ditutup" (T-39/T-40/T-43/T-41) terputus dari tabelnya oleh garis `---`,
# lima baris berpipa tak ter-escape di dalam sel (manifest meta, kontrak warisan, dua di
# ACCEPTANCE_TEST_LOG konten-kreator, manifest konten-kreator), dan dua baris tabel diputus baris
# kosong (draft kerangka + `sistem-undangan/00_RENCANA_KERANGKA.md`). Penjaga versi lama hanya
# membaca 2 berkas, jadi SEMUA itu lolos sementara validator mencetak PASS — persis pola "klaim
# lebih luas dari cakupan" yang sudah dua kali ditutup di PR ini.
#
# PENJAGA INI BERBASIS BLOK, bukan streaming. Versi streaming yang sempat dibuat menandai BARIS
# HEADER sebagai yatim (header selalu datang sebelum baris pemisah, jadi kolom harapan belum
# diketahui) dan menghasilkan ratusan temuan palsu; ketahuan karena dijalankan pada pohon bersih
# dulu. Aturan mainnya: baris pipa yang BERURUTAN = satu blok. Kalau baris kedua blok adalah pemisah
# (`|---|`), blok itu tabel → setiap baris wajib se-kolom dengan header. Kalau tidak, seluruh baris
# blok itu YATIM: tersisip di prosa, atau terputus dari tabelnya oleh baris kosong / garis `---` —
# di Markdown keduanya dirender sebagai TEKS BIASA, jadi datanya "ada" tetapi tidak pernah tampil.
#
# Yang dilewati dan mengapa: folder vendor (`skills/` = dokumen pihak ketiga yang disalin apa adanya;
# mengubahnya merusak provenance dan sinkronisasi hulu) dan ISI PAGAR KODE (pipa di dalam contoh kode
# bukan sel tabel). Pipa ter-escape `\|` juga bukan pemisah sel.
#
# Aturan yang DILEPAS dengan sadar dari versi lama: "baris non-pipa tepat sesudah baris tabel". Pada
# cakupan 2 berkas itu aman; pada seluruh repo ia menandai prosa yang wajar langsung mengikuti tabel.
# Bentuk korupsi yang diincarnya tetap tertangkap aturan yatim/kolom di bawah.
TABEL_VENDOR = ("skills", "node_modules", "backups", "template_clean", ".git", "__pycache__")
SEP_TABLE_RE = re.compile(r"^\|(?:\s*:?-+:?\s*\|)+\s*$")

# --- Berkas BUKTI HISTORIS: append-only menang atas kosmetika tabel ---------------------------------
# Keputusan pemilik 18 Sep 2026 (opsi A), menutup temuan yang dilaporkan KETIGA hakim putaran 3 PR #74:
# penjaga integritas tabel (T-47) mewajibkan pipa di dalam sel di-escape, sedangkan aturan append-only
# melarang suntingan pada berkas bukti. Dua aturan itu saling mengunci, dan yang terjadi adalah riwayat
# tersunting (2 baris `sistem/sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md`, terukur `2 2` di numstat).
# Keduanya sudah dikembalikan ke byte asli (diff-nya terhadap merge-base kini KOSONG), dan kelas berkas
# ini dikecualikan dari PAKSAAN suntingan: cacat tabel di berkas bukti historis dicetak sebagai
# PERINGATAN, bukan kegagalan. Dokumen hidup/normatif (manifest, protokol, register, ledger, DoD,
# indeks, dokumen sistem) TETAP kegagalan keras — pengecualian ini sempit dan disebut eksplisit.
# Sebabnya prinsip, bukan kenyamanan: bukti yang boleh dirapikan bukan bukti lagi.
POLA_BUKTI_HISTORIS = (
    re.compile(r"(?:^|/)ACCEPTANCE_TEST_LOG\.md$"),
    re.compile(r"(?:^|/)LOG_SESI_[^/]*\.md$"),
    re.compile(r"(?:^|/)DISKUSI_MENTAH_[^/]*\.md$"),
    re.compile(r"(?:^|/)SESSION_REPORT_[^/]*\.md$"),
    re.compile(r"(?:^|/)PILOT_REPORT_[^/]*\.md$"),
    re.compile(r"(?:^|/)BEHAVIORAL_AUDIT_[^/]*\.md$"),
    re.compile(r"(?:^|/)REGRESSION_AUDIT_[^/]*\.md$"),
    re.compile(r"(?:^|/)AUDIT_[^/]*_\d{4}-\d{2}-\d{2}\.md$"),
    re.compile(r"(?:^|/)_log-sesi/"),
    re.compile(r"(?:^|/)_internal/arsip-"),
)


def berkas_bukti_historis(rel: str) -> bool:
    """True kalau `rel` adalah rekaman peristiwa (append-only), bukan dokumen hidup/normatif."""
    r = (rel or "").replace("\\", "/")
    return any(p.search(r) for p in POLA_BUKTI_HISTORIS)


tabel_warnings: list = []


def _kolom(baris: str) -> int:
    """Jumlah sel: pipa yang TIDAK di-escape (`\|` adalah pipa literal di dalam sel)."""
    return len(re.findall(r"(?<!\\)\|", baris)) - 1


def _berkas_markdown_own():
    """Semua `.md` milik repo ini (bukan vendor), urut path supaya temuan deterministik."""
    for _p in sorted(ROOT.rglob("*.md")):
        _rel = _p.relative_to(ROOT)
        if any(_v in _rel.parts for _v in TABEL_VENDOR):
            continue
        yield str(_rel).replace("\\", "/"), _p


AWALAN_WARNING_BUKTI = ("WARNING tabel (berkas bukti historis — append-only menang atas kosmetika "
                        "tabel, keputusan pemilik 18 Sep 2026; JANGAN sunting riwayatnya): ")


def _nilai_blok_tabel(rel, blok, errors, warnings=None):
    """Nilai satu blok baris pipa berurutan: tabel sehat, kolom salah, atau baris yatim.

    Untuk **berkas bukti historis** (`berkas_bukti_historis`) temuan dialihkan ke `warnings` — bukan
    karena cacatnya tidak nyata, tetapi karena memperbaikinya berarti MENYUNTING riwayat, dan itu
    dilarang (keputusan pemilik 18 Sep 2026, opsi A). Semua berkas lain tetap masuk `errors`.
    """
    if not blok:
        return
    _bukti = warnings is not None and berkas_bukti_historis(rel)
    tujuan = warnings if _bukti else errors
    awalan = AWALAN_WARNING_BUKTI if _bukti else ""
    if len(blok) >= 2 and SEP_TABLE_RE.match(blok[1][1]):
        harap = _kolom(blok[0][1])
        for no, teks in blok[2:]:
            if _kolom(teks) != harap:
                tujuan.append(
                    f"{awalan}{rel}:{no}: baris tabel punya {_kolom(teks)} kolom padahal header tabelnya "
                    f"{harap} — baris patah/tersisip salah tempat, atau ada pipa di dalam sel yang "
                    "belum di-escape sebagai \\|"
                )
        return
    for no, teks in blok:
        tujuan.append(
            f"{awalan}{rel}:{no}: BARIS TABEL YATIM — baris `|…|` yang tidak punya header+pemisah tabel "
            f"di atasnya ({teks[:60]}). Sebab umumnya: tersisip di tengah prosa, atau terputus dari "
            "tabelnya oleh baris kosong / garis `---`. Di Markdown ini dirender sebagai TEKS BIASA, "
            "jadi datanya ada di berkas tetapi tidak pernah tampil sebagai tabel"
        )


for _rel, _path in _berkas_markdown_own():
    _garis = _path.read_text(encoding="utf-8", errors="replace").splitlines()
    _blok: list = []
    _pagar = False
    for _no, _line in enumerate(_garis, 1):
        _s = _line.strip()
        if _s.startswith("```"):
            _pagar = not _pagar
            _nilai_blok_tabel(_rel, _blok, errors, tabel_warnings)
            _blok = []
            continue
        if _pagar:
            continue
        if _s.startswith("|") and _s.endswith("|"):
            _blok.append((_no, _s))
            continue
        _nilai_blok_tabel(_rel, _blok, errors, tabel_warnings)
        _blok = []
    _nilai_blok_tabel(_rel, _blok, errors, tabel_warnings)

# --- Volatile corpus counts are forbidden in permanent evidence (C5/AT-16) --
manifest_path = ROOT / "_meta/SYSTEM_MANIFEST.md"
if manifest_path.is_file():
    in_evolution = False
    corpus_terms = r"rujukan|path\s+references|dokumen|active\s+documents"
    for lineno, line in enumerate(manifest_path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip() == "## Log Evolusi": in_evolution = True; continue
        if in_evolution and line.startswith("## "): break
        if not in_evolution or not line.startswith("|"): continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or cells[0].lower() in {"tanggal", "---"}: continue
        evidence = cells[3]
        if re.search(r"\d+\s+(?:" + corpus_terms + r")|(?:" + corpus_terms + r")\s*[:=]?\s*\d+", evidence, re.IGNORECASE):
            errors.append(f"SYSTEM_MANIFEST Log Evolusi:{lineno}: sel Bukti mengutip angka korpus; angka ini bergerak setiap kali LOG_SESI ditulis sehingga tidak bisa menjadi bukti permanen")

# --- Induk TUNDUK pada kontrak warisannya sendiri (17 Sep 2026) --------------
# Instruksi eksplisit pemilik: mekanisme wajib tertanam di META-SISTEM juga,
# bukan hanya di sistem yang dibangunnya. Sebelum cek ini ada, meta dikecualikan
# secara struktural: kontrak hanya menyebut "sistem yang dibangun oleh meta",
# INDEKS menyatakan meta "bukan salah satu isinya", dan validator hanya memeriksa
# sistem terdaftar. Tiga gap nyata (W-03/W-07/W-09) lolos tanpa terdeteksi.
#
# Yang ditagih di sini = DEKLARASI STATUS tiap butir (termasuk gap yang dinyatakan
# jujur), BUKAN keberadaan artefak. Sengaja begitu: bentuk beberapa butir memang
# berbeda di level meta (meta tidak punya "unit kerja" ber-STATUS.md), dan memaksa
# artefak yang seragam akan menghasilkan KEPATUHAN PALSU — centang tanpa substansi.
_meta_manifest = ROOT / "_meta/SYSTEM_MANIFEST.md"
if _meta_manifest.is_file():
    _mt = _meta_manifest.read_text(encoding="utf-8")
    _potong = re.split(r"^## Warisan Meta\b", _mt, maxsplit=1, flags=re.M)
    if len(_potong) < 2:
        errors.append(
            "_meta/SYSTEM_MANIFEST.md: bagian '## Warisan Meta' TIDAK ADA — induk wajib "
            "menyatakan kepatuhannya pada kontrak warisannya sendiri (permintaan pemilik 17 Sep 2026)"
        )
    else:
        _badan = re.split(r"^## ", _potong[1], maxsplit=1, flags=re.M)[0]
        # Butir wajib muncul sebagai BARIS TABEL deklarasinya (`| W-nn …`), bukan sekadar
        # disebut di prosa. Versi pertama cek ini memakai `\bW-nn\b` pada seluruh badan
        # bagian dan TERBUKTI menghasilkan PASS palsu: kalimat penjelas "menyebut semua
        # butir (W-01…W-10)" sudah memenuhi syarat walau baris deklarasinya dihapus.
        # Tertangkap oleh uji mutasi pada hari yang sama — pola "PASS palsu" yang sama
        # dengan temuan review independen PR #11.
        _baris_dideklarasikan = {
            m.group(1)
            for m in re.finditer(r"^\|\s*(W-\d{2})\b", _badan, re.M)
        }
        for _w in core.WARISAN_ITEMS:
            if _w not in _baris_dideklarasikan:
                errors.append(
                    f"_meta/SYSTEM_MANIFEST.md Warisan Meta: butir {_w} tidak punya BARIS deklarasi "
                    "`| " + _w + " …` — induk wajib menyatakan statusnya sendiri (gap boleh, "
                    "tapi wajib dinyatakan sebagai baris, bukan disebut di prosa)"
                )

# --- Daftar Pekerjaan Terbuka: utang tidak boleh DITUTUP tanpa bukti ---------
# Dibuat 17 Sep 2026 menjawab pertanyaan pemilik "nantinya semuanya diselesaikan dan
# dimatangkan tanpa ada yang terlupakan kan?". Daftar yang hanya hidup di ingatan agent
# atau tersebar di beberapa dokumen TIDAK bisa menjawab itu. Yang bisa: daftar yang
# (a) tidak bisa dihapus tanpa validator protes — berkasnya ada di CORE_REQUIRED, dan
# (b) tidak bisa ditutup tanpa bukti — dicek di sini.
_daftar_path = ROOT / "_meta/DAFTAR_PEKERJAAN_TERBUKA.md"
if _daftar_path.is_file():
    _STATUS_SAH = {"TERBUKA", "TERTAHAN", "SELESAI", "DITOLAK"}
    _dt = core.strip_code_fences(_daftar_path.read_text(encoding="utf-8"))
    _ids: list[str] = []
    for _ln, _l in enumerate(_dt.splitlines(), 1):
        if not _l.lstrip().startswith("|"):
            continue
        _sel = [x.strip() for x in _l.strip().strip("|").split("|")]
        if len(_sel) < 4 or not re.fullmatch(r"T-\d{2}", _sel[0]):
            continue  # header, pemisah, atau baris non-item
        _ids.append(_sel[0])
        _status = next((x for x in _sel if x in _STATUS_SAH), "")
        if not _status:
            errors.append(
                f"_meta/DAFTAR_PEKERJAAN_TERBUKA.md:{_ln}: item {_sel[0]} tidak punya status sah "
                f"(salah satu {sorted(_STATUS_SAH)}) — item tanpa status tidak bisa dilacak"
            )
        elif _status == "SELESAI" and not re.search(r"\b[0-9a-f]{7,40}\b", _sel[-1]):
            errors.append(
                f"_meta/DAFTAR_PEKERJAAN_TERBUKA.md:{_ln}: item {_sel[0]} ber-status SELESAI tetapi "
                "sel Bukti tidak menyebut sha commit — MENUTUP UTANG TANPA BUKTI dilarang "
                "(kalau fix-nya belum di-commit, biarkan TERBUKA dan tulis sha-nya nanti)"
            )
    for _d in sorted({i for i in _ids if _ids.count(i) > 1}):
        errors.append(
            f"_meta/DAFTAR_PEKERJAAN_TERBUKA.md: ID {_d} dipakai lebih dari sekali — ID wajib unik "
            "dan tidak boleh dipakai ulang, termasuk untuk item yang sudah ditutup"
        )
    if not _ids:
        errors.append(
            "_meta/DAFTAR_PEKERJAAN_TERBUKA.md tidak memuat satu pun baris item berpola `| T-nn …` — "
            "daftar utang yang kosong tanpa deklarasi eksplisit tidak bisa dibedakan dari daftar yang rusak"
        )

# --- Masukan pemilik yang TERCATAT wajib punya RESPONS yang bisa diperiksa ----
# Instruksi pemilik 17 Sep 2026: "jangan cuma dicatat tapi juga harus direspon/dieksekusi".
# Tiga hal ditegakkan di sini, karena "harus dibaca" yang hanya berupa imbauan akan dilupakan:
#   (a) setiap penanda tuntutan T<n> di DISKUSI_MENTAH wajib punya baris di ledger tanggapan;
#   (b) status ledger wajib dari kosakata tertutup - "TERCATAT" BUKAN status sah;
#   (c) status TERJADWAL wajib menunjuk ID item yang BENAR-BENAR ADA di daftar utang;
#   (d) kewajiban membaca kedua berkas di langkah awal sesi tidak boleh hilang diam-diam.
_LEDGER = ROOT / "_meta/TANGGAPAN_MASUKAN_PEMILIK.md"
_DAFTAR_UTANG = ROOT / "_meta/DAFTAR_PEKERJAAN_TERBUKA.md"
_STATUS_RESPONS = {"DIEKSEKUSI", "DIJAWAB", "DITOLAK", "MENUNGGU PEMILIK", "TERJADWAL"}
if _LEDGER.is_file():
    _lt = core.strip_code_fences(_LEDGER.read_text(encoding="utf-8"))
    _baris_ledger: dict[str, tuple[int, str, str]] = {}
    for _ln, _l in enumerate(_lt.splitlines(), 1):
        if not _l.lstrip().startswith("|"):
            continue
        _sel = [y.strip() for y in _l.strip().strip("|").split("|")]
        # T<n> tanpa strip = tuntutan pemilik; S-<nn> = instruksi berdiri.
        # JANGAN disamakan dengan T-<nn> (dengan strip) = item utang di daftar pekerjaan terbuka.
        if len(_sel) < 3 or not re.fullmatch(r"T\d{1,2}|S-\d{2}", _sel[0]):
            continue
        _baris_ledger[_sel[0]] = (_ln, _sel[-2], _sel[-1])

    # (a) setiap T<n> yang tercatat di DISKUSI_MENTAH wajib punya baris tanggapan
    _t_tercatat: set[str] = set()
    for _d in sorted((ROOT / "_meta" / "_internal").glob("DISKUSI_MENTAH_*.md")):
        for _m in re.finditer(r"\bT(\d{1,2})\b", core.strip_code_fences(
                _d.read_text(encoding="utf-8", errors="replace"))):
            _t_tercatat.add(f"T{int(_m.group(1))}")
    for _tid in sorted(_t_tercatat):
        if _tid not in _baris_ledger:
            errors.append(
                f"_meta/TANGGAPAN_MASUKAN_PEMILIK.md: tuntutan {_tid} TERCATAT di DISKUSI_MENTAH tetapi "
                "TIDAK PUNYA BARIS TANGGAPAN - pemilik menginstruksikan 17 Sep 2026 bahwa yang tercatat "
                "wajib direspons/dieksekusi, bukan cuma dicatat"
            )

    # (b)+(c) status sah + bukti tidak kosong + TERJADWAL menunjuk item nyata
    _teks_utang = (_DAFTAR_UTANG.read_text(encoding="utf-8")
                   if _DAFTAR_UTANG.is_file() else "")
    _id_utang = set(re.findall(r"^\|\s*(T-\d{2})\b", _teks_utang, re.M))
    for _tid, (_ln, _status, _bukti) in sorted(_baris_ledger.items()):
        if _status not in _STATUS_RESPONS:
            errors.append(
                f"_meta/TANGGAPAN_MASUKAN_PEMILIK.md:{_ln}: {_tid} ber-status '{_status}' yang TIDAK SAH "
                f"(wajib salah satu {sorted(_STATUS_RESPONS)}) - 'TERCATAT'/'terbuka'/kosong "
                "bukan tanggapan"
            )
        elif not _bukti or _bukti in {"-", "—", ""}:
            errors.append(
                f"_meta/TANGGAPAN_MASUKAN_PEMILIK.md:{_ln}: {_tid} ber-status {_status} tetapi sel bukti "
                "KOSONG - tanggapan tanpa bukti tidak bisa diperiksa"
            )
        elif _status == "TERJADWAL":
            _dirujuk = set(re.findall(r"\bT-\d{2}\b", _bukti))
            if not _dirujuk:
                errors.append(
                    f"_meta/TANGGAPAN_MASUKAN_PEMILIK.md:{_ln}: {_tid} ber-status TERJADWAL tetapi tidak "
                    "menunjuk ID item di _meta/DAFTAR_PEKERJAAN_TERBUKA.md - 'nanti dikerjakan' tanpa "
                    "tempat di daftar utang = memindahkan diam ke tempat lain"
                )
            else:
                for _r in sorted(_dirujuk - _id_utang):
                    errors.append(
                        f"_meta/TANGGAPAN_MASUKAN_PEMILIK.md:{_ln}: {_tid} ber-status TERJADWAL menunjuk "
                        f"item {_r} yang TIDAK ADA di _meta/DAFTAR_PEKERJAAN_TERBUKA.md"
                    )

    # (d) kewajiban membaca di langkah awal sesi tidak boleh hilang
    _nsp = ROOT / "_meta/NEXT_SESSION_PROMPT.md"
    if _nsp.is_file():
        _nt = _nsp.read_text(encoding="utf-8")
        for _wajib in ("_meta/DAFTAR_PEKERJAAN_TERBUKA.md", "_meta/TANGGAPAN_MASUKAN_PEMILIK.md"):
            if _wajib not in _nt:
                errors.append(
                    f"_meta/NEXT_SESSION_PROMPT.md tidak mewajibkan membaca {_wajib} di langkah awal sesi "
                    "- daftar yang tidak pernah dibaca akan dilupakan walaupun isinya lengkap"
                )

# --- Meta manifest: Status dan Versi harus bergerak bersama -----------------
# Sebab cek ini ada (ditemukan 18 Sep 2026, bukan dicari-cari): pada dua bump terakhir
# field `Versi` dinaikkan sementara `Status` tertinggal di `Released — v1.20.0`, padahal
# di `main` keduanya sama dan di commit v1.20.0 keduanya sama. Dua angka di dua tempat
# tanpa penjaga adalah pola D-2 yang sudah pernah menggigit repo ini (jumlah skenario FI
# vs dokumennya), jadi dijaga alat — bukan mata, dan bukan dicatat lalu ditinggal.
_MM = ROOT / "_meta/SYSTEM_MANIFEST.md"
if _MM.is_file():
    _mmt = _MM.read_text(encoding="utf-8")
    _st = re.search(r"^- \*\*Status:\*\* `Released — v([0-9]+\.[0-9]+\.[0-9]+)`$", _mmt, re.MULTILINE)
    _vs = re.search(r"^- \*\*Versi:\*\* `([0-9]+\.[0-9]+\.[0-9]+)`$", _mmt, re.MULTILINE)
    if not _st:
        errors.append(
            "_meta/SYSTEM_MANIFEST.md: field Status tidak berbentuk `Released — vX.Y.Z` - "
            "bentuk itu yang dipakai mendeteksi drift terhadap field Versi"
        )
    elif not _vs:
        errors.append("_meta/SYSTEM_MANIFEST.md: field Versi tidak berbentuk `X.Y.Z`")
    elif _st.group(1) != _vs.group(1):
        errors.append(
            f"_meta/SYSTEM_MANIFEST.md: Status menyebut v{_st.group(1)} tetapi Versi {_vs.group(1)} - "
            "keduanya bergerak bersama (di main dan di commit v1.20.0 keduanya sama). Naikkan KEDUANYA "
            "di commit yang sama; JANGAN melonggarkan cek ini supaya cocok dengan manifest yang tertinggal."
        )

# --- Index-driven system coverage (inheritance contract) -------------------
INDEX_PATH = ROOT / "_meta/INDEKS_SISTEM.md"
index_text = INDEX_PATH.read_text(encoding="utf-8") if INDEX_PATH.is_file() else ""
if not INDEX_PATH.is_file():
    errors.append("missing _meta/INDEKS_SISTEM.md")
elif "## Daftar Sistem" not in index_text:
    errors.append("INDEKS_SISTEM has no 'Daftar Sistem' section")

index_folders, index_errors = core.parse_index(index_text)
errors += [f"INDEKS_SISTEM: {e}" for e in index_errors]

if core.EXACT_PILOT in index_folders:
    errors.append("pilot must not be listed as an active system")

# Every sistem-* folder on disk (except the pilot fixture, by exact name)
# must be registered — exact match, no substring exceptions (review F2).
for sys_dir in sorted(list(ROOT.glob("sistem/sistem-*/")) + list(ROOT.glob("sistem-*/"))):
    rel_name = sys_dir.relative_to(ROOT).as_posix()
    if rel_name == core.EXACT_PILOT or sys_dir.name == core.EXACT_PILOT:
        continue
    if rel_name not in index_folders and sys_dir.name not in index_folders:
        errors.append(
            f"system folder {rel_name}/ not registered in INDEKS_SISTEM 'Daftar Sistem'"
        )

# Inheritance-contract checks for each REGISTERED system (03_KONTRAK_WARISAN).
for name in index_folders:
    sys_dir = ROOT / name
    if not sys_dir.is_dir():
        errors.append(f"INDEKS lists {name}/ but the folder does not exist")
        continue
    manifest = sys_dir / "SYSTEM_MANIFEST.md"
    if not manifest.is_file():
        errors.append(f"{name}: missing SYSTEM_MANIFEST.md (W-04)")
        continue
    mtext = manifest.read_text(encoding="utf-8")
    ovr = core.overridden_items(mtext)
    relax = core.manifest_tahap(mtext) == "kerangka"

    def relaxed(msg):
        (stage_warnings if relax else errors).append(msg)

    errors += core.warisan_errors(name, mtext)
    if "W-07" not in ovr and "Dipakai via lmarena" not in mtext:
        errors.append(f"{name}: SYSTEM_MANIFEST.md lacks 'Batasan Platform' (Dipakai via lmarena?) — W-07")
    if "W-01" not in ovr:
        if not (sys_dir / "PROMPT_ENTRI_UNIVERSAL.md").is_file():
            relaxed(f"{name}: missing PROMPT_ENTRI_UNIVERSAL.md (pegangan, W-01)")
        if not ((sys_dir / "PANDUAN_PENGGUNA.md").is_file() or (sys_dir / "panduan" / "PANDUAN_PENGGUNA.md").is_file()):
            relaxed(f"{name}: missing PANDUAN_PENGGUNA.md (root or panduan/) — pegangan wajib (W-01)")
    if "W-02" not in ovr:
        descent = any(
            "LOG_SESI" in f.read_text(encoding="utf-8")
            for pat in (f"{name}/*.md", f"{name}/_sistem/*.md", f"{name}/panduan/*.md")
            for f in ROOT.glob(pat)
        )
        if not descent:
            relaxed(f"{name}: LOG_SESI mechanism not descended into the system folder (W-02, self-contained requirement)")
    if "W-03" not in ovr:
        if not core.unit_status_files(sys_dir):
            relaxed(f"{name}: no unit STATUS.md found — registered system must have at least one unit (W-03)")
    # Kewajiban folder sistem: setiap sistem terdaftar wajib punya validator
    # sendiri yang self-contained. Daftar kewajibannya statis (gaya
    # CORE_REQUIRED), bukan hasil penemuan. Sistem `Tahap: kerangka` belum
    # punya isi untuk divalidasi, jadi ia ikut pelonggaran lifecycle yang
    # sama dengan W-01..W-03 — bukan pelonggaran baru.
    for rel in core.SYSTEM_REQUIRED_FILES:
        if not (sys_dir / rel).is_file():
            relaxed(f"{name}: missing {rel} — validator sistem wajib")

# --- Deterministic checkpoint field check (C-01, generalized per M-03) -----
# Every unit STATUS.md under any sistem-*/ dir (any layout — enumeration,
# not a fixed pattern list) must carry the field exactly once, outside
# quotes/fences. Template STATUS files must parse to the exact safe value.
for sys_dir in sorted(list(ROOT.glob("sistem/sistem-*/")) + list(ROOT.glob("sistem-*/"))):
    for status_path in core.unit_status_files(sys_dir):
        rel = status_path.relative_to(ROOT).as_posix()
        kind, value = core.parse_unsaved_field(status_path.read_text(encoding="utf-8"))
        if kind == "absent":
            errors.append(f"STATUS missing field Pekerjaan belum tersimpan: {rel}")
        elif kind == "ambiguous":
            errors.append(
                f"STATUS field Pekerjaan belum tersimpan muncul lebih dari sekali (bukti ganda = tidak deterministik): {rel}"
            )
        else:
            if not value:
                errors.append(f"STATUS empty Pekerjaan belum tersimpan value: {rel}")
            elif value != core.SAFE_VALUE and "tidak ada" in value.lower():
                # Free text that is NOT an exact "none" claim must not
                # pretend to be one; honest pending-work lists (no
                # "tidak ada" wording) are judged by the gate (FI), here.
                errors.append(f"STATUS must use exact 'Tidak ada' (case-sensitive): {rel}: {value}")
    for tmpl in sorted(
        set(sys_dir.glob("STATUS_TEMPLATE.md"))
        | set(sys_dir.glob("_sistem/STATUS_TEMPLATE.md"))
        | set(sys_dir.glob("_template/T*_STATUS.md"))
    ):
        rel = tmpl.relative_to(ROOT).as_posix()
        kind, value = core.parse_unsaved_field(tmpl.read_text(encoding="utf-8"))
        if kind == "absent":
            errors.append(f"STATUS template missing field: {rel}")
        elif kind == "ambiguous":
            errors.append(f"STATUS template field Pekerjaan belum tersimpan ambigu (duplikat/kutipan): {rel}")
        elif value != core.SAFE_VALUE:
            errors.append(
                f"STATUS template nilai field harus exact '{core.SAFE_VALUE}' "
                f"(petunjuk pengisian bukan bagian dari nilai — review F8): {rel} (ditemui: {value!r})"
            )

# --- Warning-tier path reference check (A-B3a, extended by M-01/M-03) -----
# Scope: ditentukan SATU definisi "dokumen aktif" di checkpoint_core
# (ACTIVE_DOC_GLOBS + ACTIVE_DOC_EXCLUDE_DIRS + ACTIVE_DOC_EXCLUDE_NAMES +
# dokumen_aktif()). Deliberate exclusions (sekarang hidup di satu tempat):
#   * `_internal/` — historical audit references, not active instructions
#     (and never shipped in the clean template, so references to it can
#     never be an operational dependency);
#   * unit living dirs (deck-aktif, unit-aktif, _produksi-aktif) — per-unit
#     work state, checked by the C-01 rules and the systems' own tools;
#   * `00_RENCANA_KERANGKA.md` — plan document kept as history; the final
#     numbering is documented in-file ("Catatan renumbering 5 Sep");
#   * `ACCEPTANCE_TEST_LOG.md` — test-run records (bukti run); menulis bukti
#     tidak boleh mengubah isi paket;
#   * `DISKUSI_MENTAH*` — diskusi mentah discovery, bukan aturan aktif.
# SCOPED resolution (review F13): a document inside a system folder resolves
# paths against its OWN system (+ _meta + root) — it can no longer borrow a
# file from another system to mask a missing local dependency. Master-level
# docs (root, _meta) stay cross-system: pointing between systems is their
# job. URIs are not repository paths (review F14).
ARTIFACT_PREFIXES = ("_meta/_internal/",)
REF_RE = re.compile(r"`([^`\n]+)`")
PATH_EXTENSIONS = (".md", ".py", ".zip", ".json")


def system_roots(name):
    roots = [
        name, f"{name}/_sistem", f"{name}/panduan",
        f"{name}/_generator", f"{name}/_template", f"{name}/_produksi-aktif",
    ]
    for unit in sorted((ROOT / name / "deck-aktif").glob("*")):
        if unit.is_dir():
            roots.append(f"{name}/{unit.parent.name}/{unit.name}")
    # Sistem konten kreator menyimpan arsip per channel; dokumen aktifnya
    # menulis `arsip-naskah/indeks.md` RELATIF terhadap folder channel.
    # Fixture channel menyediakan basis resolusi yang deterministik.
    if (ROOT / name / "channel-fixture-narasi-sejarah").is_dir():
        roots.append(f"{name}/channel-fixture-narasi-sejarah")
    return roots


ALL_ROOTS = ["", "_meta", "_meta/_internal", core.EXACT_PILOT]
for _name in index_folders:
    ALL_ROOTS += system_roots(_name)


def doc_roots(doc_rel):
    parts = doc_rel.split("/")
    if len(parts) >= 2 and parts[0] == "sistem" and f"sistem/{parts[1]}" in index_folders:
        sys_name = f"sistem/{parts[1]}"
        return system_roots(sys_name) + ["_meta", "_meta/_internal", ""]
    first = parts[0]
    if first.startswith("sistem-") and first in index_folders:
        return system_roots(first) + ["_meta", "_meta/_internal", ""]
    return ALL_ROOTS


def active_documents():
    """Active documents in scope (single definition: checkpoint_core)."""
    docs = set(core.dokumen_aktif(ROOT, None))
    for _name in index_folders:
        docs.update(core.dokumen_aktif(ROOT, _name))
    return sorted(docs)


def is_path_like(ref):
    # URIs (http://, https://, mailto:, ...) are external, not repository
    # paths (review F14). "[", "<", "*" are placeholders/glob patterns;
    # spaces mean a command line (e.g. `python3 tools/validate_repo.py`);
    # absolute paths ("/tmp/...") are external evidence. Bare filenames in
    # prose are not judged: resolving them needs a writing convention this
    # repository has not adopted.
    if "://" in ref or re.match(r"^[a-z][a-z0-9+.-]*:", ref, re.IGNORECASE):
        return False
    return (
        "/" in ref
        and not any(c in ref for c in ("[", "<", "*", " "))
        and not ref.startswith("/")
        and ref.lower().endswith(PATH_EXTENSIONS)
    )


def resolves(ref, doc_rel):
    if any(ref.startswith(p) for p in ARTIFACT_PREFIXES):
        return True  # _internal: historical area, never an operational dependency
    return any((ROOT / base / ref).is_file() for base in doc_roots(doc_rel))


def scan_references():
    docs = active_documents()
    checked = 0
    warnings = []
    for path in docs:
        rel = path.relative_to(ROOT).as_posix()
        for lineno, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for match in REF_RE.finditer(line):
                ref = match.group(1)
                if not is_path_like(ref):
                    continue
                checked += 1
                if resolves(ref, rel):
                    continue
                warnings.append(
                    f"WARNING reference: {rel}:{lineno}: "
                    f"unresolved path reference `{ref}`"
                )
    return docs, checked, warnings


ref_docs, ref_checked, ref_warnings = scan_references()
ref_warnings += stage_warnings

# ---------------------------------------------------------------------------
# Penjaga field `- **Keadaan:**` di setiap log sesi (usulan hakim putaran 5 PR #74,
# temuan #6). Tanpa penjaga ini header "Keadaan Sesi" bisa BASI atau HILANG tanpa ada
# yang protes - persis yang lolos pada LOG_SESI_2026-09-17.md (basi sejak 6f60c7c:
# menulis folder sistem-undangan "belum dibuat" padahal ada) dan pada log lanjutan
# slot 24 (tidak punya blok Keadaan Sesi sama sekali padahal template mewajibkannya).
# Nilai yang sah hanya OPEN atau CLOSED; nilai lain ("menunggu gerbang ...") membuat
# agent berikutnya tidak tahu apakah log ini masih hidup. Fail-closed: folder log yang
# hilang atau kosong juga error. Cakupan: semua `_log-sesi/LOG_SESI_*.md`, termasuk
# yang diturunkan ke folder sistem (butir warisan W-02).
# ---------------------------------------------------------------------------
_LOG_DIKECUALIKAN = {".git", "backups", "template_clean", "node_modules", "__pycache__"}
_pola_keadaan = re.compile(r"^- \*\*Keadaan:\*\*\s*`?(OPEN|CLOSED)`?", re.M)
_berkas_log = sorted(
    p for p in ROOT.rglob("LOG_SESI_*.md")
    if "_log-sesi" in p.parts and not (_LOG_DIKECUALIKAN & set(p.parts))
)
# Fail-closed HANYA bila folder lognya ada: repo meta wajib punya log sesi, sedangkan ekstrak
# template (benih sistem baru) memang TIDAK memuat folder `_log-sesi/` karena riwayat sesi adalah
# data personal yang sengaja dikecualikan dari template - menuntut log di sana akan merusak
# TEMPLATE CLEAN BUILD. Kalau foldernya ada tapi kosong, itu berarti lognya dipindahkan/dihapus
# untuk membungkam penjaga, dan itu error.
if (ROOT / "_log-sesi").is_dir() and not _berkas_log:
    errors.append(
        "_log-sesi/: foldernya ada tetapi tidak memuat LOG_SESI_*.md - penjaga field "
        "`- **Keadaan:**` tidak bisa berjalan (fail-closed: log sesi tidak boleh dipindahkan "
        "atau dikosongkan untuk membungkam penjaga)"
    )
for _lg in _berkas_log:
    if not _pola_keadaan.search(_lg.read_text(encoding="utf-8")):
        errors.append(
            f"{_lg.relative_to(ROOT)}: field wajib `- **Keadaan:**` bernilai OPEN atau CLOSED "
            "tidak ada (atau nilainya di luar dua itu) - header 'Keadaan Sesi' harus menyatakan "
            "keadaan log ini supaya agent berikutnya tahu log ini masih hidup atau sudah "
            "arsip; tambahkan field-nya sebagai append bertanggal, jangan sunting riwayatnya"
        )

if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    for w in ref_warnings:
        print(w)
    sys.exit(1)

# The line below is quoted verbatim by _meta/_internal/HANDOFF_NEXT_SESSION.md
# and by audit records on other branches. Keep the FORMAT byte-identical;
# the count is live data and moves with the required set.
print(f"VALIDATION PASSED: {len(required)} required files and Markdown invariants checked")
print(
    f"COVERAGE: {len(ref_docs)} active documents scanned, "
    f"{ref_checked} path references checked, {len(ref_warnings)} unresolved"
)
print(f"SYSTEMS CHECKED (inheritance contract): {len(index_folders)} registered + pilot excluded by design")
for w in ref_warnings:
    print(w)
for w in tabel_warnings:
    print(w)
_jumlah_warning = len(ref_warnings) + len(tabel_warnings)
if _jumlah_warning:
    print(f"WARNINGS: {_jumlah_warning} (warning tier, exit code unaffected)")
else:
    print("WARNINGS: none")
