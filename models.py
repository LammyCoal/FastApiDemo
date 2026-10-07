from pydantic import BaseModel

class MyProduct(BaseModel):
    id: int
    name: str
    description: str
    quantity : int
    price : float
