# from folder
from database.config import db
from database.models import Product
from database.schemas import show_product
from api_routes.product.aggregationSearch import product_search_agg

# from models
from fastapi import APIRouter, HTTPException
from bson import ObjectId


router = APIRouter()


# Get Product and Count List by filter or all
@router.get("/product", tags=["products"])
async def show_product_by_filter(filterBy: str = None , SearchText: str = None, limit: int = 10, skip: int = 0):
    if filterBy and SearchText:
        data = list(db.product.aggregate(product_search_agg(filterBy, SearchText, limit, skip)))
        products = [show_product(product) for product in data[0]["products"]]
        count_products = data[0]["count"][0]["total_products"] if data[0]["count"] else 0
        return {
            "products" : products,
            "count" : count_products
        }
    products = [show_product(product) for product in db.product.find().skip(skip).limit(limit)]
    count_products = [db.product.count_documents({})]
    return {
        "products" : products,
        "count" : count_products
    }

# Get Product List
# @router.get("/product", tags=["products"])
# async def list_products(skip: int = 0, limit: int = 5):
#     products = [show_product(product) for product in db.product.find().skip(skip).limit(limit)]
#     return {"products" : products}


# Get Product by ID
@router.get("/product/{_id}", tags=["products"])
async def show_product_by_id(_id: str):
    id_product = ObjectId(_id)
    product = db.product.find_one({"_id" : id_product})
    if not(product):
        raise HTTPException(status_code=404, detail=f"Product Not Exists")
    return {"product" : show_product(product)}



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