#!/usr/bin/env python3
"""
Sync memory rules -> CLAUDE.md
Triggered via PostToolUse hook when memory files are modified.
"""
import json
import sys
import os
import re

MEMORY_DIR = "/Users/hathuy/.claude/projects/-Users-hathuy-Documents-FPT-1/memory"
CLAUDE_MD = "/Users/hathuy/Documents/FPT-1/CLAUDE.md"
FEEDBACK_FILE = os.path.join(MEMORY_DIR, "feedback_conventions.md")

SYNC_START = "<!-- MEMORY_SYNC_START -->"
SYNC_END = "<!-- MEMORY_SYNC_END -->"


def extract_rules(content):
    body = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL).strip()
    rules = []
    for line in body.split('\n'):
        m = re.match(r'^\*\*Rule \d+ — (.+?)\.?\*\*', line)
        if m:
            rules.append(f"- {m.group(1)}.")
    return rules


def main():
    try:
        data = json.load(sys.stdin)
        file_path = data.get('tool_input', {}).get('file_path', '')
    except Exception:
        sys.exit(0)

    if not file_path or MEMORY_DIR not in file_path:
        sys.exit(0)

    if not os.path.exists(FEEDBACK_FILE):
        sys.exit(0)

    with open(FEEDBACK_FILE) as f:
        content = f.read()

    rules = extract_rules(content)
    if not rules:
        sys.exit(0)

    bullets = '\n'.join(rules)
    sync_block = f"{SYNC_START}\n{bullets}\n{SYNC_END}"

    with open(CLAUDE_MD) as f:
        claude = f.read()

    if SYNC_START in claude:
        updated = re.sub(
            re.escape(SYNC_START) + r'.*?' + re.escape(SYNC_END),
            sync_block,
            claude,
            flags=re.DOTALL
        )
    else:
        updated = claude.rstrip() + f"\n\n## Conventions (Auto-Sync)\n{sync_block}\n"

    with open(CLAUDE_MD, 'w') as f:
        f.write(updated)


if __name__ == '__main__':
    main()
