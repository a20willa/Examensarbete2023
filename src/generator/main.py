from generateData import generate_collection_of_datatype, generate_one_of_datatype, json
import pymongo

# Create mongodb client
myclient = pymongo.MongoClient()
mydb = myclient["MongoDB_Tests"]
mycol = mydb["MongoDB_Tests"]

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
        data = json.loads(generate_one_of_datatype("point", i, 100))
        mycol.insert_one(data)

# Either of these can be called
insertCollections(100)
# insertOnes(100)