---

title: RAG Document Assistant
emoji: 📄
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: "1.32.0"
python_version: "3.10"
app_file: app.py
pinned: false
-------------

# 📄 Intelligent Document Assistant (RAG)

An AI-powered **Retrieval-Augmented Generation (RAG)** system that allows users to upload PDFs and ask questions about them.
The system retrieves relevant sections of the documents using **semantic search** and generates answers with an **LLM**, including **citations from the source documents**.

---

## 🚀 Features

* Upload **multiple PDFs**
* Ask natural language questions about documents
* **Semantic search** using vector embeddings
* **FAISS vector database** for fast retrieval
* **LLM-powered answers** using Groq
* **Source citations** showing document and page
* Automatic **temporary file cleanup**
* Efficient **embedding caching for fast queries**

---

## 🧠 System Architecture

The system follows a typical **RAG pipeline**:

```
User Question
      ↓
Embedding Generation
      ↓
Vector Similarity Search (FAISS)
      ↓
Retrieve Relevant Document Chunks
      ↓
LLM (Groq)
      ↓
Answer + Source Citations
```

Document processing pipeline:

```
PDF Upload
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embedding Generation
    ↓
Vector Database (FAISS)
```

---

## 🛠 Tech Stack

| Component       | Technology            |
| --------------- | --------------------- |
| Language        | Python                |
| UI              | Streamlit             |
| Embeddings      | Sentence Transformers |
| Vector Database | FAISS                 |
| LLM Inference   | Groq                  |
| PDF Processing  | PyPDF                 |
| Deployment      | HuggingFace Spaces    |

---

## 📂 Project Structure

```
RAG_doc_assistant
│
├── app.py
├── requirements.txt
│
├── rag/
│   ├── ingest.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── generator.py
│   └── citation.py
│
├── tests/
└── README.md
```

---

## ⚙️ How It Works

1. User uploads one or more PDF documents.
2. The system extracts text from the PDFs.
3. Documents are split into smaller **chunks**.
4. Each chunk is converted into **vector embeddings**.
5. Embeddings are stored in a **FAISS vector database**.
6. When a user asks a question:

   * The question is converted into an embedding.
   * The system retrieves the most relevant chunks.
   * The LLM generates an answer based on the retrieved context.
7. The system displays **sources and page numbers** for transparency.

---

## ▶️ Running Locally

Clone the repository:

```
git clone https://github.com/Nadeemmir873216/RAG_doc_assistant.git
cd RAG_doc_assistant
```

Create virtual environment:

```
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the app:

```
streamlit run app.py
```

---

## 🔑 Environment Variables

Create a `.env` file and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

---

## 🌍 Live Demo

Deployed on HuggingFace Spaces:

https://huggingface.co/spaces/nadeemeer/RAG_doc_assistant

---

## 📌 Future Improvements

* Hybrid search (BM25 + vector search)
* Context reranking
* Support for more document formats
* Persistent vector database
* Better UI and document previews

---

## 👨‍💻 Author

**Nadeem Mir**

Data Science student interested in **AI, ML, and Applied AI Engineering**.

GitHub:
https://github.com/Nadeemmir873216
