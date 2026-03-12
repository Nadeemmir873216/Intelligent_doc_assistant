from rag.ingest import load_pdf
from rag.chunking import chunk_documents

docs = load_pdf("data/report.pdf")

chunks = chunk_documents(docs)

print("Total chunks:", len(chunks))

chunk_no = int(input("Which chunk no : "))

print(chunks[chunk_no])