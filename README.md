# AI-Powered News Summarizer

An AI-powered news article summarizer using OpenAI's GPT-3.5-turbo model. The application can be run both on the terminal and as a Streamlit web app.

![Screenshot of the App](screenshot.jpeg)

## Live Demo
Check out the live demo of the application [here](https://ai-powered-news-summarizer.streamlit.app).

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/djpapzin/AI-Powered-News-Summarizer.git
   cd AI-Powered-News-Summarizer
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup API Key**
   
   - Obtain an API key from [OpenAI](https://beta.openai.com/signup/).
   
   - If you're using the terminal, rename `.env copy` to `.env` and paste your API key in the file.
   
   - If you're using Streamlit, rename `secrets.toml copy` in the `.streamlit` directory to `secrets.toml` and paste your API key in the file.

4. **Run the Application**

   - **Terminal**:
     ```bash
     python news_summarizer.py
     ```

   - **Streamlit**:
     ```bash
     streamlit run news_summarizer.py
     ```

## Usage

- **Terminal**: The application will prompt you to enter the URL of a news article. After entering the URL, it will provide a summarized version of the article.

- **Streamlit**: Enter the URL of the news article in the input box and click on the "Summarize" button. The summarized version of the article will be displayed below.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.