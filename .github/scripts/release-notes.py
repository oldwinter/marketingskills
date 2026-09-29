#!/usr/bin/env python3
import argparse
import pathlib
import re


def extract_blocks(text: str) -> dict[str, str]:
    parts = re.split(r"\n### (\d+\.\d+\.\d+) \([^)]*\)\n", text)
    return {
        parts[index]: parts[index + 1].split("\n### ", 1)[0].strip()
        for index in range(1, len(parts), 2)
    }


def release_title(version: str, body: str) -> str:
    first = next((line for line in body.splitlines() if line.strip()), "")
    first = re.sub(r"[*`_]|^- |\[([^\]]+)\]\([^)]+\)", r"\1", first).strip()
    title = f"v{version} — {first}"
    return title if len(title) <= 100 else title[:99].rstrip() + "…"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    parser.add_argument("--versions-file", default="VERSIONS.md")
    parser.add_argument("--notes-file", default="release-notes.md")
    parser.add_argument("--title-file", default="release-title.txt")
    args = parser.parse_args()

    text = pathlib.Path(args.versions_file).read_text(encoding="utf-8")
    blocks = extract_blocks(text)
    if args.version not in blocks:
        parser.error(f"VERSIONS.md has no release notes for {args.version}")

    body = blocks[args.version]
    title = release_title(args.version, body)
    pathlib.Path(args.notes_file).write_text(body + "\n", encoding="utf-8")
    pathlib.Path(args.title_file).write_text(title, encoding="utf-8")
    print("Title:", title)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
