from pygooglenews import GoogleNews
import logging
from datetime import datetime

def fetch_trending_news(topic, timeframe="7d", max_articles=10):
    """
    Fetch trending news articles using PyGoogleNews.
    """
    gnews = GoogleNews()
    try:
        search_results = gnews.search(topic, when=timeframe)
        entries = search_results.get("entries", [])
        articles = []
        for entry in entries:
            pub_date = entry.get("published")
            if pub_date:
                pub_date = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %Z")
                if pub_date >= datetime(2024, 10, 1):
                    articles.append({
                        "title": entry["title"],
                        "summary": entry.get("summary", ""),
                        "link": entry.get("link", ""),
                        "published": pub_date
                    })
            if len(articles) >= max_articles:
                break
        logging.info(f"Fetched {len(articles)} news articles.")
        return articles
    except Exception as e:
        logging.error(f"Error fetching news: {e}")
        return []