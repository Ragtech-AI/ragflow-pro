from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.routes import documents
app = FastAPI(title="RAGFlow Pro API", version="1.0.0")

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