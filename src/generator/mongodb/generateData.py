# ===================#
#      MongoDB      #
# ===================#

import random
from random import seed
import json

# Functions
def generate_random_point_data(n):
    """
    Generates n random geospatial points in GeoJSON format.

    Args:
        n (int): Number of points to generate.

    Returns:
        str: GeoJSON string representing the generated points.
    """
    # Define the GeoJSON features list
    coordinates = []

    # Generate random coordinates in the range of -90 to 90 for longitude and -90 to 90 for latitude
    longitude = random.uniform(-90, 90)
    latitude = random.uniform(-90, 90)
    coordinates = [longitude, latitude]

    return coordinates


def generate_random_linestring_data(num_points):
    """
    Generates a random geospatial linestring in GeoJSON format.

    Args:
        num_points (int): Number of points to generate for the linestring.

    Returns:
        str: GeoJSON string representing the generated linestring.
    """
    # Define the GeoJSON features list
    coordinates = []

    # Generate random coordinates for the start and end points of the linestring
    for i in range(num_points):
        longitude = random.uniform(-90, 90)
        latitude = random.uniform(-90, 90)
        coordinates.append([longitude, latitude])

    return coordinates


def generate_random_polygon_data(num_points):
    """
    Generates a random geospatial polygon in GeoJSON format.

    Args:
        num_points (int): Number of points to generate for the polygon.

    Returns:
        str: GeoJSON string representing the generated polygon.
    """
    # Define the GeoJSON features list
    coordinates = [[]]
    firstLine = []

    # Generate random coordinates for the start and end points of the polygon
    for i in range(num_points):
        longitude = random.uniform(-90, 90)
        latitude = random.uniform(-90, 90)

        # We need to save the first point as the first and last point in a polygon always is the same
        if i == 0:
            firstLine = [longitude, latitude]
            coordinates[0].append([longitude, latitude])
        elif i == num_points - 1:
            coordinates[0].append(firstLine)
        else:
            coordinates[0].append([longitude, latitude])

    # Calculate the polygon's area (This is to make sure the polygon follows the "right-hand" rule - https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6)
    area = 0
    for i in range(num_points):
        j = (i + 1) % num_points
        area += (
            coordinates[0][i][0] * coordinates[0][j][1]
            - coordinates[0][j][0] * coordinates[0][i][1]
        )

    # If the area is negative, reverse the order of the vertices
    if area < 0:
        coordinates[0].reverse()

    return coordinates


def generate_one_of_datatype(datatype, randomSeed, pointsToGenerate):
    """
    Generates a single geospatial point, linestring, or polygon in GeoJSON format.

    Args:
        datatype ("point" | "linestring" | "polygon"): The datatype to generate
        randomSeed (number): The seed to use for random generation
        pointsToGenerate (number): The amount of points to generate for either a linestring or a polygon

    Returns:
        str: GeoJSON string representing the generated collection
    """
    # Define the GeoJSON features list
    seed(randomSeed)
    features = []
    functionToRun = None
    type = ""

    if datatype == "point":
        functionToRun = generate_random_point_data
        type = "Point"
    elif datatype == "linestring":
        functionToRun = generate_random_linestring_data
        type = "LineString"
    elif datatype == "polygon":
        functionToRun = generate_random_polygon_data
        type = "Polygon"

    # Create the GeoJSON feature for the polygon
    geojson = {"type": type, "coordinates": functionToRun(pointsToGenerate)}

    # Return the GeoJSON string
    return json.dumps(geojson)


def generate_collection_of_datatype(
    datatype, amountOfInstancesInItem, randomSeed, pointsToGenerate
):
    """
    Generates a collection of either geospatial points, linestrings, or polygons in GeoJSON format, effectively simulating a multipoint, multilinestring, and multipolygon, respectively.

    Args:
        datatype ("multipoint" | "multilinestring" | "multipolygon"): The datatype to generate
        amountOfInstancesInItem (number): The amount of point, linestring or polygon instances to insert into the multipoint, multilinestring or multipolygon
        randomSeed (number): The seed to use for random generation
        pointsToGenerate (number): The amount of points to generate for either a linestring or a polygon

    Returns:
        str: GeoJSON string representing the generated collection
    """
    # Define the GeoJSON features list
    seed(randomSeed)
    collection = []
    functionToRun = None
    type = ""

    # Check which datatype to create a query for
    if datatype == "multipoint":
        functionToRun = generate_random_point_data
        type = "MultiPoint"
    elif datatype == "multilinestring":
        functionToRun = generate_random_linestring_data
        type = "MultiLineString"
    elif datatype == "multipolygon":
        functionToRun = generate_random_polygon_data
        type = "MultiPolygon"

    for i in range(int(amountOfInstancesInItem)):
        collection.append(functionToRun(int(pointsToGenerate)))

    # Create the GeoJSON feature for the polygon
    geojson = {"type": type, "coordinates": collection}

    # Return the GeoJSON string
    return json.dumps(geojson)
