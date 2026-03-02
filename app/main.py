from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI RAG Production")

app.include_router(router)