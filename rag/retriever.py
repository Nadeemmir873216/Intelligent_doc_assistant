class Retriever:
    def __init__(self, embedder, vector_store):
        self.embedder = embedder
        self.vector_store = vector_store
    
    def retrieve(self, question, k=5):
        query_embedding = self.embedder.embed([question])[0]
        results = self.vector_store.search(query_embedding,k)
        return results