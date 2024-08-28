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
                "unit" : {
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
        
    elif filterBy == "price":
        return [
        {
            "$match" : {
                "price" : {
                    "$eq" : int(searchInput)
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
        
    elif filterBy == "LowerPrice":
        return [
        {
            "$match" : {
                "price" : {
                    "$lt" : int(searchInput)
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
        
    elif filterBy == "GreaterPrice":
        return [
        {
            "$match" : {
                "price" : {
                    "$gt" : int(searchInput)
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
    else:
        return []

def order_search_agg(filterBy, searchText, skip, limit):
    if filterBy == "customer":
        return [
            {
                "$match" : {
                    "customer" : {
                        "$regex" : f"^{searchText}"
                    }
                }
            },
            {
                "$facet" : {
                    "orders" : [{}, { "$skip" : skip }, { "$limit" : limit }],
                    "count" : [{ "$count" : "total_orders" }]
                }
            }
        ]
    elif filterBy == "product_id":
        return [
            {
                "$match" : {
                    "product_id" : {
                        "$eq" : searchText
                    }
                }
            },
            {
                "$facet" : {
                    "orders" : [{}, { "$skip" : skip }, { "$limit" : limit }],
                    "count" : [{ "$count" : "total_orders" }]
                }
            }
        ]
    elif filterBy == "qty":
        return [
            {
                "$match" : {
                    "qty" : {
                        "$eq" : int(searchText)
                    }
                }
            },
            {
                "$facet" : {
                    "orders" : [{}, { "$skip" : skip }, { "$limit" : limit }],
                    "count" : [{ "$count" : "total_orders" }]
                }
            }
        ]
    elif filterBy == "order_date":
        return [
            {
                "$match" : {
                    "order_date" : {
                        "$eq" : searchText
                    }
                }
            },
            {
                "$facet" : {
                    "orders" : [{}, { "$skip" : skip }, { "$limit" : limit }],
                    "count" : [{ "$count" : "total_orders" }]
                }
            }
        ]

