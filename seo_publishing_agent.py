import logging
from firebase_admin import firestore

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def publish_to_firebase(db, collection_name, title, article):
    """
    Publish a formatted article to Firebase.
    """
    try:
        # Format article with visual placeholders
        formatted_article = format_article(article)

        # Define document data
        doc_data = {
            "title": title,
            "content": formatted_article,
            "timestamp": firestore.SERVER_TIMESTAMP
        }

        # Add the document to the specified collection
        db.collection(collection_name).add(doc_data)
        logging.info("Article published to Firebase successfully.")
    except Exception as e:
        logging.error(f"Error publishing to Firebase: {e}")

def format_article(article):
    """
    Enhance readability of the article with visual placeholders and structure.
    """
    formatted_content = []
    paragraphs = article.split("\n")
    for para in paragraphs:
        if len(para) > 100:
            # Break long paragraphs into shorter ones for readability
            sub_paragraphs = [para[i:i+100] for i in range(0, len(para), 100)]
            formatted_content.extend(sub_paragraphs)
        else:
            formatted_content.append(para)

    # Add visual placeholders (e.g., headings, bullet points)
    formatted_article = "\n\n".join(
        [f"### {line}" if idx == 0 else line for idx, line in enumerate(formatted_content)]
    )
    return formatted_article