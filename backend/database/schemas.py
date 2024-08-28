def show_product(product):
    return {
        "_id": str(product["_id"]),
        "name": product["name"],
        "unit": product["unit"],
        "price": product["price"]
    }
    
def show_order(order):
    return {
        "_id" : str(order["_id"]),
        "customer" : order["customer"],
        "product_id" : order["product_id"],
        "qty" : order["qty"],
        "order_date" : order["order_date"]
    }