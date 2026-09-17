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
- Review F9: Warisan enforcement — all nine items W-01..W-09 present in the
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
        # butir (W-01…W-09)" sudah memenuhi syarat walau baris deklarasinya dihapus.
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
if ref_warnings:
    print(f"WARNINGS: {len(ref_warnings)} (warning tier, exit code unaffected)")
else:
    print("WARNINGS: none")
