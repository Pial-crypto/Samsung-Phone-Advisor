import requests
from bs4 import BeautifulSoup

def scrape_phone(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    # print(f"Scraping {url} - Status Code: {response.status_code}")
    # print("*" * 50)
    # print(f"Response Headers: {response.headers}")
    # print("*" * 50)
    # print(f"Response Content: {response.text[:500]}")  # Print the first 500 characters of the response
    # print("*" * 50)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(f"Parsed HTML Title: {soup.title.string if soup.title else 'No title found'}")  # Print the title of the page
    # print("*" * 50)
    # # print("soup ",soup.prettify()[:500])  # Print the first 500 characters of the prettified HTML
    # print("*" * 50)
    # print("h1 tag:", soup.find("h1"))  # Print the h1 tag to check if it's being found correctly
    # print("*" * 50)
    # print("*" * 50)
    model_name = soup.find("h1").text.strip()
    print(f"Model Name: {model_name}")  # Print the model name
    # print(f"Model Name: {model_name}")  # Print the model name
    # print("*" * 50)
    # if not model_name.lower().startswith("samsung"):
    #     return None

    specs = {}

    tables = soup.find_all("table")
    # print(tables)  # Print the tables to check if they are being found correctly
    # print("*" * 50)
    # print(f"Number of tables found: {len(tables)}")  # Print the number of tables found
    # print("*" * 50)
    # print("*" * 50)



    for table in tables:
        # print(f"Processing table with class: {table.get('class')}")  # Print the class of the current table
        # print(f"Table content: {table.prettify()[:500]}")  # Print the first 500 characters of the table content
        # print("*" * 50)
        rows = table.find_all("tr")
        for row in rows:
            key = row.find("td", class_="ttl")
            # print(f"Key found: {key.text.strip() if key else 'No key found'}")  # Print the key found in the current row

            value = row.find("td", class_="nfo")
            # print(f"Value found: {value.text.strip() if value else 'No value found'}")  # Print the value found in the current row
            # print("*" * 50)
            # print("*" * 50)
            # print("*" * 50)
            if key and value:
                specs[key.text.strip()] = value.text.strip()

    return {
    "model_name": model_name,
    "release_date": specs.get("Announced"),
    "display": specs.get("Size"),
    "battery": specs.get("Type"),
    "camera": specs.get("Main Camera"),
    "ram": specs.get("RAM"),
    "storage": specs.get("Internal"),
    "price": specs.get("Price")
}


if __name__ == "__main__":
    url = "https://www.gsmarena.com/samsung_galaxy_s23_ultra-12024.php"
    data = scrape_phone(url)
    print(data)