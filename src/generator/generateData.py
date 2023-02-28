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

# Generate 10 random points
point_data = generate_random_point_data(10)

# Print the GeoJSON string
print(point_data)
