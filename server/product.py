from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    sale: bool
    image: str
    description: str
    category: str