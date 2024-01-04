import requests


files = [
    "products",
    "categories",
    "stores",
]
for each in files:
    url = f"https://raw.githubusercontent.com/zkan/open-data/main/best-buy-apis/{each}.json"
    response = requests.get(url)
    with open(f"{each}.json", mode="wb") as f:
        f.write(response.content)
