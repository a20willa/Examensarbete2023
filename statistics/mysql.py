import matplotlib.pyplot as plt
import json
import numpy as np

def generateLineDiagram():
    """
    Generates a line diagram for the geospatial requests
    """
    global_time_values = 0

    plt.title("Geospatial requests times for mysql")
    plt.xlabel("Amount of requests")
    plt.ylabel("Time (ms)")

    files = ["/pilot study/mysql/point/geospatial_test_data.json", "/pilot study/mysql/linestring/geospatial_test_data.json", "/pilot study/mysql/polygon/geospatial_test_data.json", "/pilot study/mysql/multipoint/geospatial_test_data.json", "/pilot study/mysql/multilinestring/geospatial_test_data.json", "/pilot study/mysql/multipolygon/geospatial_test_data.json"]

    for file in files:
        # Load the data from the json file
        with open('statistics/' + file, 'r') as f:
            data = json.load(f)

        # Get the time values from the data
        time_values = [d["time"] for d in data["values"]]
        global_time_values = len(time_values)

        # Plot the time values for geospatial requests
        plt.plot(time_values, alpha=0.5)

    # Show the plot
    # Customize the x-axis tick locations and labels
    plt.xticks(np.arange(0, global_time_values, 1))
    plt.legend(["Point", "LineString", "Polygon", "MultiPoint", "MultiLineString", "MultiPolygon"])
    plt.show()

generateLineDiagram()