# ===================#
#       MySQL       #
# ===================#

# Import needed dependencies
from generateData import generate_collection_of_datatype, generate_one_of_datatype
from dotenv import dotenv_values
import mysql.connector
import re
import sys

# Import helper functions
sys.path.insert(1, "src/generator/helpers")
from helpers import command_line_parser, createSeperator

# Create mongodb client
config = dotenv_values(".env")
sqldb = mysql.connector.connect(
    host=config["mysql_host"],
    user=config["mysql_user"],
    password=config["mysql_user_password"],
    database=config["mysql_database"],
)

# Creates the cursor needed to execute queries
mycursor = sqldb.cursor()

# Drop the table as it needs to be empty before adding new data
try:
    sql = "DROP TABLE IF EXISTS {}".format(config["mysql_table_name"])
    mycursor.execute(sql)
except Exception as e:
    print(e)

# Create the table with a id and a single column for the geospatial data
try:
    sql = "CREATE TABLE {} (id INT NOT NULL AUTO_INCREMENT, g GEOMETRY, PRIMARY KEY (id))".format(
        config["mysql_table_name"]
    )
    mycursor.execute(sql)
except Exception as e:
    print(e)


def insertCollections(amount, type, points, instances, seed):
    """
    Inserts x collection instances queries into a given collection

    Args:
        amount (number): The amount of geometries to generate
        type ("multipoint" | "multilinestring" "multipolygon"): The datatype to generate
        points (number): The amount of points to generate for strings or polygons
        instances (number): The amount of geometry instances to generate within the collection
        seed (number): The seed for the generation
    """
    mysqlSpatialData = []

    # Create all queries and put them in an array
    for i in range(amount):
        mysqlSpatialData.append(
            re.sub(
                r",\s*\)",
                ")",
                generate_collection_of_datatype(type, instances, int(seed) + i, points),
            )
        )

    # Run the queries using the "executemany()" function
    sql = "INSERT INTO {} (type, g) VALUES (%s, ST_GeomFromText(%s))".format(
        config["mysql_table_name"]
    )
    vals = [(type, val,) for val in mysqlSpatialData]
    mycursor.executemany(sql, vals)



def insertOnes(amount, type, points, seed):
    """
    Inserts x single instance queries into a given collection

    Args:
        amount (number): The amount of geometries to generate
        type ("point" | "linestring" | "polygon"): The datatype to generate
        points (number): The amount of points to generate for strings or polygons
        seed (number): The seed for the generation
    """
    mysqlSpatialData = []

    # Create all queries and put them in an array
    for i in range(amount):
        mysqlSpatialData.append(
            re.sub(r",\s*\)", ")", generate_one_of_datatype(type, int(seed) + 1, points))
        )

    # Run the queries using the "executemany()" function
    sql = "INSERT INTO {} (type, g) VALUES (%s, ST_GeomFromText(%s))".format(
        config["mysql_table_name"]
    )
    vals = [(type, val,) for val in mysqlSpatialData]
    mycursor.executemany(sql, vals)


def select():
    """
    Executes a select statement to print the table contents in human readable form
    """
    sql = "SELECT ST_AsText(g) from {}".format(config["mysql_table_name"])
    mycursor.execute(sql)
    result = mycursor.fetchall()
    separator, separator_line = createSeperator("Results", max(result, key=len), 50)
    print(separator)
    for entry in result:
        print(entry)
    print(separator_line)


def main():
    # Remove table
    remove_table_query = """
        DROP TABLE IF EXISTS {}
    """.format(config["mysql_table_name"])
    mycursor.execute(remove_table_query)

    # Create table
    create_table_query = """
        CREATE TABLE IF NOT EXISTS {} (
            id INT PRIMARY KEY AUTO_INCREMENT,
            type TEXT,
            g GEOMETRY
        )
        """.format(config["mysql_table_name"])
    mycursor.execute(create_table_query)

    # Get command line arguments
    amount, type, points, instances, seed = command_line_parser()

    # Notify that the application is startinng
    print("Starting...\n")

    # Check type and run correct function
    if type == "point" or type == "linestring" or type == "polygon":
        insertOnes(amount, type, points, seed)
    else:
        insertCollections(amount, type, points, instances, seed)

    # Needed to actually commit the changes, otherwise nothing will land in the databbase
    sqldb.commit()

    # Print resutls
    select()
    print("\nDone!")


main()
