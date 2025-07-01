import tweepy 
from dotenv import load_dotenv
import os
import feedparser
from pprint import pprint
from article import Article
import pyshorteners


shortener = pyshorteners.Shortener()

def get_client():
    load_dotenv()

    client = tweepy.Client(
        consumer_key =os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
    )

    return client

def create_tweet(client, tweet_text):
    title = article.title
    summary = article.summary
    link = shortener.tinyurl.short(article.link)
    author = article.author

    tweet_text = f"Title: {title}\nSummary: {summary}\nAuthor: {author}\n\n{link}"
    
    client.create_tweet(text=tweet_text)

    

feed = feedparser.parse("https://www.wired.com/feed/tag/ai/latest/rss")
first_article = feed['entries'][0]

article = Article(
    first_article['author'],
    first_article['link'],
    first_article['published'],
    first_article['summary'],
    first_article['title']
)

client = get_client()

create_tweet(client, article)