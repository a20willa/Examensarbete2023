from generateData import generate_collection_of_datatype, generate_one_of_datatype, json
import pymongo

# Create mongodb client
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["MongoDB_Tests"]
mycol = mydb["MongoDB_Tests"]

# Remove everyting in the database
mycol.delete_many({})

# Functions
def insertCollections(amountOfDocumentsToGenerate):
    """
    Inserts documents into a given collection

    Args:
        amountOfDocumentsToGenerate (number): The amount of documents to generate
    """
    for i in range(amountOfDocumentsToGenerate):
        data = json.loads(generate_collection_of_datatype("point", 100, i, 100))
        mycol.insert_one(data)

def insertOnes(amountOfFilesToGenerate):
    """
    Inserts documents into a given collection

    Args:
        amountOfDocumentsToGenerate (number): The amount of documents to generate
    """
    for i in range(amountOfFilesToGenerate):
        data = json.loads(generate_one_of_datatype("point", i, 100))
        mycol.insert_one(data)

# Either of these can be called
insertCollections(100)
# insertOnes(100)