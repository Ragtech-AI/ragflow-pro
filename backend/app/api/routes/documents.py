from fastapi import APIRouter, File, UploadFile
from backend.app.services.file_storage import validate_file, generate_file_id, save_uploaded_file

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    validate_file(file)
    file_id = generate_file_id()
    file_path, metadata = save_uploaded_file(file, file_id)
    return metadata