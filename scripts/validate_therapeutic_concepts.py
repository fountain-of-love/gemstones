#!/usr/bin/env python3
"""Validate one gemstone's therapeutic concept graph contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path


CONCEPT_RE = re.compile(r"\[\[(concepts/(?:emotional|mental|physical)/[^]|]+)")


def frontmatter(text: str) -> str:
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError("missing YAML frontmatter")
    return parts[1]


def register_status(register: str) -> str:
    match = re.search(r"^Status:\s*(\w+)", register, re.MULTILINE)
    return match.group(1).lower() if match else "missing"


def print_errors(errors: list[str]) -> None:
    print("FAIL: therapeutic concept validation")
    for error in errors:
        print(f"- {error}")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_therapeutic_concepts.py gemstones/<slug>.md", file=sys.stderr)
        return 2

    gemstone = Path(sys.argv[1])
    root = Path.cwd()
    errors: list[str] = []
    if not gemstone.exists():
        errors.append(f"gemstone page does not exist: {gemstone}")
        print_errors(errors)
        return 1

    text = gemstone.read_text()
    try:
        fm = frontmatter(text)
    except ValueError as exc:
        errors.append(str(exc))
        print_errors(errors)
        return 1

    if "therapeutic_concepts:" not in fm:
        errors.append("missing therapeutic_concepts frontmatter")

    concept_ids = sorted(set(CONCEPT_RE.findall(text)))
    for concept_id in concept_ids:
        note = root / f"{concept_id}.md"
        if not note.exists():
            errors.append(f"missing canonical concept note: {concept_id}.md")
            continue
        note_text = note.read_text()
        note_frontmatter = note_text.split("---", 2)[1] if note_text.startswith("---") else ""
        vocabulary_id = concept_id.removeprefix("concepts/")
        dimension, concept_name = vocabulary_id.split("/", 1)
        required_note_fields = {
            "type": "therapeutic-concept",
            "dimension": dimension,
            "concept_id": vocabulary_id,
            "concept_kind": None,
        }
        for field, expected in required_note_fields.items():
            if not re.search(rf"^{field}:\s*", note_frontmatter, re.MULTILINE):
                errors.append(f"concept note lacks {field}: {note}")
            elif expected and not re.search(rf"^{field}:\s*{re.escape(expected)}\s*$", note_frontmatter, re.MULTILINE):
                errors.append(f"concept note has incorrect {field}: {note}")
        if "## Related Gemstones" not in note_text:
            errors.append(f"concept note lacks Related Gemstones section: {note}")
        gemstone_name = gemstone.stem.replace("-", " ").title()
        reciprocal = rf"\[\[(?:gemstones/)?{re.escape(gemstone.stem)}(?:\|[^]]+)?\]\]"
        if not (re.search(reciprocal, note_text, re.I) or re.search(rf"\[\[{re.escape(gemstone_name)}\]\]", note_text, re.I)):
            errors.append(f"concept note lacks reciprocal gemstone link: {note}")

    # Each frontmatter entry must expose provenance fields.
    entries = re.findall(r"(?ms)^\s+- concept:.*?(?=^\s+- concept:|\Z)", fm)
    for entry in entries:
        for field in ("relation", "source", "scope"):
            if not re.search(rf"^\s+{field}:\s*\S+", entry, re.MULTILINE):
                errors.append(f"frontmatter concept entry lacks {field}: {entry.splitlines()[0].strip()}")

    register = root / "concept-coverage" / f"{gemstone.stem}.md"
    if not register.exists():
        errors.append(f"missing coverage register: {register}")
    else:
        register_text = register.read_text()
        status = register_status(register_text)
        if status == "missing":
            errors.append(f"coverage register lacks Status: {register}")
        if re.search(r"\bPending\b|\bIn progress\b", register_text, re.I):
            errors.append("coverage register contains unresolved Pending/In progress text")
        if status == "reconciled" and re.search(r"\bBlocked\b", register_text, re.I):
            errors.append("reconciled register still contains blocked work")

    if errors:
        print_errors(errors)
        return 1

    print(f"PASS: {gemstone} ({len(concept_ids)} canonical concept targets checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
