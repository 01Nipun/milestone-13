import json

def search_products(query):
    with open("data/products.json") as f:
        products = json.load(f)

    results = [p["name"] for p in products if query.lower() in p["name"].lower()]

    if results:
        return results
    else:
        return ["No matching products found"]