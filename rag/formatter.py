def format_specs(phone_tuple):
    if not phone_tuple:
        return "Sorry, phone not found."
    
    print("Raw phone data:", phone_tuple)  # Debugging line to check the raw data

    model, release_date, display, battery, camera, ram, storage, price = phone_tuple

    answer = f"""
{model} was released in {release_date}.
It features a {display}.
It comes with a {battery} battery.
Camera setup: {camera}.
RAM options: {ram}.
Storage options: {storage}.
Price: {price}.
"""

    return answer.strip()