import sys
from dotenv import load_dotenv
import requests
from newspaper import Article
from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI

def get_summary(article_url):
    # Load environment variables
    load_dotenv()

    # Set headers for requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    # Load the model
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # Create a session
    session = requests.Session()

    # Fetch the article
    try:
        response = session.get(article_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            article = Article(article_url)
            article.download()
            article.parse()

            # Prepare the prompt
            template = """You are an advanced AI assistant that summarizes online articles into bulleted lists.
            Here's the article you need to summarize.
            ==================
            Title: {article_title}
            {article_text}
            ==================
            Now, provide a summarized version of the article in a bulleted list format.
            """
            prompt = template.format(article_title=article.title, article_text=article.text)

            # Generate summary
            messages = [HumanMessage(content=prompt)]
            summary = chat(messages)
            return summary

        else:
            return f"Failed to fetch article at {article_url}"
    except Exception as e:
        return f"Error occurred while fetching article at {article_url}: {e}"

def run_streamlit_app():
    import streamlit as st
    st.title("AI-Powered News Summarizer")
    st.write("*An AI-powered news article summarizer using OpenAI's GPT-3.5-turbo model*")

    # Input for the article URL
    article_url = st.text_input("**Enter the URL of the news article:**", placeholder="https://www.artificialintelligence-news.com/2022/01/25/meta-claims-new-ai-supercomputer-will-set-records/")

    if st.button("Summarize"):
        with st.spinner('Summarizing...'):
            summary = get_summary(article_url)
            st.write("Summary:")
            st.write(summary.content)

def run_terminal_app():
    article_url = input("Enter the URL of the news article: ")
    if article_url:
        summary = get_summary(article_url)
        print("Summary:")
        print(summary.content)

if __name__ == "__main__":
    # Check if the script is being run through Streamlit or not
    if 'streamlit' in sys.modules:
        run_streamlit_app()
    else:
        run_terminal_app()
