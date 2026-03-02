from app.core.embeddings import EmbeddingService
from app.services.vector_store import VectorStore

class Retriever:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def add_document(self, text: str):
        vector = self.embedding_service.embed(text)
        self.vector_store.add(text, vector)

    def query(self, text: str):
        query_vector = self.embedding_service.embed(text)
        return self.vector_store.search(query_vector)