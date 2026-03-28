from pydantic import BaseModel
import json

class JsonDB(BaseModel):
    path: str

    def read(self):
        f = open(self.path, "r")
        data = json.loads(f.read())
        f.close() 
        return data
    
    def insert(self, data):
        data = self.read()
        data['products'].append(product.dict())
        f = open(self.path, "w")
        f.write(json.dumps(data))
        f.close()

    def delete(self, product_id):
        data = self.read()
        for product in data['products']:
            if product['id'] == product_id:
                data['products'].remove(product)
                f = open(self.path, "w")
                f.write(json.dumps(data))
                f.close()
                return {"message": "Produto deletado com sucesso!"}
        return {"error": "Produto não encontrado"}
    
