# from folder
from database.config import db
from database.models import Product
from database.schemas import show_product
from api_routes.aggregationSearch import search_agg

# from models
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from bson.son import SON


router = APIRouter()


# Get Product List
@router.get("/product", tags=["products"])
async def list_products():
    products = [show_product(product) for product in db.product.find()]
    return {"products" : products}


# Get Product by ID
@router.get("/product/{_id}", tags=["products"])
async def show_product_by_id(_id: str):
    id_product = ObjectId(_id)
    product = db.product.find_one({"_id" : id_product})
    if not(product):
        raise HTTPException(status_code=404, detail=f"Product Not Exists")
    return {"product" : show_product(product)}


# Get Product by Name
@router.get("/product/", tags=["products"])
async def show_product_by_name(filterBy: str = None , SearchText: str = None):
    
    pipeline = search_agg(filterBy, SearchText)
    products = [show_product(product) for product in db.product.aggregate(pipeline)]
    return {"products" : products}

    

       


# Post Product
@router.post("/product", tags=["products"])
async def add_product(product: Product):
    try:
        db.product.insert_one(dict(product))
        return {"data" : "inserted"}
    except:
        raise HTTPException(status_code=500, detail="unit must be 'kg' or 'each' and price must be greater than or equal 0")
    
    


# Put Product
@router.put("/product/{_id}", tags=["products"])
async def update_product(_id: str, product: Product):
    id_product = ObjectId(_id)
    searched_product = db.product.find_one({"_id": id_product})
    if not(searched_product):
        raise HTTPException(status_code=404, detail=f"Product Not Exists")
    try:
        db.product.update_one({"_id": id_product}, {"$set" : dict(product)})
        return {"data" : "Product Updated!"}
    except Exception as e:
        raise HTTPException(500, f"unit must be 'kg' or 'each' and price must be greater than or equal 0")


# Delete Product
@router.delete("/product/{_id}", tags=["products"])
async def delete_product(_id: str):
    try:
        id_product = ObjectId(_id)
        searched_product = db.product.find_one({"_id": id_product})
        if not(searched_product):
            raise HTTPException(status_code=404, detail=f"Product Not Exists")
        db.product.delete_one({"_id": id_product})
        return {"data" : "Product Deleted!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")