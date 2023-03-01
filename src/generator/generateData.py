import random
import json

def generate_random_point_data(n):
    """
    Generates n random geospatial points in GeoJSON format.

    Args:
        n (int): Number of points to generate.

    Returns:
        str: GeoJSON string representing the generated points.
    """
    # Define the GeoJSON features list
    features = []
    
    for i in range(n):
        # Generate random coordinates in the range of -180 to 180 for longitude and -90 to 90 for latitude
        longitude = random.uniform(-180, 180)
        latitude = random.uniform(-90, 90)

        # Create a GeoJSON feature for the point
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [longitude, latitude]
            },
            "properties": {}
        }
        
        # Append the feature to the features list
        features.append(feature)
    
    # Create the GeoJSON object
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    
    # Return the GeoJSON string
    return json.dumps(geojson)

def generate_random_linestring_data(num_points):
    """
    Generates a random geospatial linestring in GeoJSON format.

    Args:
        num_points (int): Number of points to generate for the linestring.

    Returns:
        str: GeoJSON string representing the generated linestring.
    """
    # Define the GeoJSON features list
    features = []
    coordinates = []

    # Generate random coordinates for the start and end points of the linestring
    for i in range(num_points):
        longitude = random.uniform(-180, 180)
        latitude = random.uniform(-90, 90)
        coordinates.append([longitude, latitude])

    # Create the GeoJSON feature for the linestring
    linestring_feature = {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates":  coordinates
        },
        "properties": {}
    }

    # Append the feature to the features list
    features.append(linestring_feature)

    # Create the GeoJSON object
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    # Return the GeoJSON string
    return json.dumps(geojson)

def generate_random_polygon_data(num_points):
    """
    Generates a random geospatial polygon in GeoJSON format.

    Args:
        num_points (int): Number of points to generate for the polygon.

    Returns:
        str: GeoJSON string representing the generated polygon.
    """
    # Define the GeoJSON features list
    features = []
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

    # Create the GeoJSON feature for the polygon
    polygon_feature = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates":  coordinates
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

def generate_collection_of_datatype(datatype):
    """
    Generates a collection of either geospatial points, linestrings, or polygons in GeoJSON format, effectively simulating a multipoint, multilinestring, and multipolygon, respectively.

    Args:
        datatype ("point" | "linestring" | "polygon"): The datatype to generate
        
    Returns:
        str: GeoJSON string representing the generated collection
    """

    

# Generate 10 random points
point_data = generate_random_point_data(10)
line_data = generate_random_linestring_data(5)
polygon_data = generate_random_polygon_data(5)

# Print the GeoJSON string
print(polygon_data)