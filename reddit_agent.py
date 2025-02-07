import praw
import logging
import os

def initialize_reddit(client_id, client_secret, user_agent):
    """
    Initialize Reddit API client.
    """
    return praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)


def fetch_reddit_posts(query, limit=10):
    """
    Search for Reddit posts related to a specific topic.
    
    Args:
        query (str): The search query (e.g., "AI trends").
        limit (int): Number of posts to fetch.
        
    Returns:
        list: A list of dictionaries containing post details.
    """
    try:
        # Initialize Reddit API client
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent="topic_reddit_scraper"
        )
        
        # Search for posts related to the query
        posts = reddit.subreddit("all").search(query, limit=limit, sort="hot")
        
        # Extract relevant data from posts
        result = [
            {
                "title": post.title,
                "url": post.url,
                "score": post.score,
                "subreddit": str(post.subreddit),
                "created_utc": post.created_utc,
                "selftext": post.selftext
            }
            for post in posts
        ]
        return result
    except Exception as e:
        logging.error(f"Error fetching Reddit posts for query '{query}': {e}")
        return []