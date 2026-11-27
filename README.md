# 🗞️ Daily AI & Tech Digest

A small automated pipeline that curates the most-discussed **AI / LLM** and tech stories from Hacker News up to three times a day.

- ⏰ A GitHub Actions cron job runs a **morning** edition every day, plus **midday** and **evening** editions on some days
- 🧠 A keyword classifier splits stories into *AI & LLMs* and *Also trending in tech*
- ♻️ Each edition skips anything already listed earlier that day, so every run adds something new
- 📁 Each day is saved as a Markdown file under [`digests/`](digests)

Built with plain Python (stdlib only) and GitHub Actions. It's the data-collection side of **Byte**, a "useful scrolling" app I'm building that serves bite-sized AI news cards instead of a social feed.

<!--DIGEST:START-->
_The first digest will appear here after the next scheduled run._
<!--DIGEST:END-->

---

**Run it locally:** `python scripts/digest.py` (use `EDITION=evening` to force an edition)
