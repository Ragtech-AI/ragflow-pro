from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.routes import documents
app = FastAPI(title="RAGFlow Pro API", version="1.0.0")
from backend.app.core.database import get_vector_store
from backend.app.api.routes import vector_db
app.include_router(vector_db.router, prefix="/api/vector_db", tags=["vector_db"])



@app.on_event("startup")
def initialize_services():
    get_vector_store()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to RAGFlow Pro API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
app.include_router(documents.router, prefix="/api/documents", tags=["documents"])





