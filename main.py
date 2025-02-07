import os
import logging
import spacy
import firebase_admin
from firebase_admin import credentials, firestore
from news_agent import fetch_trending_news
from reddit_agent import fetch_reddit_posts
from data_integration_agent import integrate_data
from content_generation_agent import generate_article

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Initialize Firebase
cred = credentials.Certificate("firebase-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def publish_to_firebase(article, title):
    """
    Publish the article to Firebase Firestore.
    """
    try:
        db.collection("articles").add({
            "title": title,
            "content": article,
            "timestamp": firestore.SERVER_TIMESTAMP
        })
        logging.info("Article published to Firebase successfully.")
    except Exception as e:
        logging.error(f"Error publishing to Firebase: {e}")

def main():
    """
    Main function to orchestrate the agents.
    """
    logging.info("Starting the AI Agent system...")

    # Step 1: Gather data
    topic = "Computer Science Job Market"
    news_articles = fetch_trending_news(topic)
    reddit_posts = fetch_reddit_posts("Compsci Job Market", limit=15)

    # Step 2: Integrate data
    integrated_data = integrate_data(news_articles, reddit_posts)

    # Step 3: Generate content
    context = f"Topic: {topic}"  # Provide a meaningful context for the content generation
    for data in integrated_data:
        article = generate_article(data["news"], data["reddit"], context)

        # Step 4: Publish to Firebase
        if article:
            publish_to_firebase(article, topic)

if __name__ == "__main__":
    main()