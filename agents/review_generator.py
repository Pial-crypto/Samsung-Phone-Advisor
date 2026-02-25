def extract_number(text):
    """
    Extract first integer found in string.
    Example: '5000 mAh' → 5000
    """
    import re
    match = re.search(r'\d+', str(text))
    return int(match.group()) if match else 0


def generate_comparison(phone_data, question):
    if len(phone_data) < 2:
        return "Not enough phones to compare."

    phone1 = phone_data[0]
    phone2 = phone_data[1]

    name1, _, _, battery1, camera1, _, _, price1 = phone1
    name2, _, _, battery2, camera2, _, _, price2 = phone2

    battery_val1 = extract_number(battery1)
    battery_val2 = extract_number(battery2)

    camera_val1 = extract_number(camera1)
    camera_val2 = extract_number(camera2)

    comparison = f"Comparison between {name1} and {name2}:\n\n"

    # Camera comparison
    if camera_val1 > camera_val2:
        comparison += f"{name1} has a higher resolution camera.\n"
        better_camera = name1
    elif camera_val2 > camera_val1:
        comparison += f"{name2} has a higher resolution camera.\n"
        better_camera = name2
    else:
        comparison += "Both phones have similar camera resolution.\n"
        better_camera = None

    # Battery comparison
    if battery_val1 > battery_val2:
        comparison += f"{name1} offers better battery capacity.\n"
        better_battery = name1
    elif battery_val2 > battery_val1:
        comparison += f"{name2} offers better battery capacity.\n"
        better_battery = name2
    else:
        comparison += "Both phones have similar battery capacity.\n"
        better_battery = None

    # Recommendation logic
    if better_camera:
        comparison += f"\nFor photography, {better_camera} is recommended."
    elif better_battery:
        comparison += f"\nFor longer usage, {better_battery} is recommended."
    else:
        comparison += "\nBoth phones are quite similar in overall performance."

    return comparison