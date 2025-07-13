import os
import faiss
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import cohere

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY not found in environment variables.")

co = cohere.Client(COHERE_API_KEY)

with open("loan_data_cleaned.txt", "r", encoding="utf-8") as f:
    data = f.read()

print("Embedding text chunks...")
print(f"Total characters loaded: {len(data)}")

chunks = [chunk.strip() for chunk in data.split("\n") if len(chunk.strip()) > 10]
print(f"Number of chunks generated: {len(chunks)}")


if not chunks:
    raise ValueError("No valid text chunks found")


model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


def get_relevant_chunks(query, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    return [chunks[i] for i in indices[0]]


def ask_cohere(question, context):
    try:
        response = co.chat(
            model="command-r",
            message=question,
            temperature=0.5,
            chat_history=[],
            documents=[{"text": context}]
        )
        return response.text.strip()
    except Exception as e:
        return f" Cohere API error: {str(e)}"



print("\n Loan Product Assistant (Cohere) is ready. Type your question or 'exit'.\n")

while True:
    user_input = input(" Your Question: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print(" Goodbye!")
        break

    relevant_chunks = get_relevant_chunks(user_input)
    context = "\n\n".join(relevant_chunks)
    answer = ask_cohere(user_input, context)
    print("\n Answer:", answer, "\n")
