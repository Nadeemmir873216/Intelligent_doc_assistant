from rag.ingest import load_pdf
from rag.chunking import chunk_documents
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from rag.retriever import Retriever


docs = load_pdf("data/report.pdf")

chunks = chunk_documents(docs)

embedder = EmbeddingModel()

texts = [c["text"] for c in chunks]

embeddings = embedder.embed(texts)

vector_store = VectorStore(len(embeddings[0]))

vector_store.add(embeddings, chunks)

retriever = Retriever(embedder, vector_store)

results = retriever.retrieve("What does machine learnign model does ?")

print("Retrieved chunks:\n")

for r in results:
    print(r["source"], "page", r["page"])
    print(r["text"][:200])
    print("----")