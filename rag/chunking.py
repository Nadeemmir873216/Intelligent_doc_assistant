def chunk_documents(documents, chunk_size=1000, overlap=200):
    chunks = []
    for doc in documents:
        words = doc["text"].split()

        start = 0
        chunk_id = 0

        while start < len(words):
            end = start + chunk_size
            chunk_words = words[start:end]

            chunk_text = " ".join(chunk_words)

            chunk = {
                "text": chunk_text,
                "page" : doc["page_number"],
                "source" : doc["source"],
                "chunk_id" : chunk_id
            }

            chunks.append(chunk)

            start += chunk_size - overlap
            chunk_id += 1

    return chunks
