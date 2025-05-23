import os
import chromadb
from chromadb.api.types import EmbeddingFunction
from langchain_ollama import OllamaEmbeddings

# ✅ Define a wrapper to conform to ChromaDB's required interface
class ChromaOllamaEmbeddingFunction(EmbeddingFunction):
    def __init__(self, model: str, base_url: str):
        self.embedder = OllamaEmbeddings(model=model, base_url=base_url)

    def __call__(self, input: list[str]) -> list[list[float]]:
        return self.embedder.embed_documents(input)

# ✅ Create the embedding function wrapper
embedding_function = ChromaOllamaEmbeddingFunction(
    model="llama3.2",  # Update this if needed
    base_url="http://localhost:11434"
)

# ✅ Initialize ChromaDB persistent client
chroma_client = chromadb.PersistentClient(path=os.path.join(os.getcwd(), "chroma_db"))

# ✅ Create or load collection with proper embedding function
collection = chroma_client.get_or_create_collection(
    name="rag_collection",
    embedding_function=embedding_function
)
