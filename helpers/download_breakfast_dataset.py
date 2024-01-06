import requests


files = [
    "products",
    "stores",
    "transactions",
]
for each in files:
    url = f"https://raw.githubusercontent.com/zkan/open-data/main/breakfast-at-the-frat/cleaned/{each}.csv"
    response = requests.get(url)
    with open(f"breakfast_{each}.csv", mode="wb") as f:
        f.write(response.content)
