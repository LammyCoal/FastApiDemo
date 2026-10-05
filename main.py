from fastapi import FastAPI
from models import MyProduct

app = FastAPI()

@app.get("/") 
def greet():
    return "Welcome to Lammy's App!"

Products = [
    MyProduct(1,"laptop", "Personal laptop", 11, 57.80),
    MyProduct(2,"Phone","Iphone 11", 1, 1234.5)
]

@app.get("/products")
def get_all_products():
    return Products
