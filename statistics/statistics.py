import matplotlib.pyplot as plt
import json
import numpy as np

def generateLineDiagram(type, files):
    """
    Generates a line diagram for the geospatial requests
    """
    global_time_values = 0

    plt.title("Geospatial requests times for MongoDB and MySQL ({})".format(type))
    plt.xlabel("Amount of requests")
    plt.ylabel("Time (ms)")

    for file in files:
        print(file)
        # Load the data from the json file
        with open('statistics/' + file, 'r') as f:
            data = json.load(f)

        # Get the time values from the data
        time_values = [d["time"] for d in data["values"]]
        first_time_values = time_values[10:20]
        global_time_values = len(first_time_values)

        # Set the color of the line
        if "mysql" in file:
            color = "blue"
        else:
            color = "green"

        # Plot the time values for geospatial requests
        plt.plot(first_time_values,  color=color, alpha=0.5)

    # Show the plot
    # Customize the x-axis tick locations and labels
    plt.xticks(np.arange(0, global_time_values, 1))
    plt.legend(["MySQL", "MongoDB"])
    plt.show()

generateLineDiagram("point", ["databases/mysql/geospatial_test_data.json", "databases/mongodb/geospatial_test_data.json"])