from fastapi import FastAPI
from pydantic import BaseModel

from core.query_classifier import classify_query
from database.db import get_phone_by_name
from rag.formatter import format_specs
from agents.data_extractor import extract_models_from_query, get_phone_data_for_models
from agents.review_generator import generate_comparison

app = FastAPI()


class Question(BaseModel):
    question: str


@app.post("/ask")
def ask_question(q: Question):

    query_type = classify_query(q.question)

    # SPEC QUERY → RAG
    if query_type == "specs":
        models = extract_models_from_query(q.question)
        phone = get_phone_by_name(models[0]) if models else None
        answer = format_specs(phone)

    # COMPARE QUERY → Multi-Agent
    elif query_type == "compare":
        models = extract_models_from_query(q.question)
        phones = get_phone_data_for_models(models)
        answer = generate_comparison(phones, q.question)

    # RECOMMEND QUERY → Multi-Agent (simple reuse)
    elif query_type == "recommend":
        models = extract_models_from_query(q.question)
        phones = get_phone_data_for_models(models)
        answer = generate_comparison(phones, q.question)

    else:
        answer = "Sorry, I could not understand the question."

    return {"answer": answer}