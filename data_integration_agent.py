import spacy

# Load NLP model for semantic analysis
nlp = spacy.load("en_core_web_sm")

def analyze_context(text):
    """
    Analyze the semantic context of a text using SpaCy.
    """
    doc = nlp(text)
    return [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

def categorize_data(news_articles, reddit_posts):
    """
    Categorize articles and posts by shared themes or keywords.
    """
    categorized_data = {}

    for article in news_articles:
        article_keywords = analyze_context(article["summary"])
        for post in reddit_posts:
            post_keywords = analyze_context(post["title"])
            shared_keywords = set(article_keywords) & set(post_keywords)

            if shared_keywords:
                key = tuple(sorted(shared_keywords))
                if key not in categorized_data:
                    categorized_data[key] = {"news": [], "reddit": []}

                categorized_data[key]["news"].append({
                    "title": article["title"],
                    "summary": article["summary"],
                    "link": article["link"],
                })
                categorized_data[key]["reddit"].append({
                    "title": post["title"],
                    "url": post["url"],
                    "score": post["score"],
                })

    return categorized_data

def integrate_data(news_articles, reddit_posts):
    """
    Combine news articles and Reddit posts into a unified, context-aware dataset.
    """
    categorized_data = categorize_data(news_articles, reddit_posts)
    integrated_data = []

    for key, data in categorized_data.items():
        integrated_data.append({
            "shared_context": list(key),
            "news": data["news"],
            "reddit": data["reddit"],
        })

    return integrated_data
