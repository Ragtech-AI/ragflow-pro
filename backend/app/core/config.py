from pathlib import Path

MAX_FILE = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXTENSIONS = {".pdf", ".txt", ".docx"}
UPLOAD_FOLDER = Path("uploads")
ALLOWED_MIME_TYPES = {
    "application/pdf",
    "text/plain",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document", 
}

# vector db config
VECTOR_DB_DIR = Path("./chroma_data")
COLLECTION_NAME = "ragflow_documents"
DISTANCE_METRIC = "cosine"
EMBEDDING_DIMENSIONS = 384
