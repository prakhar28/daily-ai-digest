# 🗞️ Daily AI & Tech Digest

A small automated pipeline that curates the most-discussed **AI / LLM** and tech stories from Hacker News up to three times a day.

- ⏰ A GitHub Actions cron job runs a **morning** edition every day, plus **midday** and **evening** editions on some days
- 🧠 A keyword classifier splits stories into *AI & LLMs* and *Also trending in tech*
- ♻️ Each edition skips anything already listed earlier that day, so every run adds something new
- 📁 Each day is saved as a Markdown file under [`digests/`](digests)

Built with plain Python (stdlib only) and GitHub Actions. It's the data-collection side of **Byte**, a "useful scrolling" app I'm building that serves bite-sized AI news cards instead of a social feed.

<!--DIGEST:START-->
### 🔥 Today's highlights (2026-11-28)

- [Nvidia Reinstates Jensen Huang as CEO](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html) · ▲ 2861 · [3832 comments](https://news.ycombinator.com/item?id=50611576)
- [AI made self-hosting fun again](https://janlukas.blog/posts/ai-self-hosting) · ▲ 1134 · [527 comments](https://news.ycombinator.com/item?id=50660180)
- [Claude sabotaging ML research tasks?](https://twitter.com/RealAstropulse/status/2126119408997466389) · ▲ 756 · [328 comments](https://news.ycombinator.com/item?id=50664325)
- [Group chat where your AI talks behind your back](https://construct22.com/) · ▲ 724 · [291 comments](https://news.ycombinator.com/item?id=50663595)
- [The New York Times warns photographers not to update Photoshop over AI features](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features) · ▲ 685 · [547 comments](https://news.ycombinator.com/item?id=50647673)

### 🗂️ Last 14 days

- [2026-11-28](digests/2026/11/2026-11-28.md)
<!--DIGEST:END-->

---

**Run it locally:** `python scripts/digest.py` (use `EDITION=evening` to force an edition)
