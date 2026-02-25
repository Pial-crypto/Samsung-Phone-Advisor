def classify_query(question: str):
    question = question.lower()

    if "compare" in question or "difference" in question:
        return "compare"

    if "best" in question or "recommend" in question:
        return "recommend"

    return "specs"