"""Tiny Hacker News client (stdlib only) shared by the daily jobs."""
import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

API = "https://hacker-news.firebaseio.com/v0"

AI_PATTERN = re.compile(
    r"\b(ai|a\.i\.|llms?|gpt[- ]?\d*|openai|anthropic|claude|gemini|llama|mistral|deepseek|qwen|"
    r"agents?|agentic|rag|transformers?|diffusion|neural|machine learning|ml|deep learning|"
    r"inference|fine[- ]?tun\w*|embeddings?|prompt\w*|copilot|chatbot|reasoning model|mcp|"
    r"vector db|evals?|benchmark\w*|hugging ?face|pytorch|tensorflow|nvidia|gpu)\b",
    re.IGNORECASE,
)


def _get(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "daily-ai-digest/1.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)


def top_stories(limit: int = 150) -> list[dict]:
    """Return the current top stories with title, url, score, comments."""
    ids = _get(f"{API}/topstories.json")[:limit]
    with ThreadPoolExecutor(max_workers=16) as pool:
        items = list(pool.map(lambda i: _safe_item(i), ids))
    stories = []
    for it in items:
        if not it or it.get("type") != "story" or it.get("dead") or it.get("deleted"):
            continue
        sid = it["id"]
        stories.append(
            {
                "id": sid,
                "title": it.get("title", "").strip(),
                "url": it.get("url") or f"https://news.ycombinator.com/item?id={sid}",
                "hn": f"https://news.ycombinator.com/item?id={sid}",
                "score": it.get("score", 0),
                "comments": it.get("descendants", 0),
            }
        )
    return stories


def _safe_item(item_id: int):
    try:
        return _get(f"{API}/item/{item_id}.json")
    except Exception:
        return None


def is_ai(story: dict) -> bool:
    return bool(AI_PATTERN.search(story["title"]))


def md_line(s: dict) -> str:
    title = s["title"].replace("|", "\\|").replace("[", "(").replace("]", ")")
    return f"- [{title}]({s['url']}) · ▲ {s['score']} · [{s['comments']} comments]({s['hn']})"
