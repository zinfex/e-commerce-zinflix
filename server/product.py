from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    sale: bool
    image: str
    description: str
    category: str


class Vendas(BaseModel):
    id: int
    id_produto: int
    price: float
    quant: int