from fastapi import FastAPI, Depends
from fastapi import APIRouter
from backend.app.core.database import get_vector_store


router = APIRouter()

@router.get("/health")
def health_check(vector_store=Depends(get_vector_store)):
    return vector_store.health_check()

@router.get("/info")
def get_collection_info(vector_store=Depends(get_vector_store)):
    count, details = vector_store.get_collection_info()
    return {"vector_count": count, "details": details}

@router.post("/reset")
def reset_collection(vector_store=Depends(get_vector_store)):
    vector_store.reset_collection()
    return {"status": "collection reset"}   

