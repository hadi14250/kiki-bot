# Kiki

Kiki is a Python bot that scrapes public profile and post data from X (formerly Twitter), TikTok, and Instagram while bypassing common bot-detection systems. The collected data feeds into SCOM (Secure Commerce for Online Marketing), where it powers influencer rate suggestions and post-verification.

## What Kiki Collects

- Username and display name
- Follower and following counts
- Post / tweet count
- Per-post likes and engagement
- Post date
- Post and tweet text content

## Role Within SCOM

SCOM connects companies and startups with influencers. Kiki sits behind the scenes and does two main jobs:

1. **Profile analysis.** When a user signs up on SCOM, Kiki pulls their public activity across the supported platforms and produces a suggested rate that appears on their SCOM profile. This helps brands shortlist influencers and gives both sides a reasonable starting point for negotiation.
2. **Post verification.** Once a deal is made and an influencer publishes the agreed-upon content, Kiki checks the live post against the brief to confirm the post matches what was contracted.

## How It Runs

Kiki is a long-running scheduler. `main.py` boots two worker threads — one for social-media profile scrapes and one for post scrapes — and a daily job that emails moderators a spreadsheet of accounts that failed validation.

- `scheduledFunctions.py` — orchestrates the recurring scrape jobs
- `getSocialMediaQueue.py` / `getPostQueue.py` — pull work off the SCOM API
- `extractInsta*.py`, `extractTiktok*.py`, `extractTwitter*.py`, `extractTweet.py` — per-platform extractors
- `threadingRequests.py` — concurrent request layer with proxy rotation
- `calculateTotalReward.py` — computes the suggested rate from collected metrics
- `sendEmail.py` + `addInvalidUsersToExcelSheet.py` — daily moderator report

Configuration is environment-driven (proxy URL, time zone, daily report hour, user limits, batch size, thread multiplier, emailing list, DB credentials).

## Local Development

A development stack is provided via Docker Compose (Postgres + the SCOM API + Redis):

```bash
docker compose -f docker-compose-dev.yml up
```

Then start the bot:

```bash
./start.sh
```

Required environment variables are read from a local `.env` file.

## Future Enhancements

- **AI-powered rate suggestions** — replace the current heuristic with a model trained on historical deal data for sharper pricing.
- **Post-activity analysis** — study engagement *after* a sponsored post lands and feed that signal back into the rating mechanism.
- **Intelligent matching** — recommend influencers to companies (and vice versa) based on audience fit, not just headline metrics.
