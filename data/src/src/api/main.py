from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from faq_loader import FAQRetriever  # noqa: E402
from llm_client import answer_with_context  # noqa: E402

app = FastAPI(title="AI Receptionist")

FAQ_PATH = os.getenv("FAQ_PATH", "data/faqs.csv")
retriever = FAQRetriever(FAQ_PATH)


class AskRequest(BaseModel):
    query: str


class FAQItem(BaseModel):
    question: str
    answer: str
    score: float


class AskResponse(BaseModel):
    answer: str
    retrieved_faqs: List[FAQItem]


@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    faqs = retriever.retrieve(req.query, top_k=3)
    answer = answer_with_context(req.query, faqs)
    return AskResponse(
        answer=answer,
        retrieved_faqs=[FAQItem(**f) for f in faqs],
    )
