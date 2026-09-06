#!/usr/bin/env python3
"""Reproduce the pinned PR16 review without echoing protected test text.

Read-only Git inspection; optional CI runs use disposable git-archive snapshots.
The exit status is 1 when the orientation scan detects the reported regression.
No branch checkout, stash, ref update, PR mutation, or production/test-run edit.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(subprocess.check_output(
    ["git", "rev-parse", "--show-toplevel"],
    cwd=Path(__file__).resolve().parent,
    text=True,
).strip())
MAIN = "454507e23c31376ecdfa85e5fc09442ac8269a8a"
HEAD = "437ceeb77c1223ea9fae290de061547ef2502b81"
BASIS = "d4e687c19aa6b170d070fad6b88d3afb0b980338"
SUBJECT = "5465096e82ea96b705c75ddf742592efcf3726d1"
FIRST = "1c11ba739d6aafb1d26353d5fc480d861888e66b"
RESPONSE_RECORD = "283b8d0a36804add703fabde91abc3208a3b78d4"
DOMAIN = "sistem-konten-kreator"
LOG = f"{DOMAIN}/ACCEPTANCE_TEST_LOG.md"
UNIT = f"{DOMAIN}/_produksi-aktif/fixture-narasi-sejarah-tiga-benda-di-meja-nenek"
MANIFEST = f"{DOMAIN}/SYSTEM_MANIFEST.md"
TOOLS = ("tools/validate_repo.py", "tools/test_failure_injection.py")
FIXED_ORIENTATION = [
    f"{DOMAIN}/_sistem/START_DI_SINI.md",
    f"{DOMAIN}/_sistem/00_CARA_PAKAI_SISTEM.md",
    f"{UNIT}/STATUS.md",
    f"{DOMAIN}/channel-fixture-narasi-sejarah/channel-brief.md",
    f"{DOMAIN}/channel-fixture-narasi-sejarah/model-konten/narasi-60-detik/brief.md",
    "_meta/INDEKS_SISTEM.md",
    MANIFEST,
]


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def blob(rev, path):
    return git("show", f"{rev}:{path}")


def emit(label, value):
    print(label + " " + json.dumps(value, ensure_ascii=False, sort_keys=True), flush=True)


def orientation(rev):
    paths = git("ls-tree", "-r", "--name-only", rev).decode().splitlines()
    return FIXED_ORIENTATION + [
        p for p in paths if "/" not in p and p.startswith("LOG_SESI")
    ]


def signatures():
    # Extract existing signatures by immutable source coordinates. Never print
    # their values or place them in command-line arguments or generated files.
    lines = blob(HEAD, LOG).decode().splitlines()
    primary = re.findall(r"`([^`]+)`", lines[924])[:2]
    broad = re.findall(r'"([^"\n]+)" = 0 hit', lines[905])[2]
    assert len(primary) == 2 and all(primary) and broad
    emit("signature_sources", {
        "P1_P2": f"{HEAD}:{LOG}:925",
        "P3": f"{HEAD}:{LOG}:906",
        "note": "P3 overlaps P2; counts are not independent exposed lines",
    })
    return primary + [broad]


def grep_pointers(rev, pattern, paths):
    result = subprocess.run(
        ["git", "grep", "-n", "-I", "-F", "-f", "-", rev, "--", *paths],
        cwd=ROOT, input=(pattern + "\n").encode(), capture_output=True,
    )
    if result.returncode not in (0, 1):
        raise RuntimeError("git grep failed; protected output not echoed")
    # Drop matched text, retaining only SHA:path:line.
    return [":".join(line.split(":", 3)[:3])
            for line in result.stdout.decode().splitlines()]


def github_metadata(patterns):
    # A GitHub comment is not a Git blob or a subject access log. Only metadata,
    # a digest, and presence booleans are emitted; the body stays in memory.
    data = json.loads(subprocess.check_output([
        "gh", "api", "repos/With-AI-Agent/Pembangun-Sistem/issues/comments/5556242435",
    ], cwd=ROOT))
    body = data["body"]
    emit("B4_metadata", {
        "id": data["id"], "url": data["html_url"],
        "created_at": data["created_at"], "updated_at": data["updated_at"],
        "body_sha256": hashlib.sha256(body.encode()).hexdigest(),
        "P1_P2_present": [p in body for p in patterns[:2]],
        "subject_read_proven": False,
    })
    for number, line in enumerate(body.splitlines(), 1):
        if "**B8" in line:
            spans = re.findall(r"`([^`]+)`", line)
            if spans and "|" in spans[0]:
                pattern = spans[0].split("|")[-1]
                hits = grep_pointers(HEAD, pattern, orientation(HEAD))
                emit("P4_original_B8", {
                    "comment_line": number, "head_hits": len(hits), "pointers": hits,
                })
                break
    else:
        emit("P4_original_B8", "source changed; manual review required")


def run_ci(rev):
    results = {}
    with tempfile.TemporaryDirectory(prefix="pr16-review-") as directory:
        archive = subprocess.Popen(
            ["git", "archive", rev], cwd=ROOT, stdout=subprocess.PIPE,
        )
        try:
            subprocess.run(["tar", "-x", "-C", directory],
                           stdin=archive.stdout, check=True)
        finally:
            archive.stdout.close()
        if archive.wait() != 0:
            raise RuntimeError("git archive failed")
        env = dict(os.environ)
        env.pop("FI_SKIP_NESTED", None)  # Run all regressions, not a reduced suite.
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        for tool in TOOLS:
            result = subprocess.run(
                [sys.executable, tool], cwd=directory, env=env,
                capture_output=True, text=True, timeout=240,
            )
            results[tool] = {
                "exit": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
            }
            emit("CI", {"revision": rev, "tool": tool, **results[tool]})
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ci", action="store_true", help="run both tools on both snapshots")
    parser.add_argument("--github", action="store_true", help="verify public B4 metadata")
    args = parser.parse_args()
    errors = []

    merge_base = git("merge-base", MAIN, HEAD).decode().strip()
    emit("pins", {"main": MAIN, "head": HEAD, "basis": BASIS,
                  "subject": SUBJECT, "merge_base": merge_base})
    if merge_base != MAIN:
        errors.append("merge-base mismatch")

    before, after = blob(MAIN, LOG), blob(HEAD, LOG)
    append_only = after.startswith(before)
    runs = re.findall(r"^## Run (\d+)\b", after.decode(), re.M)
    added_runs = re.findall(r"^## Run (\d+)\b", after[len(before):].decode(), re.M)
    emit("append", {
        "prefix_identical": append_only,
        "base_lines": len(before.splitlines()), "head_lines": len(after.splitlines()),
        "added_lines": len(after[len(before):].splitlines()),
        "base_sha256": hashlib.sha256(before).hexdigest(),
        "prefix_sha256": hashlib.sha256(after[:len(before)]).hexdigest(),
        "run_numbers": runs, "appended_run_numbers": added_runs,
        "run6_heading_count": len(re.findall(r"^#{1,6}\s+Run 6\b", after.decode(), re.M)),
    })
    if not append_only or runs != ["1", "2", "3", "4", "5", "7"] or added_runs != ["7"]:
        errors.append("append/run-number invariant failed")

    patterns = signatures()
    for rev in (BASIS, MAIN, HEAD):
        paths = orientation(rev)
        unique = set()
        emit("orientation_scope", {"revision": rev, "files": len(paths),
                                   "root_logs": len(paths) - len(FIXED_ORIENTATION)})
        for index, pattern in enumerate(patterns, 1):
            hits = grep_pointers(rev, pattern, paths)
            unique.update(hits)
            emit("orientation_signature", {"revision": rev, "id": f"P{index}",
                                           "hits": len(hits), "pointers": hits})
        emit("orientation_unique_lines", {"revision": rev, "count": len(unique)})
        if rev == HEAD and unique:
            errors.append("PR16 orientation contains protected signatures")

    old_log = "LOG_SESI_2026-09-06.md"
    basis_lines = blob(BASIS, old_log).decode().splitlines()
    for start, end in ((20, 26), (77, 81)):
        source = basis_lines[start - 1:end]
        emit("residual_preservation", {
            "source": f"{BASIS}:{old_log}:{start}-{end}",
            "identical_at_first": source == blob(FIRST, old_log).decode().splitlines()[start - 1:end],
            "identical_at_head": source == blob(HEAD, old_log).decode().splitlines()[start - 1:end],
            "read_extent_proven": False,
        })
    for rev in (FIRST, RESPONSE_RECORD):
        emit("commit_timestamp", git("show", "-s", "--format=%H %aI %cI %P", rev).decode().strip())
    emit("timestamp_limit", "Commit time is not an independently timestamped user message")

    base_boxes = re.findall(r"^\s*- \[([ xX])\]", blob(MAIN, MANIFEST).decode(), re.M)
    head_boxes = re.findall(r"^\s*- \[([ xX])\]", blob(HEAD, MANIFEST).decode(), re.M)
    emit("manifest_checkboxes", {"count": len(head_boxes), "states_unchanged": base_boxes == head_boxes})
    if base_boxes != head_boxes:
        errors.append("manifest gate states changed")
    for tool in (*TOOLS, "tools/checkpoint_core.py"):
        equal = blob(MAIN, tool) == blob(HEAD, tool)
        emit("tool_unchanged", {"path": tool, "equal": equal})
        if not equal:
            errors.append("tool changed: " + tool)

    changed = git("diff", "--name-only", MAIN + "..." + HEAD).decode().splitlines()
    sizes = {path: len(blob(HEAD, path)) for path in changed}
    emit("delta_hygiene", {
        "changed_blob_bytes": sizes,
        "new_paths": git("diff", "--diff-filter=A", "--name-only", MAIN + "..." + HEAD).decode().splitlines(),
        "non_markdown_paths": [p for p in changed if not p.endswith(".md")],
        "binary_paths": [p for p in changed if b"\0" in blob(HEAD, p)],
        "temp_paths": [p for p in changed if any(part in ("tmp", ".cache", "__pycache__") for part in Path(p).parts)],
        "version_035_locations": [f"{HEAD}:{p}:{i}" for p in changed
                                  for i, line in enumerate(blob(HEAD, p).decode().splitlines(), 1)
                                  if "0.3.5" in line],
    })
    check = subprocess.run(["git", "diff", MAIN + "..." + HEAD, "--check"],
                           cwd=ROOT, capture_output=True)
    emit("PR16_diff_check", {"exit": check.returncode, "output_bytes": len(check.stdout) + len(check.stderr)})
    if check.returncode:
        errors.append("PR16 whitespace check failed")

    if args.github:
        github_metadata(patterns)
    if args.ci:
        base_results = run_ci(merge_base)
        head_results = run_ci(HEAD)
        same = base_results == head_results
        emit("CI_baseline_comparison", {"identical_results": same,
                                        "head_suite_all_green": all(r["exit"] == 0 for r in head_results.values())})
        if not same:
            errors.append("CI differs from merge-base")

    emit("mechanical_blockers", errors)
    emit("manual_review", "Residual materiality is evaluated in README.md; grep alone cannot establish isolation")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
