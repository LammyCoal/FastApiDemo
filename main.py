from fastapi import FastAPI
from models import MyProduct

app = FastAPI()

@app.get("/") 
def greet():
    return "Welcome to Lammy's App!"

Products = [
    MyProduct(id=1, name="laptop", description="Personal laptop", quantity=11, price=57.80),
    MyProduct(id=2, name="Phone", description="Iphone 11", quantity=1, price=1234.5),
    MyProduct(id=3, name="Headphones", description="Noise cancelling headphones", quantity=5, price=99.99)
]

@app.get("/products")
def get_all_products():
    return Products

@app.get("/products/{id}")
def get_product_by_id(id: int):
    for product in Products:
        if product.id == id:
            return product

    return "product not found!" 

@app.post("/products")
def add_products(product: MyProduct):
    Products.append(product)
    return product

@app.put("/products")
def update_products(id:int , products:MyProduct):
    for i in range(len(Products)):
        if Products[i].id == id:
            Products[i] = products
            return "Product updated successfully!"
        
    return "Product not found!"

@app.delete("/products")
def delete_product(id:int):
    for i in range(len(Products)):
        if Products[i].id == id:
            del Products[i]
            return "Product deleted successfully!"

    return "Product not found!"
    