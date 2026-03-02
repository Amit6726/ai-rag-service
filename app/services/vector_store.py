import numpy as np

class VectorStore:
    def __init__(self):
        self.documents = []
        self.vectors = []

    def add(self, text: str, vector: list[float]):
        self.documents.append(text)
        self.vectors.append(np.array(vector))

    def search(self, query_vector: list[float], top_k: int = 1):
        if not self.vectors:
            return []

        query_vec = np.array(query_vector)

        scores = []
        for vec in self.vectors:
            similarity = np.dot(query_vec, vec) / (
                np.linalg.norm(query_vec) * np.linalg.norm(vec)
            )
            scores.append(similarity)

        top_indices = np.argsort(scores)[-top_k:][::-1]
        return [self.documents[i] for i in top_indices]