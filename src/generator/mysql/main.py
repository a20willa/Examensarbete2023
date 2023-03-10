# ===================#
#       MySQL       #
# ===================#

# Import needed dependencies
from generateData import generate_collection_of_datatype, generate_one_of_datatype
import pymongo
from dotenv import dotenv_values
import mysql.connector
import re
import sys

# Import helper functions
sys.path.insert(1, 'src/generator/helpers')
from command_line_parser import command_line_parser

# Create mongodb client
config = dotenv_values(".env")
myclient = pymongo.MongoClient()
sqldb = mysql.connector.connect(
    host=config["mysql_host"],
    user=config["mysql_user"],
    password=config["mysql_user_password"],
    database=config["mysql_database"]
)

# Creates the cursor needed to execute queries
mycursor = sqldb.cursor()

# Drop the table as it needs to be empty before adding new data
try:
    #
    sql = "DROP TABLE IF EXISTS {}".format(config["mysql_table_name"])
    mycursor.execute(sql)
except Exception as e:
    print(e)

# Create the table with a id and a single column for the geospatial data
try:
    sql = "CREATE TABLE {} (id INT NOT NULL AUTO_INCREMENT, g GEOMETRY, PRIMARY KEY (id))".format(
        config["mysql_table_name"])
    mycursor.execute(sql)
except Exception as e:
    print(e)

# Create functions to insert data into MySQL


def insertCollections(amountOfQueriesToGenerate, type):
    """
    Inserts x collection instance documents into a given collection

    Args:
        amountOfQueriesToGenerate (number): The amount of documents to generate
    """
    mysqlSpatialData = []

    # Create all queries and put them in an array
    for i in range(amountOfQueriesToGenerate):
        mysqlSpatialData.append(re.sub(r',\s*\)', ')',
                                generate_collection_of_datatype(type, 100, 3)))

    # Run the queries using the "executemany()" function
    sql = "INSERT INTO {} (g) VALUES (ST_GeomFromText(%s))".format(
        config["mysql_table_name"])
    vals = [(val,) for val in mysqlSpatialData]
    print(vals)
    mycursor.executemany(sql, vals)


def insertOnes(amountOfQueriesToGenerate, type, pointsToGenerate):
    """
    Inserts x single instance queries into a given collection

    Args:
        amountOfQueriesToGenerate (number): The amount of documents to generate
        type ("point" | "linestring" | "polygon"): The datatype to generate
        pointsToGenerate (number): The amount of points to generate for strings or polygons
    """
    mysqlSpatialData = []

    # Create all queries and put them in an array
    for i in range(amountOfQueriesToGenerate):
        mysqlSpatialData.append(re.sub(r',\s*\)', ')', generate_one_of_datatype(type, 100, pointsToGenerate)))

    # Run the queries using the "executemany()" function
    sql = "INSERT INTO {} (g) VALUES (ST_GeomFromText(%s))".format(
        config["mysql_table_name"])
    vals = [(val,) for val in mysqlSpatialData]
    mycursor.executemany(sql, vals)


def createSeperator(text, matchStringLength, customLength=None):
    """
    Creates seperators (i.e. =====) to make output prettier

    Args:
        text (string): The text to be in the middle of the equal signs
        matchStringLength (string): Text to match the length of (i.e. if this word is 30 characters, the return value of this function will be 30 characters too)
        customLength (number): A custom length of the return value of this function (overrides matchStringLength)
    Returns:
        separator, separator_line: Both the header (`====text====`) and footer (`============`)
    """
    if customLength:
        separator_length = customLength
    else:
        separator_length = len(matchStringLength)

    left_side = (separator_length - len(text)) // 2
    right_side = separator_length - len(text) - left_side
    separator = "=" * left_side + text + "=" * right_side
    separator_line = "=" * separator_length

    return separator, separator_line


def select():
    """
    Executes a select statement to print the table contents in human readable form
    """
    sql = "SELECT ST_AsText(g) from {}".format(config["mysql_table_name"])
    mycursor.execute(sql)
    result = mycursor.fetchall()
    separator, separator_line = createSeperator(
        "Results", max(result, key=len), 50)
    print(separator)
    for entry in result:
        print(entry)
    print(separator_line)


def main():
    # Get command line arguments
    amount, type, pointsToGenerate = command_line_parser()

    # Notify that the application is startinng
    print("Starting...")

    # insertCollections(100)
    insertOnes(amount, type, pointsToGenerate)

    # Needed to actually commit the changes, otherwise nothing will land in the databbase
    sqldb.commit()

    # Print resutls
    select()
    print("Done")


main()
