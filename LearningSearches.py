from backend.database.config import db
import pprint

product_col = db.products

# products =[
#     { "name": "Apple", "unit": "kg", "price": 3.5 },
#     { "name": "Banana", "unit": "kg", "price": 1.2 },
#     { "name": "Orange", "unit": "kg", "price": 2.8 },
#     { "name": "Tomato", "unit": "kg", "price": 2.3 },
#     { "name": "Potato", "unit": "kg", "price": 1.5 },
#     { "name": "Onion", "unit": "kg", "price": 1.0 },
#     { "name": "Carrot", "unit": "kg", "price": 2.0 },
#     { "name": "Cucumber", "unit": "kg", "price": 1.8 },
#     { "name": "Spinach", "unit": "kg", "price": 2.5 },
#     { "name": "Broccoli", "unit": "kg", "price": 3.0 },
#     { "name": "Chicken Breast", "unit": "kg", "price": 5.5 },
#     { "name": "Salmon Fillet", "unit": "kg", "price": 12.0 },
#     { "name": "Beef Steak", "unit": "kg", "price": 15.0 },
#     { "name": "Pork Chop", "unit": "kg", "price": 8.0 },
#     { "name": "Shrimp", "unit": "kg", "price": 10.0 },
#     { "name": "Eggplant", "unit": "kg", "price": 2.2 },
#     { "name": "Bell Pepper", "unit": "kg", "price": 3.0 },
#     { "name": "Zucchini", "unit": "kg", "price": 2.7 },
#     { "name": "Cauliflower", "unit": "kg", "price": 2.9 },
#     { "name": "Pineapple", "unit": "each", "price": 4.5 },
#     { "name": "Watermelon", "unit": "each", "price": 6.0 },
#     { "name": "Mango", "unit": "each", "price": 1.5 },
#     { "name": "Papaya", "unit": "each", "price": 3.0 },
#     { "name": "Cabbage", "unit": "kg", "price": 1.8 },
#     { "name": "Lettuce", "unit": "each", "price": 2.0 },
#     { "name": "Grapes", "unit": "kg", "price": 4.0 },
#     { "name": "Strawberries", "unit": "kg", "price": 6.0 },
#     { "name": "Blueberries", "unit": "kg", "price": 10.0 },
#     { "name": "Raspberries", "unit": "kg", "price": 9.0 },
#     { "name": "Peach", "unit": "each", "price": 1.3 },
#     { "name": "Plum", "unit": "each", "price": 1.2 },
#     { "name": "Avocado", "unit": "each", "price": 2.5 },
#     { "name": "Kiwi", "unit": "each", "price": 0.8 },
#     { "name": "Pomegranate", "unit": "each", "price": 2.2 },
#     { "name": "Coconut", "unit": "each", "price": 3.0 },
#     { "name": "Pumpkin", "unit": "kg", "price": 1.6 },
#     { "name": "Sweet Potato", "unit": "kg", "price": 2.4 },
#     { "name": "Ginger", "unit": "kg", "price": 6.5 },
#     { "name": "Garlic", "unit": "kg", "price": 4.0 },
#     { "name": "Radish", "unit": "kg", "price": 1.7 },
#     { "name": "Beetroot", "unit": "kg", "price": 2.1 },
#     { "name": "Apple", "unit": "kg", "price": 3.4 },
#     { "name": "Pear", "unit": "kg", "price": 3.8 },
#     { "name": "Cherry", "unit": "kg", "price": 7.0 },
#     { "name": "Apricot", "unit": "kg", "price": 5.0 },
#     { "name": "Melon", "unit": "each", "price": 5.5 },
#     { "name": "Durian", "unit": "kg", "price": 12.0 },
#     { "name": "Dragonfruit", "unit": "each", "price": 4.0 },
#     { "name": "Lychee", "unit": "kg", "price": 8.0 },
#     { "name": "Rambutan", "unit": "kg", "price": 7.5 }
# ]

# db.products.insert_many(products)

# find product by name
def product_by_name(name):
    pipeline = [
        {
            "$match" : {
                "name": name
            }
        }
    ]
    
    for product in product_col.aggregate(pipeline):
        print()
        pprint.pp(product)
        print()
        
        

# -------------------------- #


# calculate count of product found by name

def calculate_products_by_name(name):
    pipeline = [
        {
            "$match" : {
                "name": name
            }
        },
        {
            # $count helps you to count products found
            # numberProducts is the name of the field that you want to put count in
            "$count" : "numberProducts"
        }
    ]
    print()
    pprint.pp([product for product in product_col.aggregate(pipeline)])
    print()

# -------------------------- #


# get Average of price grouped by unit


def avg_price_group():
    pipeline = [
        {
            "$group": {
                # id you removed "_id" the group will not work
                "_id" : "$unit", # replace "$unit" with None if you want to get avg for all by one group
                # Create new average field for price
                "avgPrice" : {
                    # avg helps you to get average of price
                    "$avg" : "$price"
                }
            }
        }
    ]
    print()
    pprint.pp([product for product in product_col.aggregate(pipeline)])
    print()



