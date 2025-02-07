# News-Article-Agents

**Author**: [Kapo179](https://github.com/Kapo179)  
**Repository**: [GitHub - Kapo179/News-Article-Agents](https://github.com/Kapo179/News-Article-Agents)

---

## Overview

**News-Article-Agents** is an AI-driven infrastructure designed to **collect**, **analyze**, and **synthesize** news articles and public opinion data from a variety of sources. By simply **modifying the topics in `main.py`**, you can tailor the system to retrieve and process information on any subject—ranging from global events to niche interests. While this repository can be extended to analyze job markets or any other domain, its primary purpose is to offer a **flexible platform** for gathering the **latest news** and **Reddit-based** public sentiment.

In conjunction with [Exhibit A](https://kapooo.notion.site/The-Computer-Science-Job-Market-Are-Comp-sci-Grads-Cooked-15b3548bee9280a1bc4dc622f245b9fc?pvs=4) and [Exhibit B](https://kapooo.notion.site/The-Unspoken-Truths-of-the-Computer-Science-Job-Market-Are-We-Facing-an-Industry-Crisis-1933548bee928050a6b5f7bad9d38ac3?pvs=4), this project demonstrates how **domain-agnostic** AI agents can be utilized to extract meaningful insights from ever-evolving bodies of information. These exhibits serve as **practical examples** of how the tools might be adapted to a specific topic—though **News-Article-Agents** is by no means limited to job market analysis.

---

## Key Features

1. **Modular Agent Architecture**  
   - **Scraper Agents** gather data from various news APIs or RSS feeds.  
   - **Reddit Opinion Agents** collect public sentiment and discussion topics.  
   - Each component can be easily replaced or extended without impacting the core infrastructure.

2. **Domain-Agnostic Design**  
   - Topics, keywords, and data sources are defined in `main.py`, ensuring adaptability to any subject matter—from **politics** to **sports** to **cutting-edge research**.

3. **NLP and Text Analytics**  
   - Integrated with popular NLP libraries (like spaCy or NLTK) for tokenization, summarization, and entity recognition.  
   - Potential to incorporate **Large Language Models (LLMs)** or advanced summarizers.

4. **Pluggable Data Pipeline**  
   - Data can be stored in **JSON** format, a local or remote **database**, or other output mediums.  
   - Built with scalability in mind: you could add streaming layers, cloud services, or container orchestration with minimal changes.

5. **Reddit-Based Public Opinion Gathering**  
   - Agents can query Reddit for relevant keywords, gathering user sentiments, trending subtopics, and conversation metrics.

---

## Architecture

```plaintext
                         +--------------------------+
                         |  News Source APIs / RSS  |
                         +------------+-------------+
                                      |
     +----------------------------------------------------------+
     |                   Ingestion / Scraper Agents             |
     | (Responsible for fetching news headlines & articles)     |
     +----------------------------+-----------------------------+
                                      |
     +----------------------------------------------------------+
     |                    Reddit Opinion Agent                   |
     | (Collects relevant posts/comments, performs sentiment)    |
     +----------------------------+-----------------------------+
                                      |
     +----------------------------------------------------------+
     |            NLP & Analysis Layer (spaCy, NLTK, etc.)       |
     |     (Topic modeling, summarization, entity extraction)    |
     +----------------------------+-----------------------------+
                                      |
     +----------------------------------------------------------+
     |                    Data Storage / Output                  |
     |   (JSON, databases, or further pipelines / dashboards)    |
     +----------------------------------------------------------+

### **Ingestion / Scraper Agents**
- Retrieve articles from news APIs or RSS feeds.
- Can be configured to run at regular intervals or on-demand.

### **Reddit Opinion Agent**
- Pulls related subreddit posts, enabling analysis of public sentiment and emerging discussion trends.

### **NLP & Analysis Layer**
- Core text analytics: cleaning, tokenizing, summarizing.
- May integrate LLMs for advanced text interpretation.

### **Storage / Output**
- Data is stored in the outlined databases in main.py/ & seo_publishing_agent/.

---

## Getting Started

### **Prerequisites**
- Python 3.8+
- A recommended virtual environment (venv, Conda, Poetry, etc.)
- Basic familiarity with command line and Git

### **Installation**
#### **Clone the Repository**
```bash
git clone https://github.com/Kapo179/News-Article-Agents.git
cd News-Article-Agents
```

#### **Create and Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
# or
.\venv\Scripts\activate    # Windows
```

#### **Install Dependencies**
```bash
pip install -r requirements.txt
```
(Adjust as needed if you use Poetry or another dependency manager.)

#### **Set Up Environment Variables**
Copy the  `.env.example` file and populate it with your own API keys, Reddit credentials, etc.
```bash
# API Keys (replace with your actual keys)
API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=dbname
DB_USER=username
DB_PASSWORD=password

# Other Configuration
DEBUG=False
ENVIRONMENT=development

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Google Search Configuration
GOOGLE_API_KEY=your_google_api_key_here
SEARCH_ENGINE_ID=your_search_engine_id_here

# Reddit API Configuration
REDDIT_CLIENT_ID=your_reddit_client_id_here
REDDIT_CLIENT_SECRET=your_reddit_client_secret_here
REDDIT_USER_AGENT=your_user_agent_here

# Notion Integration (Not Yet Supported)


# Firebase Configuration
FIREBASE_CREDENTIALS=firebase-key.json  # Path to your Firebase credentials JSON file 
```

---

## Usage
### **Modify `main.py`**
- Define the topics, keywords, or subreddits you want to scrape.
- Update parameters such as API endpoints, time intervals, or output paths.

### **Run the Main Script**
```bash
python main.py
```
- This triggers the Scraper Agents and Reddit Opinion Agent.
- The system processes all retrieved content, performing NLP tasks as configured.

### **Check Outputs**
- Articles and Reddit data are either printed to the console, stored as JSON, or saved to a database (depending on your config).
- Review logs in the `logs/` directory (if available) for debugging or performance insights.

---

## Customization
### **Ingestion**
- Add or remove news sources in `news_agent.py/` to target specific media outlets or niche websites.

### **NLP**
- Extend or replace the default tokenizer or summarizer in `nlp_layer/`.

### **Reddit Agent**
- Adjust subreddits or conversation filters in `reddit_agent/`.
- Incorporate advanced sentiment analysis or topic classification.

### **Storage**
- Output to a local JSON file, AWS S3, or any custom solution by modifying the relevant sections in `seo_publishing_agent.py/`, & `main.py/`

---

## Contributing
1. Fork this repository and create a feature branch.
2. Implement your changes—be it a new agent, an NLP feature, or a data visualization module.
3. Submit a Pull Request describing the rationale, usage, and purpose.

### **We welcome ideas for:**
- **Enhanced Summarization** using advanced LLMs.
- **Multi-language Support** for international news sources.
- **Real-time Dashboards** for visual analytics.

---

## Future Roadmap
- **Realtime Web Dashboard**: Build news articles that can publish directly into HTML Webpages
- **Continuous Integration/Deployment**: Automated testing and Docker-based deployments to streamline updates.
- **Extended Public Opinion Gathering**: Expand beyond Reddit to platforms like X.

---

## Exhibits
### **[Exhibit A](https://kapooo.notion.site/The-Computer-Science-Job-Market-Are-Comp-sci-Grads-Cooked-15b3548bee9280a1bc4dc622f245b9fc?pvs=4)** 
### **[Exhibit B](https://kapooo.notion.site/The-Unspoken-Truths-of-the-Computer-Science-Job-Market-Are-We-Facing-an-Industry-Crisis-1933548bee928050a6b5f7bad9d38ac3?pvs=4)**
Although News-Article-Agents is not specifically aimed at job market data, these exhibits illustrate how the system can be pointed for any domain—even crucial economic or occupational trend updates—by merely adjusting the topics and feed sources in `main.py`.

---

## License
This project generally follows the **MIT License**, unless otherwise noted within the source files. Feel free to fork, modify, and redistribute under these terms.

---

## Contact
- **GitHub**: [Kapo179](https://github.com/Kapo179)
- **Issues**: Please open a new issue for support requests or feature suggestions.

