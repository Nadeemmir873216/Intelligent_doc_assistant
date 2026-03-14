# this code is to make system identify the root directory

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

#streamlit code starts here

import streamlit as st

from rag.ingest import load_pdf
from rag.chunking import chunk_documents
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from rag.generator import Generator
from rag.citation import format_sources

st.title("Intelligent Document Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

question = st.text_input("Ask a question about the document")

if uploaded_file and question:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    docs = load_pdf("temp.pdf")

    chunks = chunk_documents(docs)

    embedder = EmbeddingModel()

    texts = [c["text"] for c in chunks]

    embeddings = embedder.embed(texts)

    vector_store = VectorStore(len(embeddings[0]))

    vector_store.add(embeddings, chunks)

    retriever = Retriever(embedder, vector_store)

    generator = Generator()

    retrieved_chunks = retriever.retrieve(question)

    answer = generator.generate(question, retrieved_chunks)

    sources = format_sources(retrieved_chunks)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Sources")
    for s in sources:
        st.write(s)