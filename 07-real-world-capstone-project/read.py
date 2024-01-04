import json


with open("products.json") as f:
    products = json.load(f)

print("### Products ###")
print(products[0])

with open("categories.json") as f:
    categories = json.load(f)

print("### Categories ###")
print(categories[0])

with open("stores.json") as f:
    stores = json.load(f)

print("### Stores ###")
print(stores[0])