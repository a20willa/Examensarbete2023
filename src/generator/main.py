from generateData import *
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["MongoDB_Tests"]
mycol = mydb["MongoDB_Tests"]

data = json.loads(generate_collection_of_datatype("point", 8))

mycol.insert_one(data)