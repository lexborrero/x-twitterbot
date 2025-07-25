# 🤖 X-TwitterBot

**X-TwitterBot** is a Python-based automation tool that tweets the latest AI-related news from the [Wired AI RSS feed](https://www.wired.com/feed/tag/ai/latest/rss). It parses the RSS feed, extracts article details (title, summary, author, and link), shortens the URL, and posts the content directly to Twitter (X).

---

## 📌 Features
- Fetches the latest AI-related article from Wired's RSS feed.
- Automatically extracts article title, summary, author, and link.
- Shortens article URLs using **TinyURL** (via `pyshorteners`).
- Tweets the formatted article using the **Twitter (X) API**.

---

## 🛠️ Technologies Used
- **Python 3.8+**
- [tweepy](https://www.tweepy.org/) – For interacting with the Twitter API.
- [python-dotenv](https://pypi.org/project/python-dotenv/) – To securely load API keys from `.env`.
- [feedparser](https://pypi.org/project/feedparser/) – For parsing RSS feeds.
- [pyshorteners](https://pypi.org/project/pyshorteners/) – For URL shortening.
- **Twitter Developer Account** – Required to obtain API keys.

---

## 📂 Project Structure

- XBOT.py # Main bot script
 ─ article.py # Article class definition (stores article details)
 ─ .env # Stores API credentials (not shared)
 ─ requirements.txt # Project dependencies

## Created a env file in project root
CONSUMER_KEY=your_consumer_key
CONSUMER_SECRET=your_consumer_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret

## Usage 
The bot will:

1. Fetch the latest article from Wired AI's RSS feed.

2. Format the article with title, summary, author, and shortened URL.

3. Post the tweet to your connected Twitter (X) account.

## Example Tweet Format
- Title: [Article Title]
- Summary: [Short Summary]
- Author: [Author Name]

 - https://tinyurl.com/shortened-link

