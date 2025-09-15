from backend.app.services.vector_store import VectorStore


vector_store = None
def get_vector_store() -> VectorStore:
    global vector_store
    if vector_store is None:
        vector_store = VectorStore()
    return vector_store
