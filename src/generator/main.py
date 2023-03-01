from generateData import *

# Print the GeoJSON string
jsonToFile("out.json", generate_collection_of_datatype("point", 8))