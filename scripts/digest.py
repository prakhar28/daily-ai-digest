"""Append one edition (morning / midday / evening) of the daily AI & tech digest.

Writes digests/YYYY/MM/YYYY-MM-DD.md and refreshes the index in README.md.
Stories already listed earlier today are skipped, so every edition adds something new.
"""
import datetime as dt
import os
import re
from pathlib import Path

from hn import is_ai, md_line, top_stories

ROOT = Path(__file__).resolve().parent.parent
EDITIONS = {"morning": "🌅 Morning", "midday": "☀️ Midday", "evening": "🌙 Evening"}


def edition_for(now: dt.datetime) -> str:
    forced = os.environ.get("EDITION", "").strip().lower()
    if forced in EDITIONS:
        return forced
    h = now.hour  # UTC
    return "morning" if h < 15 else "midday" if h < 20 else "evening"


def main() -> None:
    now = dt.datetime.now(dt.timezone.utc)
    day = now.date().isoformat()
    edition = edition_for(now)

    path = ROOT / "digests" / f"{now:%Y}" / f"{now:%m}" / f"{day}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = path.read_text(encoding="utf-8") if path.exists() else f"# AI & Tech Digest · {day}\n"

    if f"## {EDITIONS[edition]} edition" in existing:
        print(f"{edition} edition already written for {day}; nothing to do")
        return

    seen = set(re.findall(r"item\?id=(\d+)", existing))
    stories = [s for s in top_stories() if str(s["id"]) not in seen]
    ai = sorted([s for s in stories if is_ai(s)], key=lambda s: -s["score"])[:8]
    tech = sorted([s for s in stories if not is_ai(s)], key=lambda s: -s["score"])[:5]
    if not ai and not tech:
        print("no new stories; skipping")
        return

    section = [f"\n## {EDITIONS[edition]} edition · {now:%H:%M} UTC\n"]
    if ai:
        section += ["\n### 🤖 AI & LLMs\n"] + [md_line(s) for s in ai]
    if tech:
        section += ["\n### 💻 Also trending in tech\n"] + [md_line(s) for s in tech]
    path.write_text(existing.rstrip("\n") + "\n" + "\n".join(section) + "\n", encoding="utf-8")

    update_readme(day, ai[:5] or tech[:5])
    print(f"wrote {edition} edition to {path.relative_to(ROOT)}")


def update_readme(day: str, highlights: list[dict]) -> None:
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")

    files = sorted((ROOT / "digests").rglob("*.md"), reverse=True)[:14]
    archive = "\n".join(f"- [{f.stem}]({f.relative_to(ROOT).as_posix()})" for f in files)
    today = "\n".join(md_line(s) for s in highlights)

    block = (
        f"<!--DIGEST:START-->\n### 🔥 Today's highlights ({day})\n\n{today}\n\n"
        f"### 🗂️ Last 14 days\n\n{archive}\n<!--DIGEST:END-->"
    )
    text = re.sub(r"<!--DIGEST:START-->.*?<!--DIGEST:END-->", block, text, flags=re.S)
    readme.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
