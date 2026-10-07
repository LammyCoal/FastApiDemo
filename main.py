from fastapi import FastAPI
from models import MyProduct

app = FastAPI()

@app.get("/") 
def greet():
    return "Welcome to Lammy's App!"

Products = [
    MyProduct(1,"laptop", "Personal laptop", 11, 57.80),
    MyProduct(2,"Phone","Iphone 11", 1, 1234.5),
    MyProduct(3,"Headphones","Noise cancelling headphones", 5, 99.99),
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