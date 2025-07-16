
🏦 Loan Product Assistant (RAG with Cohere API)

A smart AI assistant that answers natural-language questions about Bank of Maharashtra loan products using a Retrieval-Augmented Generation (RAG) pipeline built with Python, FAISS, Sentence Transformers, and Cohere’s `command-r` model.

───────────────────────────────
📌 Project Highlights

- ✅ Web-scrapes loan-related pages from Bank of Maharashtra
- ✅ Cleans and chunkifies the data
- ✅ Uses FAISS to retrieve relevant chunks for a user’s question
- ✅ Sends context + question to Cohere API (`command-r`) for response
- ✅ Works entirely in your terminal

───────────────────────────────
🧠 Tech Stack & Libraries

Component                | Library / Tool
------------------------|------------------------------
Embedding model         | sentence-transformers/all-MiniLM-L6-v2
Vector Search           | faiss-cpu
LLM (Answer Generator)  | cohere (Cohere API with command-r)
Scraping                | requests, beautifulsoup4
Environment config      | python-dotenv
Language                | Python 3.8+

───────────────────────────────
🗂️ Project Structure

loan-product-assistant/
├── scrape_loans.py            # Scrapes loan content from BOM website
├── clean_data.py              # Cleans raw scraped content
├── build_rag.py               # Main RAG assistant (FAISS + Cohere)
├── loan_data_raw.txt          # Scraped loan content
├── loan_data_cleaned.txt      # Cleaned, chunk-ready content
├── .env                       # Your Cohere API key (not committed)
├── requirements.txt           # Python dependencies
└── README.txt                 # This file

───────────────────────────────
🚀 How to Run the Project

1. Clone the repository:
   https://github.com/palekarpradhyumna/Loan-Product-Assistant.git
   cd loan-product-assistant

2. Create and activate a virtual environment:
   python -m venv env
   .\env\Scripts\activate  

3. Install dependencies:
   pip install -r requirements.txt

4. Add your Cohere API key:
  $env:COHERE_API_KEY = "cLjGuamzwJ7nU7BOPFzSco1l08VgEQgmef52eFWJ"


───────────────────────────────
▶️ To Run the Assistant

python build_rag.py

Then ask a question like:
Your Question: What are the interest rates for a home loan?
Answer: The interest rate for a home loan starts from 9.15% 

Type `exit` to quit.

───────────────────────────────
🔍 How It Works

1. Scrapes content from BOM loan product pages
2. Cleans and formats the scraped text
3. Splits text into clean chunks (~paragraphs)
4. Embeds chunks using Sentence Transformers
5. Indexes with FAISS for fast retrieval
6. Retrieves top-k relevant chunks for any query
7. Sends context and question to Cohere API (`command-r`)
8. Cohere generates a smart, contextual answer

───────────────────────────────
🔐 API Key Management

We use `python-dotenv` to load your API key from a `.env` file securely.  
This file is ignored from version control using `.gitignore`.

───────────────────────────────
🧠 Libraries Used

cohere  
faiss-cpu  
sentence-transformers  
requests  
beautifulsoup4  
python-dotenv

───────────────────────────────
📦 Sample requirements.txt

cohere==4.32  
faiss-cpu  
sentence-transformers  
requests  
beautifulsoup4  
python-dotenv

───────────────────────────────
🙋‍♂️ Author

Pradhyumna Palekar  
Email: palekarpradhyumna@gmail.com  
