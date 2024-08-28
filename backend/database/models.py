from pydantic import BaseModel
from datetime import datetime as dt

class Product(BaseModel):
    name: str
    unit: str
    price: float
    
class Order(BaseModel):
    customer: str
    product_id: str
    qty: int
    order_date: dt = dt.now()