from fastapi import FastAPI

app = FastAPI()

@app.get("/") 
def greet():
    return "Welcome to Lammy's App!"

@app.get("/products")
def get_all_products():
    return "all product"