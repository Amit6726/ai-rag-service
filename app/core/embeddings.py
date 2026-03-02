import numpy as np


class EmbeddingService:
    def embed(self, text: str) -> list[float]:
        # deterministic vector based on text hash
        np.random.seed(abs(hash(text)) % (10**6))
        return np.random.rand(384).tolist()