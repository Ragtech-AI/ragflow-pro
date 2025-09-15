from backend.app.services.vector_store import VectorStore
def test_vector_store_initialization():
    store = VectorStore()
    assert store is not None
    assert store.collection is not None
def test_store_and_retrieve():
    store = VectorStore()
    store.reset_collection()  # Start fresh
    doc_id = "test_doc"
    chunks = ["This is chunk one.", "This is chunk two."]
    embeddings = [[0.1]*384, [0.2]*384]  # Dummy embeddings
    metadatas = [{"source": "test1"}, {"source": "test2"}]
    store.store_document_chunks(doc_id, chunks, embeddings, metadatas)
    count, _ = store.get_collection_info()
    assert count == 2
    results = store.search_similar_chunks([[0.1]*384], top_k=1)
    assert len(results["ids"][0]) == 1
