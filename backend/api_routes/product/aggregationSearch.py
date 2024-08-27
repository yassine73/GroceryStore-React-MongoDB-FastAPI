def product_search_agg(filterBy , searchInput, limit, skip):
    
    if filterBy == "name":
        return [
        {
            "$match" : {
                "name" : {
                    "$regex" : f"^{searchInput}",
                    "$options" : "i"
                }
            }
        },
        {
            "$facet" : 
                {
                    "products" : [
                        {
                            "$match" : {}
                        },
                        {
                            "$skip" : skip
                        },
                        {
                            "$limit" : limit
                        }
                    ],
                    "count" : [
                        {
                            "$count" : "total_products"
                        }
                    ]
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
                },
                { "$limit" : limit},
                { "$skip" : skip }
            ]
        
    elif filterBy == "price":
        return [
                {
                    "$match" : {
                        "price": {
                            "$eq": int(searchInput)
                        }
                    }
                },
                { "$limit" : limit},
                { "$skip" : skip }
            ]
        
    elif filterBy == "LowerPrice":
        return [
                {
                    "$match" : {
                        "price": {
                            "$lt": int(searchInput)
                        }
                    }
                },
                { "$limit" : limit},
                { "$skip" : skip }
            ]
        
    elif filterBy == "GreaterPrice":
        return [
                {
                    "$match" : {
                        "price": {
                            "$gt": int(searchInput)
                        }
                    }
                },
                { "$limit" : limit},
                { "$skip" : skip }
            ]
    else:
        return []

