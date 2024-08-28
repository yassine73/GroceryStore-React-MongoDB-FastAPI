# Import From Files
from database.config import db
from database.models import Order
from database.schemas import show_order
from api_routes.aggregationSearch import order_search_agg

# Import From Modules
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from datetime import datetime as dt


router = APIRouter()


# Get List of Orders / show
@router.get("/order", tags=["Orders"])
async def get_orders(filterBy: str = None, searchText: str = None, skip: int = 0, limit: int = 10):
    if filterBy and searchText:
        data = db.order.aggregate(order_search_agg(filter, searchText, skip, limit))
        orders = [show_order(order) for order in data[0]["orders"]]
        count_orders = data[0]["count"][0]["total_orders"] if data[0]["count"] else 0
        return {
            "orders" : orders,
            "count" : count_orders
        }
    orders = [show_order(order) for order in db.order.find().skip(skip).limit(limit)]
    count_orders = db.order.count_documents({})
    return {
        "orders" : orders,
        "count" : count_orders
    }
    


# Get order by ID
@router.get("/order/{_id}", tags=["Orders"])
async def get_order_by_id(_id: str):
    try:
        order_id = ObjectId(_id)
        order = db.order.find_one({"_id" : order_id})
        if not(order):
            return HTTPException(404, "Order Not Found!")
        return {"order" : show_order(order)}
    except Exception as e:
        raise HTTPException(400, f"{e}")



# Post Order / Add 
@router.post("/order", tags=["Orders"])
async def add_order(order: Order):
    try:
        db.order.insert_one(dict(order))
        return { "data" : "Inserted!" }
    except Exception as e:
        HTTPException(400, f"{e}")


# Put Order / Update
@router.put("/order/{_id}", tags=["Orders"])
async def update_order(_id: str, order: Order):
    try:
        order_id = ObjectId(_id)
        search_order = db.order.find_one({"_id": order_id})
        if not(search_order):
            raise HTTPException(404, "Not Found!")
        db.order.update_one({"_id": order_id}, {"$set" : dict(order)})
        return { "data" : "Updated!" }
    except Exception as e:
        raise HTTPException(400, f"{e}")
        

# Delete Order
@router.delete("/order/{_id}", tags=["Orders"])
async def delete_order(_id: str):
    try:
        order_id = ObjectId(_id)
        search_order = db.order.find_one({"_id": order_id})
        if not(search_order):
            raise HTTPException(404, "Not Found!")
        db.order.delete_one({"_id" : order_id})
        return { "data" : "success" }
    except Exception as e:
        raise HTTPException(400, f"{e}")