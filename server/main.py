import json

from fastapi import FastAPI, Depends
from indb import generate_products

#Auth
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

# oath2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# @app.post("/token")
# async def generate_token(request_form: OAuth2PasswordRequestForm = Depends()):
#     token = await token_generator(request_form.username, request_form.password)
#     return {"access_token": token, "token_type": "bearer"}

# async def get_current_user(token: str = Depends(oath2_scheme)):
#     return {"token" : "user_token"}

@app.get("/produtos")
async def get_produtos():
    return generate_products()

@app.get("/produtos/{produto_id}")
async def get_produto(produto_id: int):
    produtos = generate_products()
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    return {"error": "Produto não encontrado"}

@app.post("/produtos")
async def create_produto(produto: dict):
    produtos = generate_products()
    produtos.append(produto)
    with open("./data/products.json", "w") as f:
        json.dump(produtos, f)
    return {"message": "Produto criado com sucesso!"}

@app.put("/produtos/{produto_id}")
async def update_produto(produto_id: int, updated_produto: dict):
    produtos = generate_products()
    for i, produto in enumerate(produtos):
        if produto["id"] == produto_id:
            produtos[i] = {**produto, **updated_produto}
            with open("./data/products.json", "w") as f:
                json.dump(produtos, f)
            return {"message": "Produto atualizado com sucesso!"}
    return {"error": "Produto não encontrado"}

@app.delete("/produtos/{produto_id}")
async def delete_produto(produto_id: int):
    produtos = generate_products()
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    return {"error": "Produto não encontrado"}
