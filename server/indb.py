import json

def generate_products():
    with open("./data/products.json", "r") as f:
        return json.load(f)

def list_sales():
    with open("./data/sales.json", "r") as f:
        return json.load(f)