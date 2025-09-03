from backend.app.core.config import ALLOWED_EXTENSIONS, ALLOWED_MIME_TYPES, MAX_FILE, UPLOAD_FOLDER
from backend.app.services.document_processor import extract_metadata, extract_text, preprocess_text, chunk_text
from pathlib import Path
import uuid
from datetime import datetime
from fastapi import UploadFile,HTTPException

def validate_file(file: UploadFile):
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    extension = Path(file.filename).suffix
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="File extension not allowed")
def generate_file_id():
    return str(uuid.uuid4())

def save_uploaded_file(file: UploadFile, file_id: str) -> Path:
    UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
    file_path = UPLOAD_FOLDER / f"{file_id}_{file.filename}"
    with open(file_path, "wb") as buffer:
        content = file.file.read()
        if len(content) > MAX_FILE:
            raise HTTPException(status_code=400, detail="File size exceeds the maximum limit")
        buffer.write(content)
        metadata = {
          "file_id": file_id,
          "size": len(content),  # Use the content we already read
          "filename": file.filename,
          "content_type": file.content_type,
          "upload_time": datetime.utcnow().isoformat(),
        }
        try:
            processing_results = document_processing_pipeline(file_path)
            metadata.update({"metadata": processing_results.get("metadata", {})})
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing document: {str(e)}")
        return file_path, metadata
        

def document_processing_pipeline(file_path: Path):
    text = extract_text(str(file_path))
    cleaned_text = preprocess_text(text)
    chunks = chunk_text(cleaned_text)
    metadata = extract_metadata(str(file_path))
    return {
        "text": text,
        "cleaned_text": cleaned_text,
        "chunks": chunks,
        "metadata": metadata
    }

