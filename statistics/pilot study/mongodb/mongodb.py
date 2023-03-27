import matplotlib.pyplot as plt
import json
import numpy as np

def generateLineDiagram():
    """
    Generates a line diagram for the geospatial requests
    """
    global_time_values = 0

    plt.title("MongoDB latency in milliseconds over 10 attempts")
    plt.xlabel("Amount of requests")
    plt.ylabel("Time (ms)")

    files = ["./point/geospatial_test_data.json", "./linestring/geospatial_test_data.json", "./polygon/geospatial_test_data.json", "./multipoint/geospatial_test_data.json", "./multilinestring/geospatial_test_data(1).json", "./multipolygon/geospatial_test_data(1).json"]

    for file in files:
        # Load the data from the json file
        with open(file, 'r') as f:
            data = json.load(f)

        # Get the time values from the data
        time_values = [d["time"] for d in data["values"]]
        global_time_values = len(time_values)

        # Plot the time values for geospatial requests
        plt.plot(time_values)

    # Show the plot
    # Customize the x-axis tick locations and labels
    plt.xticks(np.arange(0, global_time_values, 1))
    plt.legend(["Point", "LineString", "Polygon", "MultiPoint", "MultiLineString", "MultiPolygon"], loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.savefig('mongodb.png')

generateLineDiagram()