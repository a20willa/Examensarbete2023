#===================#
#       MySQL       #
#===================#

import random
from random import seed
import json

# Functions


def generate_random_point_data(n):
    """
    Generates n random geospatial points in MySQL format.

    Args:
        n (int): Number of points to generate.

    Returns:
        str: MySQL string representing the generated points.
    """
    # Define the MySQL features list
    coordinates = []

    # Generate random coordinates in the range of -180 to 180 for longitude and -90 to 90 for latitude
    longitude = random.uniform(-180, 180)
    latitude = random.uniform(-90, 90)
    coordinates = [longitude, latitude]

    return coordinates


def generate_random_linestring_data(num_points):
    """
    Generates a random geospatial linestring in MySQL format.

    Args:
        num_points (int): Number of points to generate for the linestring.

    Returns:
        str: MySQL string representing the generated linestring.
    """
    # Define the MySQL features list
    coordinates = []

    # Generate random coordinates for the start and end points of the linestring
    for i in range(num_points):
        longitude = random.uniform(-180, 180)
        latitude = random.uniform(-90, 90)
        coordinates.append([longitude, latitude])

    return coordinates


def generate_random_polygon_data(num_points):
    """
    Generates a random geospatial polygon in MySQL format.

    Args:
        num_points (int): Number of points to generate for the polygon.

    Returns:
        str: MySQL string representing the generated polygon.
    """
    # Define the MySQL features list
    coordinates = [[]]
    firstLine = []

    # Generate random coordinates for the start and end points of the polygon
    for i in range(num_points):
        longitude = random.uniform(-180, 180)
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
        area += coordinates[0][i][0] * coordinates[0][j][1] - \
            coordinates[0][j][0] * coordinates[0][i][1]

    # If the area is negative, reverse the order of the vertices
    if area < 0:
        coordinates[0].reverse()

    return coordinates


def generate_one_of_datatype(datatype, randomSeed, pointsToGenerate):
    """
    Generates a single geospatial point, linestring, or polygon in MySQL format.

    Args:
        datatype ("point" | "linestring" | "polygon"): The datatype to generate
        randomSeed (number): The seed to use for random generation
        pointsToGenerate (number): The amount of points to generate for either a linestring or a polygon

    Returns:
        str: MySQL string representing the generated collection
    """
    # Define the MySQL features list
    seed(randomSeed)
    functionToRun = None
    type = ""
    prompt = ""

    # Get the data type
    if datatype == "point":
        functionToRun = generate_random_point_data
        type = "Point"
    elif datatype == "linestring":
        functionToRun = generate_random_linestring_data
        type = "LineString"
    elif datatype == "polygon":
        functionToRun = generate_random_polygon_data
        type = "Polygon"

    # Get coordinates
    coordinates = functionToRun(pointsToGenerate)

    # Check which datatype to create a query for
    if datatype == "point":
        prompt = "{}({}, {})".format(type, coordinates[0], coordinates[1])
    elif datatype == "linestring":
        prompt += "{}(".format(type)
        for point in coordinates:
            prompt += "{} {},".format(point[0], point[1])
        prompt += ")"
    elif datatype == "polygon":
        prompt += "{}((".format(type)
        for points in coordinates:
            for point in points:
                prompt += "{} {},".format(point[0], point[0])
        prompt += "))"

    # Return the MySQL string
    print(prompt)
    return prompt


def generate_collection_of_datatype(datatype, amountOfInstancesInItem, randomSeed, pointsToGenerate):
    """
    Generates a collection of either geospatial points, linestrings, or polygons in MySQL format, effectively simulating a multipoint, multilinestring, and multipolygon, respectively.

    Args:
        datatype ("point" | "linestring" | "polygon"): The datatype to generate
        amountOfInstancesInItem (number): The amount of point, linestring or polygon instances to insert into the multipoint, multilinestring or multipolygon
        randomSeed (number): The seed to use for random generation
        pointsToGenerate (number): The amount of points to generate for either a linestring or a polygon

    Returns:
        str: MySQL string representing the generated collection
    """
    # Define the MySQL features list
    seed(randomSeed)
    functionToRun = None
    type = ""
    prompt = ""

    # Get the data type
    if datatype == "point":
        functionToRun = generate_random_point_data
        type = "Point"
    elif datatype == "linestring":
        functionToRun = generate_random_linestring_data
        type = "LineString"
    elif datatype == "polygon":
        functionToRun = generate_random_polygon_data
        type = "Polygon"

    # Get coordinates
    coordinates = functionToRun(pointsToGenerate)

    # Check which datatype to create a query for
    if datatype == "point":
        prompt += "({}".format(type)
        for points in coordinates:
            prompt = "({} {}),".format(type, coordinates[0], coordinates[1])
        prompt += ")"
    elif datatype == "linestring":
        prompt += "{}(".format(type)
        for point in coordinates:
            prompt += "{} {},".format(point[0], point[1])
        prompt += ")"
    elif datatype == "polygon":
        prompt += "{}((".format(type)
        for points in coordinates:
            for point in points:
                prompt += "{} {},".format(point[0], point[0])
        prompt += "))"

    return prompt

def test(): 
    # Testing
    print(generate_one_of_datatype("point", 999,3))
    print()
    print(generate_one_of_datatype("linestring", 999,3))
    print()
    print(generate_one_of_datatype("polygon", 999,3))
    print()
    print(generate_collection_of_datatype("point", 10, 999, 3))
    print()
    print(generate_collection_of_datatype("linestring", 10, 999, 3))
    print()
    print(generate_collection_of_datatype("polygon", 10, 999, 3))

test()
