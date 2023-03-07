from generateData import generate_collection_of_datatype, generate_one_of_datatype, json
import pymongo
from dotenv import dotenv_values

# Create mongodb client
config = dotenv_values(".env")
myclient = pymongo.MongoClient()
mydb = myclient[config["mongodb_database"]]
mycol = mydb[config["mongodb_collection_name"]]

# Start of application
print("Starting...")

# Remove everyting in the database
try:
    mycol.delete_many({})
except pymongo.errors.ServerSelectionTimeoutError:
    print("Could not connect to MongoDB database, is it running?")
    exit(1)

# Functions
def insertCollections(amountOfDocumentsToGenerate):
    """
    Inserts x collection instance documents into a given collection

    Args:
        amountOfDocumentsToGenerate (number): The amount of documents to generate
    """
    for i in range(amountOfDocumentsToGenerate):
        data = json.loads(generate_collection_of_datatype("point", 100, i, 100))
        mycol.insert_one(data)

def insertOnes(amountOfFilesToGenerate):
    """
    Inserts x single instance documents into a given collection

    Args:
        amountOfDocumentsToGenerate (number): The amount of documents to generate
    """
    for i in range(amountOfFilesToGenerate):
        data = json.loads(generate_one_of_datatype("polygon", i, 10))
        mycol.insert_one(data)

# Either of these can be called
print("Done")
#insertCollections(100)
insertOnes(100)