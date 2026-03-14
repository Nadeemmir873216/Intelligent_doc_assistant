from rag.ingest import load_pdf
from rag.chunking import chunk_documents
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from rag.generator import Generator


docs = load_pdf(f"data/{input()}")

chunks = chunk_documents(docs)

embedder = EmbeddingModel()

texts = [c["text"] for c in chunks]

embeddings = embedder.embed(texts)

vector_store = VectorStore(len(embeddings[0]))

vector_store.add(embeddings, chunks)

retriever = Retriever(embedder, vector_store)

generator = Generator()

question = "can you provide me the links provided in the document and tell me about those too?"

retrieved_chunks = retriever.retrieve(question)

answer = generator.generate(question, retrieved_chunks)

print("\nANSWER:\n")
print(answer)