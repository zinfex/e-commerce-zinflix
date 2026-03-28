import json

def generate_products():
    with open("./data/products.json", "r") as f:
        return json.load(f)
