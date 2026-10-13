#!/usr/bin/env python3
"""Kiểm tra nội dung repo và toàn bộ blob reachable trong lịch sử Git."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECRET_PATTERNS = [
    re.compile(rb"sk-[A-Za-z0-9]{20,}"),
    re.compile(rb"sk_(?:live|test)_[A-Za-z0-9]{16,}"),
    re.compile(rb"sb_secret_[A-Za-z0-9_-]{10,}"),
    re.compile(rb"AKIA[0-9A-Z]{16}"),
    re.compile(rb"ASIA[0-9A-Z]{16}"),
    re.compile(rb"ghp_[A-Za-z0-9]{36}"),
    re.compile(rb"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(rb"gh[so]_[A-Za-z0-9]{20,}"),
    re.compile(rb"glpat-[A-Za-z0-9_-]{20,}"),
    re.compile(rb"xox[baprs]-[A-Za-z0-9-]{20,}"),
    re.compile(rb"AIza[0-9A-Za-z_-]" + rb"{30,}"),
    re.compile((b"-" * 5) + rb"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
TEXT_EXTENSIONS = {".md", ".markdown", ".txt", ".json", ".yml", ".yaml", ".py"}


def run(*args: str) -> bytes:
    return subprocess.check_output(args, cwd=ROOT)


def tracked_files() -> list[Path]:
    raw = run("git", "ls-files", "-z")
    return [ROOT / item.decode("utf-8") for item in raw.split(b"\0") if item]


def check_paths(files: list[Path]) -> list[str]:
    failures: list[str] = []
    for path in files:
        if not path.is_symlink():
            continue
        target = path.resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            failures.append(f"symlink thoát khỏi repo: {path.relative_to(ROOT)} -> {target}")
    return failures


def check_bytes(data: bytes, label: str) -> list[str]:
    failures: list[str] = []
    if b"\xe2\x80\x93" in data or b"\xe2\x80\x94" in data:
        failures.append(f"ký tự gạch dài trong {label}")
    for pattern in SECRET_PATTERNS:
        if pattern.search(data):
            failures.append(f"secret-shaped string trong {label}: {pattern.pattern.decode('ascii', 'replace')}")
    return failures


def check_links(files: list[Path]) -> list[str]:
    failures: list[str] = []
    known = {p.relative_to(ROOT).as_posix() for p in files}
    for path in files:
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if not clean:
                continue
            candidate = (path.parent / clean).resolve()
            try:
                relative = candidate.relative_to(ROOT).as_posix()
            except ValueError:
                failures.append(f"link thoát khỏi repo: {path.relative_to(ROOT)} -> {target}")
                continue
            if relative not in known and not candidate.is_dir():
                failures.append(f"link không tồn tại: {path.relative_to(ROOT)} -> {target}")
    return failures


def check_metadata() -> list[str]:
    failures = check_bytes(run("git", "log", "--all", "--format=%B"), "commit messages")
    refs = run("git", "for-each-ref", "--format=%(objectname)", "refs/tags").decode("ascii", "replace").splitlines()
    for oid in refs:
        if run("git", "cat-file", "-t", oid).strip() == b"tag":
            failures.extend(check_bytes(run("git", "cat-file", "tag", oid), f"tag {oid}"))
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if event_path:
        try:
            event = json.loads(Path(event_path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"không đọc được GitHub event metadata: {exc}")
        else:
            pull = event.get("pull_request") or {}
            for name, value in (("PR title", pull.get("title")), ("PR body", pull.get("body"))):
                if value:
                    failures.extend(check_bytes(value.encode("utf-8"), name))
    return failures


def check_history() -> list[str]:
    failures: list[str] = []
    objects = run("git", "rev-list", "--objects", "--all").decode("utf-8", "replace").splitlines()
    seen: set[str] = set()
    for line in objects:
        oid = line.split(" ", 1)[0]
        if oid in seen:
            continue
        seen.add(oid)
        kind = run("git", "cat-file", "-t", oid).strip()
        if kind != b"blob":
            continue
        data = run("git", "cat-file", "blob", oid)
        failures.extend(check_bytes(data, f"blob {oid}"))
    return failures


def main() -> int:
    files = tracked_files()
    failures = check_paths(files)
    for path in files:
        if path.is_symlink():
            try:
                path.resolve().relative_to(ROOT)
            except ValueError:
                continue
        try:
            failures.extend(check_bytes(path.read_bytes(), path.relative_to(ROOT).as_posix()))
        except OSError as exc:
            failures.append(f"không đọc được {path}: {exc}")
    failures.extend(check_links(files))
    failures.extend(check_metadata())
    failures.extend(check_history())
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    head = os.environ.get("HEAD_SHA") or run("git", "rev-parse", "HEAD").decode("ascii").strip()
    base = os.environ.get("BASE_SHA", "not provided")
    checked_at = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    print(f"PASS: {len(files)} tracked files, current tree, metadata, and reachable Git history checked; base={base}; head={head}; checked_at={checked_at}; artifacts=none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
