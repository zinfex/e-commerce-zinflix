import json

from fastapi import FastAPI
from indb import generate_products, list_sales

app = FastAPI()

@app.get("/vendas")
async def get_vendas():
    return list_sales()

@app.get("/vendas/{venda_id}")
async def get_venda(venda_id: int):
    vendas = list_sales()
    for venda in vendas:
        if venda["id"] == venda_id:
            return venda
    return {"error": "Venda não encontrada"}

@app.get("/produtos")
async def get_produtos():
    return generate_products()

@app.post("/produtos")
async def create_produto(produto: dict):
    produtos = generate_products()
    produtos.append(produto)
    with open("./data/products.json", "w") as f:
        json.dump(produtos, f)
    return {"message": "Produto criado com sucesso!"}