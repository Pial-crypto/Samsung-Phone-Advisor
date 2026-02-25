
from scraper.scraper import scrape_phone
from database.db import insert_phone
# PHONE_URLS = [
#     # S Series
#     "https://www.gsmarena.com/samsung_galaxy_s24_ultra-12771.php",
#     "https://www.gsmarena.com/samsung_galaxy_s24+-12772.php",
#     "https://www.gsmarena.com/samsung_galaxy_s24-12773.php",
#     "https://www.gsmarena.com/samsung_galaxy_s23_ultra-12024.php",
#     "https://www.gsmarena.com/samsung_galaxy_s23-12082.php",
#     "https://www.gsmarena.com/samsung_galaxy_s22_ultra-11251.php",

#     # A Series
#     "https://www.gsmarena.com/samsung_galaxy_a55-12824.php",
#     "https://www.gsmarena.com/samsung_galaxy_a54-12133.php",
#     "https://www.gsmarena.com/samsung_galaxy_a35-12823.php",
#     "https://www.gsmarena.com/samsung_galaxy_a34-12074.php",
#     "https://www.gsmarena.com/samsung_galaxy_a15-12748.php",
#     "https://www.gsmarena.com/samsung_galaxy_a05s-12584.php",

#     # Z Series
#     "https://www.gsmarena.com/samsung_galaxy_z_fold5-12418.php",
#     "https://www.gsmarena.com/samsung_galaxy_z_flip5-12252.php",
#     "https://www.gsmarena.com/samsung_galaxy_z_fold4-11737.php",
#     "https://www.gsmarena.com/samsung_galaxy_z_flip4-11573.php",

#     # FE / Others
#     "https://www.gsmarena.com/samsung_galaxy_s23_fe-12520.php",
#     "https://www.gsmarena.com/samsung_galaxy_s21_fe_5g-10954.php",

#     # M Series
#     "https://www.gsmarena.com/samsung_galaxy_m54-12220.php",
#     "https://www.gsmarena.com/samsung_galaxy_m34-12304.php",
#     "https://www.gsmarena.com/samsung_galaxy_m14-12109.php",

#     # Budget
#     "https://www.gsmarena.com/samsung_galaxy_f54-12383.php",
#     "https://www.gsmarena.com/samsung_galaxy_f34-12441.php",
#     "https://www.gsmarena.com/samsung_galaxy_xcover6_pro-11600.php",
# ]

# for url in PHONE_URLS:
#     data = scrape_phone(url)
#     print("Scraped Data:", data)
#     insert_phone(data)
#     print("Inserted into database ")
    
    


from database.db import get_phone_by_name

phone = get_phone_by_name("S23 Ultra")

# print(phone)

from database.db import get_phone_by_name
from rag.formatter import format_specs

# phone = get_phone_by_name("S23 Ultra")
# answer = format_specs(phone)
# print(phone)
# print(answer)

from core.query_classifier import classify_query

# q1 = "What are the specs of Samsung Galaxy S23 Ultra?"
# q2 = "Compare Galaxy S23 Ultra and S22 Ultra"
# q3 = "Which Samsung phone has the best battery?"

# print(classify_query(q1))
# print(classify_query(q2))
# print(classify_query(q3))

from agents.data_extractor import extract_models_from_query, get_phone_data_for_models

# question = "Compare Galaxy S23 Ultra and S22 Ultra"

# models = extract_models_from_query(question)
# print("Detected models:", models)

# phones = get_phone_data_for_models(models)
# print("Phone data:", phones)

from agents.data_extractor import extract_models_from_query, get_phone_data_for_models
from agents.review_generator import generate_comparison

question = "Compare Galaxy S23 Ultra and S21 Ultra for photography"
# print("Question:", classify_query(question))
query_type = classify_query(question)

    # SPEC QUERY → RAG
if query_type == "specs":
        models = extract_models_from_query( question)
        phone = get_phone_by_name(models[0]) if models else None
        answer = format_specs(phone)

    # COMPARE QUERY → Multi-Agent
elif query_type == "compare":
        models = extract_models_from_query(question)
        phones = get_phone_data_for_models(models)
        answer = generate_comparison(phones, question)

   
elif query_type == "recommend":
        models = extract_models_from_query(question)
        phones = get_phone_data_for_models(models)
        answer = generate_comparison(phones, question)

else:
    answer = "Sorry, I could not understand the question."

print("Answer:", answer)

   


