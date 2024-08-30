from backend.database.config import db
import pprint

product = db.product
# student = db.student

# student.insert_one({
#     "name" : "yassine",
#     "Age" : 28
# })
# student.insert_one({
#     "name" : "abdallah",
#     "Age" : 8
# })
# student.insert_one({
#     "name" : "abdarrahman",
#     "Age" : 6
# })


# create index
# product.create_index({fields : 1 for ascending or -1 for descending}, name = the name of index, default_language = the language of the field)
# product.create_index("name", name="created_index_name_1", default_language='english') # by default ascending



# Compound index
## is when you create index of two fields
# product.create_index({"price" : -1}, name = "created_index_name_2") # first find and sort with name then price



# multikey index
## used to arrays 
# product.create_index({"tags" : 1}, name = "created_index_name") # pretend the tags is an array tags = ['A', 'B', 'C']

## you can't create compound multikeys for two arrays only one allowed or use 1 array and some field(not array)
# product.create_index({"name" : 1, "tags" : 1}, name = "created_index_name") # pretend the tags is an array tags = ['A', 'B', 'C']



# Covered Query
## Covered Query is when you use projection of the fields that are part of created index
# product.create_index("name", name="created_index_name") # i have created the index of name
# products = product.find({"name" : {"$regex" : "o"}}, {"_id" : 0, "name" : 1}) # i use project to get only name of products so this is the covered query 
# for pr in products:
#     pprint.pp(pr)



# unique index
## force field to be unique 
# student.create_index({"name": 1}, unique = True, name="created_index_name")
# pprint.pp([student for student in student.find()])


# sparse index is used to fix unique fields that has null in it (ignore the null fields for unique index)
# student.create_index({"tags": 1}, unique = True, sparse = True, name="created_index_name") # now name can accept null
# pprint.pp([student for student in student.find({"tags" : None}).hint({"tags" : 1})]) # to search using index you have created earlier. so tags null will be ignored



# fullText index
## for text searches you need to work with fullText index or searches will be slow
# student.create_index({"name" : "text"})
# students = student.find({
#     "$text" : {
#         "$search" : "yassine"
#     }
# })
# for pr in students:
#     pprint.pp(pr)

searchInput = "agsiuasgisa"

# Aggregation pipeline to get documents and count
pipeline = [
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
                        "$limit" : 10
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



# Run the aggregation
# data = list(product.aggregate(pipeline))


# products = data[0]["products"]
# count_products = data[0]["count"][0]["total_products"] if data[0]["count"] else 0

# for pr in products:
#     print(pr)
# print(count_products)

from datetime import datetime as dt
from bson import ObjectId
from backend.database.models import Order

# db.order.update_one({"_id" : ObjectId("66cef9195c53097f9ea6feec")},{
#     "$set" : {
#     "customer": "ilham",
#     "product_id": "66c7caf44f2aa8c1c7bc26dd",
#     "qty": 25,
#     "order_date": dt.strptime("2024-08-27T19:00:57.053000", r"%Y-%m-%dT%H:%M:%S.%f")
#     }
# })

# order = Order(customer="ilham", product_id="66c7caf44f2aa8c1c7bc26d3",qty=1000)

# db.order.insert_one(dict(order))

# db.drop_collection("order")



pipeline = [
    {
        
        "$lookup" : {
            "from" : "product",
            "localField" : "product_id",
            "foreignField" : "_id",
            "as" : "obj"
        }
    },
    {
        "$match" : {
            "customer" : "yassine"
        }
    }
]

# db.order.create_index({"product_id" : 1}, name="index_product_id")


# orders = [order for order in db.order.aggregate(pipeline)]

# orders = [order for order in db.order.find()]

# pprint.pp(orders)




# # Extract documents and count
# products = result[0]['products']
# document_count = result[0]['count'][0]['total_products'] if result[0]['count'] else 0

# Output the documents and count
# for doc in result:
#     print(doc)
# print(f"Total Documents: {document_count}")



# delete index
# student.drop_index("text")



product.drop_index("*")
# show indexes
for index in product.list_indexes():
    pprint.pp(index)
