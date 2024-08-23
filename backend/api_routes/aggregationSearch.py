from bson.objectid import ObjectId

def search_agg(filterBy , searchInput):
    
    if filterBy == "name":
        return [
                {
                    "$match" : {
                        "name": {
                            "$regex": f"^{searchInput}", # find in name field, a name start with {name}
                            "$options": "i" # this is to ignore cases (lower or upper)
                        }
                    }
                }
            ]
        
    elif filterBy == "unit":
        return [
                {
                    "$match" : {
                        "unit": {
                            "$eq": searchInput
                        }
                    }
                }
            ]
        
    elif filterBy == "price":
        return [
                {
                    "$match" : {
                        "price": {
                            "$eq": int(searchInput)
                        }
                    }
                }
            ]
        
    elif filterBy == "LowerPrice":
        return [
                {
                    "$match" : {
                        "price": {
                            "$lt": int(searchInput)
                        }
                    }
                }
            ]
        
    elif filterBy == "GreaterPrice":
        return [
                {
                    "$match" : {
                        "price": {
                            "$gt": int(searchInput)
                        }
                    }
                }
            ]
    else:
        return []