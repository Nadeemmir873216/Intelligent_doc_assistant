from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "RAG systems combine retrieval and generation"

embedding = model.encode(text)

print("Embedding length:", len(embedding))