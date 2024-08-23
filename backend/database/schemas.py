def show_product(product):
    return {
        "_id": str(product["_id"]),
        "Name": product["name"],
        "Unit": product["unit"],
        "Price": product["price"]
    }