# SMART Code Review Bot

Automates code review for GitHub PRs using static analysis and AI.

## Features

- Static and AI-based code review
- PR comments with actionable feedback
- Extensible to multiple languages
- Optional dashboard

## Setup

1. Clone repo
2. Set up `.env` with GitHub and OpenAI tokens
3. Run `pip install -r backend/requirements.txt`
4. Start Flask server: `python backend/app.py`
5. Add webhook to your GitHub repo pointing to `/webhook`
