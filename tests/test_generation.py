from rag.ingest import load_pdf
from rag.chunking import chunk_documents
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from rag.generator import Generator
from rag.citation import format_source


docs = load_pdf("data/report.pdf")

chunks = chunk_documents(docs)

embedder = EmbeddingModel()

texts = [c["text"] for c in chunks]

embeddings = embedder.embed(texts)

vector_store = VectorStore(len(embeddings[0]))

vector_store.add(embeddings, chunks)

retriever = Retriever(embedder, vector_store)

generator = Generator()

question = "What is this about?"

retrieved_chunks = retriever.retrieve(question)

answer = generator.generate(question, retrieved_chunks)
sources = format_source(retrieved_chunks)

print("\nANSWER:\n")
print(answer)
print("\nSOURCES:\n")
for s in sources:
    print(s)
