import random
from random import seed
import json

# Global settings
"""
The amount of points a linestring or polygon should have (minimum 4 due to geojson constraints)
Note that this does apply for points
"""
itterations = 4 

"""
The seed for random generation, MUST BE SET or data will NOT be the same across generation instances 
"""
seed(3)

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

    # Generate random coordinates in the range of -180 to 180 for longitude and -90 to 90 for latitude
    longitude = random.uniform(-180, 180)
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
        longitude = random.uniform(-180, 180)
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
        area += coordinates[0][i][0] * coordinates[0][j][1] - coordinates[0][j][0] * coordinates[0][i][1]

    # If the area is negative, reverse the order of the vertices
    if area < 0:
        coordinates[0].reverse()

    return coordinates

def generate_one_of_datatype(datatype):
    """
    Generates a single geospatial point, linestring, or polygon in GeoJSON format.

    Args:
        datatype ("point" | "linestring" | "polygon"): The datatype to generate
        
    Returns:
        str: GeoJSON string representing the generated collection
    """
    # Define the GeoJSON features list
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
    polygon_feature = {
        "type": "Feature",
        "geometry": {
            "type": type,
            "coordinates":  functionToRun(itterations)
        },
        "properties": {}
    }

    # Append the feature to the features list
    features.append(polygon_feature)

    # Create the GeoJSON object
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    # Return the GeoJSON string
    return json.dumps(geojson)
    

def generate_collection_of_datatype(datatype, length):
    """
    Generates a collection of either geospatial points, linestrings, or polygons in GeoJSON format, effectively simulating a multipoint, multilinestring, and multipolygon, respectively.

    Args:
        datatype ("point" | "linestring" | "polygon"): The datatype to generate
        length (number): The amount of items in the collection
        
    Returns:
        str: GeoJSON string representing the generated collection
    """
    # Define the GeoJSON features list
    collection = []
    features = []
    functionToRun = None
    type = ""

    if datatype == "point":
        functionToRun = generate_random_point_data
        type = "MultiPoint"
    elif datatype == "linestring":
        functionToRun = generate_random_linestring_data
        type = "MultiLineString"
    elif datatype == "polygon":
        functionToRun = generate_random_polygon_data
        type = "MultiPolygon"

    for i in range(length): 
        collection.append(functionToRun(itterations))

    # Create the GeoJSON feature for the polygon
    polygon_feature = {
        "type": "Feature",
        "geometry": {
            "type": type,
            "coordinates": collection
        },
        "properties": {}
    }

    # Append the feature to the features list
    features.append(polygon_feature)

    # Create the GeoJSON object
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    # Return the GeoJSON string
    return json.dumps(geojson)

def jsonToFile(filename, data):
    """
    Writes json data to a file

    Args:
        filename (string): The name of the file
        data (string): Json as a string 
    """
    with open(filename, "w") as json_file:
        json_file.write(data)