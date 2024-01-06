import csv
import json

import requests


files = [
    "products",
    "categories",
    "stores",
]
for each in files:
    url = f"https://raw.githubusercontent.com/zkan/open-data/main/best-buy-apis/{each}.json"
    response = requests.get(url)
    with open(f"best_buy_{each}.json", mode="wb") as f:
        f.write(response.content)


with open("best_buy_products.json") as f:
    products = json.load(f)

print("### Products ###")
print(products[0])
print(products[99])
print(products[999])
print("-" * 5)

with open("best_buy_products.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    header = ["sku", "name", "description", "most_general_category"]
    writer.writerow(header)
    for each in products:
        writer.writerow([each["sku"], each["name"], each["description"], each["category"][0]["name"]])

with open("best_buy_categories.json") as f:
    categories = json.load(f)

print("### Categories ###")
print(categories[0])
print(categories[99])
print(categories[999])
print("-" * 5)

with open("best_buy_categories.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    header = ["id", "name"]
    writer.writerow(header)
    for each in categories:
        writer.writerow([each["id"], each["name"]])

with open("best_buy_stores.json") as f:
    stores = json.load(f)

print("### Stores ###")
print(stores[0])
print(stores[99])
print(stores[999])
print("-" * 5)

with open("best_buy_stores.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    header = ["id", "type", "name", "address", "address2", "city", "state", "zip"]
    writer.writerow(header)
    for each in stores:
        writer.writerow([each["id"], each["type"], each["name"], each["address"], each["address2"], each["city"], each["state"], each["zip"]])
