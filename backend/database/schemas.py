def show_product(product):
    return {
        "_id": str(product["_id"]),
        "name": product["name"],
        "unit": product["unit"],
        "price": product["price"]
    }