# ===================#
#      MongoDB      #
# ===================#

from generateData import generate_collection_of_datatype, generate_one_of_datatype, json
import pymongo
from dotenv import dotenv_values
import sys

# Create mongodb client
config = dotenv_values(".env")
myclient = pymongo.MongoClient()
mydb = myclient[config["mongodb_database"]]
mycol = mydb[config["mongodb_collection_name"]]

# Import helper functions
sys.path.insert(1, 'src/generator/helpers')
from helpers import command_line_parser, createSeperator

# Remove everyting in the database
try:
    mycol.delete_many({})
except pymongo.errors.ServerSelectionTimeoutError:
    print("Could not connect to MongoDB database, is it running?")
    exit(1)

def insertCollections(amountOfDocumentsToGenerate, type, pointsToGenerate):
    """
    Inserts x collection instance documents into a given collection

    Args:
        amountOfDocumentsToGenerate (number): The amount of documents to generate
    """
    for i in range(amountOfDocumentsToGenerate):
        data = json.loads(generate_collection_of_datatype(
            type, 100, i, pointsToGenerate))
        mycol.insert_one(data)


def insertOnes(amountOfDocumentsToGenerate, type, pointsToGenerate):
    """
    Inserts x single instance documents into a given collection

    Args:
        amountOfDocumentsToGenerate (number): The amount of documents to generate
    """
    for i in range(amountOfDocumentsToGenerate):
        data = json.loads(generate_one_of_datatype(type, i, pointsToGenerate))
        mycol.insert_one(data)


def select():
    """
    Executes a select statement to print the table contents in human readable form
    """
    separator, separator_line = createSeperator(
    "Results", max(mycol.find({}), key=len), 50)
    
    print(separator)
    for x in mycol.find({}):
        print(x)
    print(separator_line)

def main():
    # Get command line arguments
    amount, type, pointsToGenerate = command_line_parser()

    # Notify that the application is startinng
    print("Starting...\n")

    # insertCollections(100)
    insertOnes(amount, type, pointsToGenerate)

    select()

    # Either of these can be called
    print("\nDone!")

main()