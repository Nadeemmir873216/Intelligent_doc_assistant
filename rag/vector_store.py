import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimensions):
        self.index = faiss.IndexFlatL2(dimensions)
        self.metadata = []
    
    def add(self, embeddings, chunks):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.metadata.extend(chunks)
    
    def search(self,query_vector , k=5):
        query_vector = np.array([query_vector]).astype("float32")
        distance, indices = self.index.search(query_vector,k)
        results = []
        for i in indices[0]:
            if i < len(self.metadata):
                results.append(self.metadata[i])
        
        return results