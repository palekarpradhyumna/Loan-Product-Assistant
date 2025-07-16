
# 🏦 Loan Product Assistant (RAG with Cohere API)

A smart AI assistant that answers natural-language questions about **Bank of Maharashtra loan products** using a **Retrieval-Augmented Generation (RAG)** pipeline built with Python, FAISS, Sentence Transformers, and Cohere’s `command-r` model.

---

## 📌 Project Highlights

- ✅ Web-scrapes loan-related pages from Bank of Maharashtra
- ✅ Cleans and chunkifies the data
- ✅ Uses **FAISS** to retrieve relevant chunks for a user’s question
- ✅ Sends context + question to **Cohere API (`command-r`)** for response
- ✅ Works entirely in your terminal

---

## 🧠 Tech Stack & Libraries

| Component               | Library / Tool                        |
|------------------------|----------------------------------------|
| Embedding model        | `sentence-transformers/all-MiniLM-L6-v2` |
| Vector Search          | `faiss-cpu`                            |
| LLM (Answer Generator) | `cohere` (Cohere API with `command-r`) |
| Scraping               | `requests`, `beautifulsoup4`           |
| Environment config     | `python-dotenv`                        |
| Language               | Python 3.8+                            |

---

## 🗂️ Project Structure

```
loan-product-assistant/
│
├── scrape_loans.py              # Scrapes loan content from BOM website
├── clean_data.py                # Cleans raw scraped content
├── build_rag.py                 # Main RAG assistant (FAISS + Cohere)
├── loan_data_raw.txt            # Scraped loan content
├── loan_data_cleaned.txt        # Cleaned, chunk-ready content
├── .env                         # Your Cohere API key (not committed)
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 🚀 How to Run the Project

### ✅ 1. Clone this repository

```bash[
(https://github.com/palekarpradhyumna/Loan-Product-Assistant)
cd loan-product-assistant
```

### ✅ 2. Set up a virtual environment

```bash
python -m venv env
.\env\Scripts\activate           # On Windows
```
### ✅ 3. Install all dependencies

```bash
pip install -r requirements.txt
```

### ✅ 4. Add your Cohere API key
```
$env:COHERE_API_KEY = "cLjGuamzwJ7nU7BOPFzSco1l08VgEQgmef52eFWJ"

```

You can get your key from https://dashboard.cohere.com/

---

## ▶️ To Run the Assistant

```bash
python build_rag.py
```

Ask any question about BOM loans, e.g.:

```
 Your Question: What are the interest rates for a home loan?

 Answer: The interest rate for a home loan starts from 9.15% per annum...
```

Type `exit` to quit.

---

## 🔍 How It Works

1. **Scraping:** Extracts content from Bank of Maharashtra loan pages
2. **Cleaning:** Removes noise and formats paragraphs
3. **Chunking:** Splits content into ~paragraph-sized chunks
4. **Embedding:** Uses SentenceTransformers to embed each chunk
5. **Indexing:** Adds all embeddings to a FAISS vector index
6. **Retrieval:** Gets top-k chunks most relevant to your query
7. **Generation:** Passes context + question to Cohere `command-r` via `co.chat()`
8. **Answering:** Displays the generated response

---


## 🧠 Sample Libraries Used

```txt
cohere
faiss-cpu
sentence-transformers
requests
beautifulsoup4
python-dotenv
```

---

## 📦 requirements.txt (Sample)

```txt
cohere==4.32
faiss-cpu
sentence-transformers
requests
beautifulsoup4
python-dotenv
```



## 🙋‍♂️ Author

**Pradhyumna Palekar**  
📧 palekarpradhyumna@gmail.com  
