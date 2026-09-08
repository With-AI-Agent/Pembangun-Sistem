#!/usr/bin/env python3
"""Gerbang folder sistem mandiri.

Alat ini berjalan di repo master. Ia menyalin HANYA folder sistem ke direktori
sementara, menjalankan validator sistem dari salinan itu, lalu memeriksa bahwa
rujukan operasional yang keluar folder sudah divendor sebagai salinan berlabel.
Exit 0 dari alat ini adalah definisi mekanis "folder sistem = deliverable".
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
core = None
LABEL_RE = re.compile(
    r"^> Salinan turunan\. Sumber: (?P<src>[^\s]+) sha (?P<sha>[0-9a-f]{40}) "
    r"tanggal (?P<date>\d{4}-\d{2}-\d{2}) versi-meta (?P<meta>\d+\.\d+\.\d+)$"
)
REF_RE = re.compile(r"`([^`\n]+)`")
TEXT_SUFFIXES = {
    "", ".md", ".txt", ".py", ".json", ".yaml", ".yml", ".toml", ".csv",
    ".gitignore", ".gitattributes",
}
DERIVED_TOPLEVELS = {"_meta", "tools", "_salinan", "_salinan-meta", "salinan"}
NO_DIFF_VALUES = {"", "-", "tidak ada", "none", "no difference", "identik"}


@dataclass
class Finding:
    code: str
    message: str


@dataclass
class LabelInfo:
    rel: str
    source: str
    source_sha: str
    date: str
    meta_version: str
    body: bytes
    lines: list[str]
    declared_difference: str = ""


@dataclass
class SystemResult:
    name: str
    temp_root: Path
    copied_root: Path
    validator_returncode: int
    validator_stdout: str
    validator_stderr: str
    findings: list[Finding] = field(default_factory=list)
    labels: list[LabelInfo] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.validator_returncode == 0 and not self.findings


def is_master_repo() -> bool:
    return (ROOT / "_meta").is_dir()


def read_index_systems() -> tuple[list[str], list[str]]:
    index = ROOT / "_meta" / "INDEKS_SISTEM.md"
    if not index.is_file():
        return [], ["_meta/INDEKS_SISTEM.md tidak ada"]
    folders, errors = core.parse_index(index.read_text(encoding="utf-8"))
    return folders, errors


def is_text_file(path: Path) -> bool:
    if path.name in {".gitignore", ".gitattributes"}:
        return True
    return path.suffix.lower() in TEXT_SUFFIXES


def safe_read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def split_label(data: bytes) -> tuple[list[str], bytes] | None:
    lines = data.splitlines(keepends=True)
    if len(lines) < 3:
        return None
    try:
        first3 = [line.decode("utf-8").rstrip("\r\n") for line in lines[:3]]
    except UnicodeDecodeError:
        return None
    return first3, b"".join(lines[3:])


def label_info_for(path: Path, rel: str, findings: list[Finding]) -> LabelInfo | None:
    try:
        data = path.read_bytes()
    except OSError as exc:
        findings.append(Finding("LABEL-READ", f"{rel}: tidak bisa dibaca: {exc}"))
        return None
    split = split_label(data)
    if split is None:
        return None
    first3, body = split
    if not first3[0].startswith("> Salinan turunan."):
        return None
    if not all(line.startswith("> ") for line in first3):
        findings.append(Finding("LABEL-FORMAT", f"{rel}: tiga baris label pertama wajib dimulai dengan '> '"))
        return None
    m = LABEL_RE.match(first3[0])
    if not m:
        findings.append(
            Finding(
                "LABEL-FORMAT",
                f"{rel}: baris pertama label tidak sesuai format wajib: '> Salinan turunan. Sumber: <jalur> sha <40> tanggal <YYYY-MM-DD> versi-meta <x.y.z>'",
            )
        )
        return None
    diff = ""
    for line in first3[1:]:
        dm = re.match(r"^>\s*Perbedaan\s*:\s*(.*)$", line, re.IGNORECASE)
        if dm:
            diff = dm.group(1).strip()
            break
    return LabelInfo(
        rel=rel,
        source=m.group("src"),
        source_sha=m.group("sha"),
        date=m.group("date"),
        meta_version=m.group("meta"),
        body=body,
        lines=first3,
        declared_difference=diff,
    )


def looks_like_unlabelled_derivative(rel: str) -> bool:
    parts = Path(rel).parts
    if not parts:
        return False
    if parts[0] in DERIVED_TOPLEVELS:
        return True
    return any("salinan" in part.lower() for part in parts)


def reference_token(raw: str) -> str:
    token = raw.strip()
    if not token:
        return token
    # Inline commands such as `tools/x.py --flag` still point at tools/x.py.
    token = token.split()[0]
    return token.rstrip(".,;:)")


def scan_system(system: str, copied_root: Path, findings: list[Finding]) -> list[LabelInfo]:
    labels: list[LabelInfo] = []
    labels_by_source: dict[str, list[LabelInfo]] = {}
    text_files = [p for p in sorted(copied_root.rglob("*")) if p.is_file() and is_text_file(p)]

    for path in text_files:
        rel = path.relative_to(copied_root).as_posix()
        info = label_info_for(path, rel, findings)
        if info:
            labels.append(info)
            labels_by_source.setdefault(info.source, []).append(info)
        elif looks_like_unlabelled_derivative(rel):
            findings.append(
                Finding(
                    "DERIVED-NO-LABEL",
                    f"{rel}: berkas berada di area salinan/turunan tetapi tiga baris label wajib tidak ada",
                )
            )

    for info in labels:
        src_rel = info.source
        if src_rel.startswith("/") or ".." in Path(src_rel).parts:
            findings.append(Finding("LABEL-SOURCE", f"{info.rel}: sumber label tidak boleh absolut/naik direktori: {src_rel}"))
            continue
        src_path = ROOT / src_rel
        if not src_path.is_file():
            findings.append(Finding("LABEL-SOURCE", f"{info.rel}: sumber label tidak ada di master: {src_rel}"))
            continue
        src_bytes = src_path.read_bytes()
        actual_sha = hashlib.sha1(src_bytes).hexdigest()
        if info.source_sha != actual_sha:
            findings.append(
                Finding(
                    "STALE-COPY",
                    f"{info.rel}: sha label {info.source_sha} tidak cocok dengan sha sumber master {src_rel} ({actual_sha})",
                )
            )
        diff_declared = info.declared_difference.strip().lower() not in NO_DIFF_VALUES
        if info.body != src_bytes and not diff_declared:
            findings.append(
                Finding(
                    "STALE-COPY",
                    f"{info.rel}: isi badan salinan tidak sama byte dengan sumber master {src_rel} dan label tidak menyebut perbedaan",
                )
            )
        elif info.body != src_bytes and diff_declared:
            # Perbedaan yang dinyatakan bukan error; reviewer/PR wajib membaca catatan ini.
            pass

    for path in text_files:
        rel = path.relative_to(copied_root).as_posix()
        text = safe_read_text(path)
        if text is None:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for match in REF_RE.finditer(line):
                raw = match.group(1)
                token = reference_token(raw)
                if not token:
                    continue
                if token.startswith(f"{system}/"):
                    findings.append(
                        Finding(
                            "SELF-PREFIX",
                            f"{rel}:{lineno}: rujukan ke folder sendiri harus relatif terhadap folder sistem, bukan `{raw}`",
                        )
                    )
                if token.startswith("_meta/") or token.startswith("tools/"):
                    if token.endswith("/"):
                        findings.append(
                            Finding(
                                "MISSING-LABELED-COPY",
                                f"{rel}:{lineno}: rujukan `{raw}` menunjuk area master; salinan berlabel untuk direktori tidak ada di folder sistem",
                            )
                        )
                        continue
                    if token not in labels_by_source:
                        findings.append(
                            Finding(
                                "MISSING-LABELED-COPY",
                                f"{rel}:{lineno}: rujukan `{raw}` membutuhkan salinan berlabel dengan sumber {token} di dalam folder sistem",
                            )
                        )
    return labels


def run_validator(copied_root: Path) -> tuple[int, str, str]:
    validator = copied_root / "_sistem" / "validate_system.py"
    if not validator.is_file():
        return 127, "", "_sistem/validate_system.py tidak ada di salinan folder sistem\n"
    proc = subprocess.run(
        [sys.executable, "-B", "_sistem/validate_system.py"],
        cwd=str(copied_root),
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    return proc.returncode, proc.stdout, proc.stderr


def check_one(system: str, keep: bool) -> SystemResult:
    temp_root = Path(tempfile.mkdtemp(prefix=f"check-selfcontained-{system}-"))
    copied_root = temp_root / system
    shutil.copytree(
        ROOT / system,
        copied_root,
        ignore=shutil.ignore_patterns("__pycache__"),
    )
    v_rc, v_out, v_err = run_validator(copied_root)
    result = SystemResult(
        name=system,
        temp_root=temp_root,
        copied_root=copied_root,
        validator_returncode=v_rc,
        validator_stdout=v_out,
        validator_stderr=v_err,
    )
    if v_rc != 0:
        result.findings.append(Finding("VALIDATOR", f"validator sistem di salinan keluar {v_rc}"))
    result.labels = scan_system(system, copied_root, result.findings)
    if keep:
        result.notes.append(f"salinan dipertahankan: {copied_root}")
    return result


def cleanup(results: list[SystemResult], keep: bool) -> None:
    if keep:
        return
    for r in results:
        shutil.rmtree(r.temp_root, ignore_errors=True)


def render_result(result: SystemResult, report: bool) -> None:
    print(f"== {result.name} ==")
    print(f"salinan sementara: {result.copied_root}")
    print("$ python3 _sistem/validate_system.py")
    if result.validator_stdout:
        print(result.validator_stdout.rstrip())
    if result.validator_stderr:
        print("[stderr]")
        print(result.validator_stderr.rstrip())
    print(f"exit={result.validator_returncode}")
    for note in result.notes:
        print(note)
    print(f"salinan berlabel ditemukan: {len(result.labels)}")
    if report and result.labels:
        for info in result.labels:
            diff = info.declared_difference or "(tidak disebut)"
            print(f"  - {info.rel} <- {info.source} (sha {info.source_sha}; perbedaan: {diff})")
    print(f"temuan: {len(result.findings)}")
    if result.findings:
        if report:
            for f in result.findings:
                print(f"- [{f.code}] {f.message}")
        else:
            print("detail: jalankan ulang dengan --report untuk daftar temuan per baris")
    print("HASIL SISTEM: " + ("PASS" if result.ok else "FAIL"))
    print("")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="check_selfcontained.py",
        description="Cek bahwa folder sistem dapat menjadi deliverable mandiri.",
    )
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--sistem", help="nama folder sistem, mis. sistem-presentasi")
    group.add_argument("--semua", action="store_true", help="cek semua sistem terdaftar")
    ap.add_argument("--keep", action="store_true", help="pertahankan salinan sementara")
    ap.add_argument("--report", action="store_true", help="cetak detail salinan berlabel dan semua temuan")
    args = ap.parse_args(argv)

    if not is_master_repo():
        print("check_selfcontained.py adalah alat master; jalankan dari repo master yang memiliki _meta/. Repo/folder mandiri tidak memiliki mode tersembunyi untuk alat ini.")
        return 2

    global core
    try:
        import checkpoint_core as _core
    except Exception as exc:
        print(f"CHECK SELF-CONTAINED FAILED: checkpoint_core tidak bisa diimpor dari repo master: {exc}")
        return 2
    core = _core

    systems, index_errors = read_index_systems()
    if index_errors:
        print("CHECK SELF-CONTAINED FAILED: indeks sistem tidak bisa dipercaya")
        for e in index_errors:
            print(f"- {e}")
        return 2

    targets = systems if args.semua else [args.sistem]
    missing = [name for name in targets if not (ROOT / name).is_dir()]
    if missing:
        print("CHECK SELF-CONTAINED FAILED: folder sistem tidak ada")
        for name in missing:
            print(f"- {name}/")
        return 2

    print("CHECK SELF-CONTAINED — folder sistem = deliverable")
    print(f"root master: {ROOT}")
    print("mode: " + ("--semua" if args.semua else f"--sistem {args.sistem}"))
    print("aturan: salin HANYA folder sistem; jalankan validator sistem di salinan; rujukan _meta/tools harus punya salinan berlabel; rujukan ke folder sendiri harus relatif")
    print("")

    results = [check_one(system, args.keep) for system in targets]
    try:
        for result in results:
            render_result(result, args.report)
        ok = all(r.ok for r in results)
        print("HASIL AKHIR: " + ("PASS" if ok else "FAIL"))
        return 0 if ok else 1
    finally:
        cleanup(results, args.keep)


if __name__ == "__main__":
    sys.exit(main())
