#!/usr/bin/env python3
"""Validate Antigravity CLI skills in .agents/skills/."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".agents" / "skills"


def check_skill(skill_path: Path) -> list[str]:
    errors = []
    skill_file = skill_path / "SKILL.md"
    if not skill_file.exists():
        return [f"Missing SKILL.md in {skill_path.name}"]

    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return [f"{skill_path.name}/SKILL.md: Missing frontmatter start '---'"]

    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        return [f"{skill_path.name}/SKILL.md: Missing frontmatter closing '---'"]

    frontmatter = text[4:end_idx]
    body = text[end_idx + 5:].strip()

    if not re.search(r"(?m)^name:\s*\S+", frontmatter):
        errors.append(f"{skill_path.name}/SKILL.md: Missing 'name' in frontmatter")
    if not re.search(r"(?m)^description:\s*\S+", frontmatter):
        errors.append(f"{skill_path.name}/SKILL.md: Missing 'description' in frontmatter")

    if not body:
        errors.append(f"{skill_path.name}/SKILL.md: Empty body content")

    return errors


def main() -> None:
    if not SKILLS_DIR.exists():
        print(f"Skills directory not found: {SKILLS_DIR}", file=sys.stderr)
        sys.exit(1)

    skill_folders = [p for p in sorted(SKILLS_DIR.iterdir()) if p.is_dir()]
    if not skill_folders:
        print("No skill folders found in .agents/skills/", file=sys.stderr)
        sys.exit(1)

    total_errors = []
    for skill_folder in skill_folders:
        errors = check_skill(skill_folder)
        if errors:
            total_errors.extend(errors)

    if total_errors:
        print(f"Found {len(total_errors)} validation errors:")
        for err in total_errors:
            print(f"  ❌ {err}")
        sys.exit(1)

    print(f"✅ All {len(skill_folders)} Antigravity skills in {SKILLS_DIR.relative_to(ROOT)} are valid.")


if __name__ == "__main__":
    main()
