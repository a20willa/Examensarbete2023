#===================#
#       MySQL       #
#===================#

from generateData import generate_collection_of_datatype, generate_one_of_datatype
import pymongo
from dotenv import dotenv_values
import mysql.connector 
import re

# Create mongodb client
config = dotenv_values(".env")
myclient = pymongo.MongoClient()
sqldb = mysql.connector.connect(
  host=config["mysql_host"],
  user=config["mysql_user"],
  password=config["mysql_user_password"],
  database=config["mysql_database"]
)

mycursor = sqldb.cursor()

# Start of application
print("Starting...")

# Remove everyting in the database
try:
    # Delete everythinng
    sql = "DROP TABLE IF EXISTS {}".format(config["mysql_table_name"])    
    mycursor.execute(sql)
except Exception as e:
    print("Table does not exist or database is not running")

try:
    sql = "CREATE TABLE {} (id INT NOT NULL AUTO_INCREMENT, g GEOMETRY, PRIMARY KEY (id))".format(config["mysql_table_name"])    
    mycursor.execute(sql)
except Exception as e:
    print("Database is not running")

# Functions
def insertCollections(amountOfQueriesToGenerate):
    """
    Inserts x collection instance documents into a given collection

    Args:
        amountOfQueriesToGenerate (number): The amount of documents to generate
    """
    mysqlSpatialData = []
    for i in range(amountOfQueriesToGenerate):
        mysqlSpatialData.append(re.sub(r',\s*\)', ')', generate_collection_of_datatype("point", 100, 3)))

    sql = "INSERT INTO {} (g) VALUES (ST_GeomFromText(%s))".format(config["mysql_table_name"])
    vals = [(val,) for val in mysqlSpatialData]
    print(vals)
    mycursor.executemany(sql, vals)
        
def insertOnes(amountOfQueriesToGenerate):
    """
    Inserts x single instance queries into a given collection

    Args:
        amountOfQueriesToGenerate (number): The amount of documents to generate
    """
    mysqlSpatialData = []
    for i in range(amountOfQueriesToGenerate):
        mysqlSpatialData.append(re.sub(r',\s*\)', ')', generate_one_of_datatype("polygon", 100, 3)))

    sql = "INSERT INTO {} (g) VALUES (ST_GeomFromText(%s))".format(config["mysql_table_name"])
    vals = [(val,) for val in mysqlSpatialData]
    print(vals)
    mycursor.executemany(sql, vals)

def createSeperator(text, matchStringLength, customLength=None):
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
    sql = "SELECT ST_AsText(g) from {}".format(config["mysql_table_name"])
    mycursor.execute(sql)
    result = mycursor.fetchall()
    separator, separator_line = createSeperator("Results", max(result, key=len), 50)
    print(separator)
    for entry in result:
        print(entry)
    print(separator_line)


# Either of these can be called
#insertCollections(100)
insertOnes(8)

# Needed to actually commit the changes, otherwise nothing will land in the databbase
sqldb.commit()

# Print resutls
select()

# Program is finished
print("Done")