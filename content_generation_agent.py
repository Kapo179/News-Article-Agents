import openai
import logging

def generate_article(news_articles, reddit_posts, context):
    """
    Generate an SEO-optimized article in a bold, controversial tone based on gathered data.
    
    Args:
        news_articles (list): A list of news articles with title, summary, and link.
        reddit_posts (list): A list of Reddit posts with title, url, and score.
        context (str): Additional context to provide to the language model.
    
    Returns:
        str: The generated article content. 
    """
    try:
        # Prepare data for the prompt
        news_section = "\n".join([f"Title: {article['title']}\nSummary: {article['summary']}\nLink: {article['link']}" for article in news_articles])
        reddit_section = "\n".join([f"Title: {post['title']}\nURL: {post['url']}\nScore: {post['score']}" for post in reddit_posts])

        # Define the prompt
        prompt = (
            f"You are a professional SEO writer tasked with creating a controversial article in a tone similar to Forbes or The Guardian. "
            f"Your article should present hard truths, build on common fears, and provide contrasting opinions based on evidence. "
            f"Your goal is to say what everyone is thinking but may not say aloud. Use the following data:\n\n"
            f"Context:\n{context}\n\n"
            f"News Articles:\n{news_section}\n\n"
            f"Reddit Opinions:\n{reddit_section}\n\n"
            f"Craft a compelling and thought-provoking article that challenges conventional wisdom while remaining factual and engaging."
        )

        # OpenAI API call
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a professional SEO writer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.8,
            frequency_penalty=0.2,
            presence_penalty=0.3
        )

        # Extract generated content
        article = response.choices[0].message["content"].strip()
        logging.info("Successfully generated article.")
        return article

    except Exception as e:
        logging.error(f"Error generating article: {e}")
        return ""
