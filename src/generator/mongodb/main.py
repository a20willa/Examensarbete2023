# ===================#
#      MongoDB      #
# ===================#

from generateData import generate_collection_of_datatype, generate_one_of_datatype, json
import pymongo
from dotenv import dotenv_values
import sys

# Create mongodb client
config = dotenv_values(".env")
client = pymongo.MongoClient()
mydb = client[config["mongodb_database"]]
col = mydb[config["mongodb_collection_name"]]

# Import helper functions
sys.path.insert(1, 'src/generator/helpers')
from helpers import command_line_parser, createSeperator

# Remove everyting in the database
try:
    col.delete_many({})
except pymongo.errors.ServerSelectionTimeoutError:
    print("Could not connect to MongoDB database, is it running?")
    exit(1)

def insertCollections(amount, type, points, instances, seed):
    """
    Inserts x collection instances queries into a given collection

    Args:
        amount (number): The amount of geometries to generate
        type ("point" | "multipoint" | "linestring" | "multilinestring" | "polygon" | "multipolygon"): The datatype to generate
        points (number): The amount of points to generate for strings or polygons
        instances (number): The amount of geometry instances to generate within the collection
        seed (number): The seed for the generation
    """
    for i in range(amount):
        data = json.loads(generate_collection_of_datatype(
            type, instances, int(seed) + i, points))
        
        data = {'loc': data}
        col.insert_one(data)


def insertOnes(amount, type, points, seed):
    """
    Inserts x single instance queries into a given collection

    Args:
        amount (number): The amount of geometries to generate
        type ("point" | "linestring" | "polygon"): The datatype to generate
        points (number): The amount of points to generate for strings or polygons
        seed (number): The seed for the generation
    """
    for i in range(amount):
        data = json.loads(generate_one_of_datatype(type, int(seed) + i, points))
        data = {'loc': data}
        col.insert_one(data)

def select():
    """
    Executes a select statement to print the table contents in human readable form
    """
    separator, separator_line = createSeperator(
    "Results", max(col.find({}), key=len), 50)
    
    print(separator)
    for x in col.find({}):
        print(x)
    print(separator_line)

def main():
    # Get command line arguments
    amount, type, points, instances, seed  = command_line_parser()

    # Notify that the application is startinng
    print("Starting...\n")

     # Check type and run correct function
    if type == "point" or type == "linestring" or type =="polygon":
        insertOnes(amount, type, points, seed)
    else:
        insertCollections(amount, type, points, instances, seed)
        
    # Create index
    col.create_index([("loc", "2dsphere")])
    
    # Print results
    select()
    print("\nDone!")

main()