def sum_price_group():
    pipeline = [
        {
            "$group": {
                # group by product unit
                "_id" : "$unit", 
                # Create new average field for price
                "SumPrices" : {
                    # sum helps you to calculate sum of prices for each group
                    "$sum" : "$price"
                }
            }
        }
    ]
    print()
    pprint.pp([product for product in product_col.aggregate(pipeline)])
    print()
    
def count_using_sum_group():
    pipeline = [
        {
            "$group": {
                # group by product unit
                "_id" : "$unit", 
                # Create new field
                "countProducts" : {
                    # add 1 everytime you found product for each group
                    "$sum" : 1
                }
            }
        }
    ]
    print()
    pprint.pp([product for product in product_col.aggregate(pipeline)])
    print()
    
    
def count_using_count_group_and_sort():
    pipeline = [
        {
            "$group": {
                # group by product unit
                "_id" : "$unit", 
                # Create new field
                "countProducts" : {
                    # add 1 everytime you found product for each group
                    "$count" : {}
                }
            }
        },
        {
            "$sort" : {
                # sort by field you created above
                "countProducts" : -1 # order descending / put 1 for ascending order
            }
        },
        {
            # limit result docs
            "$limit" : 2
        }
    ]
    print()
    pprint.pp([product for product in product_col.aggregate(pipeline)])
    print()
    

def get_countof_array_tags_that_in_product():
    pipeline = [
        {
            # unwind is used get out the array element into documents and duplicate it into array element's count
            # $tags is the field that contains array
            "$unwind" : "$tags"
        },
        {
            "$group": {
                "_id" : "$_id",
                "NumberOfTags": {
                    "$sum": 1
                }
            }
        },
        {
            "$group":{
                "_id": None,
                "AvgNumberOfTags" : {
                    "$avg" : "$NumberOfTags"
                }
            }
        }
    ]
    print()
    pprint.pp([product for product in product_col.aggregate(pipeline)])
    print()



def add_field():
    pipeline = [
        {
            "$addFields" : {
                # add field called NumberOfTags
                "NumberOfTags": {
                    # $size used to calculate count of element inside an array exists in docs
                    # $ifNull used to controll if $tags array doesn't exists in some docs
                    "$size" : {"$ifNull" : ["$tags", []]}
                }
            }
        },
        {
            "$group": {
                "_id": None,
                "AvgNumberOfTags" : {
                    "$avg" : "$NumberOfTags"
                }
            }
        }
    ]
    
    print()
    pprint.pp([product for product in product_col.aggregate(pipeline)])
    print()
    
    
def match_and_count(unit):
    pipeline = [
        {
            "$match" : {
                "unit" : unit
            }
        },
        {
            "$count" : "CountUnit"
        }
    ]
    
    print()
    pprint.pp([product for product in product_col.aggregate(pipeline)])
    print()
    
    
# Get product that price greater than 10 and unit is kg then only return id and name

def match_price_and_unit():
    pipeline = [
        {
            "$match" : {
                "unit" : "kg",
                "price" : {"$gt" : 10}
            }
        },
        {
            "$project":{
                "_id" : 1,
                "name" : 1
            }
        }
    ]
    
    print()
    pprint.pp([product for product in product_col.aggregate(pipeline)])
    print()
    

def starts_with_using_regex(name):
    pipeline = [
            {
                "$match" : {
                    "name": {
                        "$regex": f"^{name}", # find in name field, a name start with {name}
                        "$options": "i" # this is to ignore cases
                    }
                }
            }
        ]
    
    # pipeline = [
    #     {
    #         "$match" : {
    #             "price": {
    #                 "$lt": name
    #             }
    #         }
    #     }
    # ]
    
    print()
    pprint.pp([product for product in db.product.aggregate(pipeline)])
    print()
    

def group_and_push():
    pipeline = [
        {
            # group by unit
            "$group" : {
                "_id" : "$unit",
                # create field products and fill it with _id, name, price using $push
                "products" : {
                    # you can use this $push : "$name" if you want list of product name
                    "$push" : {
                        "_id": "$_id",
                        "name": "$name",
                        "price" : "$price"
                    }
                }
            }
        }
    ]
    
    products = [product for product in db.product.aggregate(pipeline)]
    pprint.pp(products)
    


def indexing(name):
    pipeline = [
        {
            "$search" : {
                "index" : "default",
                "text" : {
                    "query" : name,
                    "path": "name"
                }
            }
        }
    ]
    
    products = [product for product in db.product.aggregate(pipeline)]
    pprint.pp(products)
    

def indexing_compound():
    db.product.create_index({ "price": 1 })

    pipeline = [
        {
            "$match": { "price": { "$lt": 1 } }
        },{
            "$limit" : 5
        }
    ]
    
    products = [product for product in db.product.aggregate(pipeline)]
    pprint.pp(products)
    




indexing_compound()
pprint.pp([index for index in db.product.list_indexes()])

