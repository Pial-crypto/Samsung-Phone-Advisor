from database.db import get_phone_by_name

from database.db import get_phone_by_name, get_all_model_names


def extract_models_from_query(question: str):
    """
    Dynamically detect models from DB instead of hardcoding keywords.
    """
    models_found = []
    question_lower = question.lower()

    # all_models = get_all_model_names()
    all_models = [
    # S Series
    "S24 Ultra",
    "S24+",
    "S24",
    "S23 Ultra",
    "S23",
    "S22 Ultra",
    "S23 FE",
    "S21 FE",

    # A Series
    "A55",
    "A54",
    "A35",
    "A34",
    "A15",
    "A05s",

    # Z Series
    "Z Fold5",
    "Z Flip5",
    "Z Fold4",
    "Z Flip4",

    # M Series
    "M54",
    "M34",
    "M14",

    # F Series
    "F54",
    "F34",

    # Others
    "XCover6 Pro"
]

    for model in all_models:
        if model.lower() in question_lower:
            models_found.append(model)

    return models_found


def get_phone_data_for_models(models):
    phones = []
    for model in models:
        phone = get_phone_by_name(model)
        if phone:
            phones.append(phone)
    return phones

def get_phone_data_for_models(models):
    phones = []
    for model in models:
        phone = get_phone_by_name(model)

        if phone:
            phones.append(phone)
    return phones