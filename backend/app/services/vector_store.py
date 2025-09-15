import chromadb
from chromadb.config import Settings
from backend.app.core.config import VECTOR_DB_DIR, COLLECTION_NAME, DISTANCE_METRIC, EMBEDDING_DIMENSIONS

class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=str(VECTOR_DB_DIR))
        self.collection = self._get_or_create_collection()  
    def store_document_chunks(self, doc_id: str, chunks: list, embeddings: list, metadatas: list):
        if len(chunks) != len(embeddings) or len(chunks) != len(metadatas):
            raise ValueError("Chunks, embeddings, and metadatas must have the same length")
        ids = [f"{doc_id}_{i}" for i in range(len(chunks))]
        self.collection.add(
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

    def _get_or_create_collection(self):
        try:
            collection = self.client.get_collection(name=COLLECTION_NAME)
        except Exception:
            collection = self.client.create_collection(name=COLLECTION_NAME, metadata={"distance_metric": DISTANCE_METRIC, "embedding_dimensions": EMBEDDING_DIMENSIONS})
        return collection



    def search_similar_chunks(self, query_embedding: list, top_k: int = 5):
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k
        )
        return results
    
    def health_check(self):
        try:
            _ = self.client.list_collections()
            return {"status": "healthy"}
        except Exception as e:
            return {"status": "unhealthy", "error": str(e)}
    def reset_collection(self):
        self.client.delete_collection(name=COLLECTION_NAME)
        self.collection = self._get_or_create_collection()
    def get_collection_info(self):
        return self.collection.count(), self.collection.get() 
    def delete_document(self, doc_id: str):
        try:
            ids_to_delete = [id for id in self.collection.get()["ids"] if id.startswith(f"{doc_id}_")]
            if ids_to_delete:
                self.collection.delete(ids=ids_to_delete)
                return {"status": "deleted", "deleted_count": len(ids_to_delete)}
            else:
                return {"status": "not_found", "deleted_count": 0}
        except Exception as e:
            return {"status": "error", "error": str(e)}
    