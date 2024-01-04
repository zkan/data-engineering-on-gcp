import csv
import json


with open("products.json") as f:
    products = json.load(f)

print("### Products ###")
print(products[0])

with open("products.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    header = ["sku", "name", "description"]
    writer.writerow(header)
    for each in products:
        writer.writerow([each["sku"], each["name"], each["description"]])

with open("categories.json") as f:
    categories = json.load(f)

print("### Categories ###")
print(categories[0])

with open("categories.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    header = ["id", "name"]
    writer.writerow(header)
    for each in categories:
        writer.writerow([each["id"], each["name"]])

with open("stores.json") as f:
    stores = json.load(f)

print("### Stores ###")
print(stores[0])

with open("stores.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    header = ["id", "type", "name", "address", "address2", "city", "state", "zip"]
    writer.writerow(header)
    for each in stores:
        writer.writerow([each["id"], each["type"], each["name"], each["address"], each["address2"], each["city"], each["state"], each["zip"]])
