from fastapi import APIRouter
from pydantic import BaseModel
from app.services.retriever import Retriever

router = APIRouter()
retriever = Retriever()


class AddRequest(BaseModel):
    text: str


class QueryRequest(BaseModel):
    text: str


@router.post("/add")
def add_document(request: AddRequest):
    retriever.add_document(request.text)
    return {"message": "Document added successfully"}


@router.post("/query")
def query_document(request: QueryRequest):
    results = retriever.query(request.text)
    return {"results": results}