from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()


# Import Info from dotenv
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
host = os.getenv("MONGO_HOST")


# Connect To Mongodb and Create DB
client = MongoClient(f"mongodb+srv://{username}:{password}@{host}")
db = client.grocery_store


# Schema Validator for Product
Product_Validator = {
    "$jsonSchema" : {
        "bsonType" : "object",
        "required" : ["name", "unit", "price"],
        "properties" : {
            "name" : {
                "bsonType" : "string",
                "description" : "Must be string"
            },
            "unit" : {
                "enum" : ["kg", "each"],
                "description" : "Must be 'kg' or 'each'"
            },
            "price" : {
                "bsonType" : "double",
                "minimum" : 0,
                "description" : "Must be Double and greater than 0"
            }
        }
    }
}


# Create Product collection on validator above
try:
    db.create_collection("product")
except Exception as e:
    print(e)


db.command("collMod" , "product" , validator = Product_Validator)