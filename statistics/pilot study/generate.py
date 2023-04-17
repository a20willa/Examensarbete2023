import matplotlib.pyplot as plt
import json
import numpy as np

def generateLineDiagram(database):
    """
    Generates a line diagram for the geospatial requests
    """
    global_time_values = 0

    # Set the title of the plot
    if database == "mysql":
        plt.title("MySQL latency in milliseconds over 100 attempt")
    elif database == "mongodb":
        plt.title("MongoDB latency in milliseconds over 100 attempt")

    # Set the labels of the plot
    plt.xlabel("Amount of requests")
    plt.ylabel("Time (ms)")

    # Get the files for the points
    points = ["./{}/point/geospatial_test_data.json".format(database), "./{}/linestring/geospatial_test_data.json".format(database), "./{}/multilinestring/geospatial_test_data.json".format(database)]

    # Loop through the files
    for file in points:
        # Load the data from the json file
        with open(file, 'r') as f:
            data = json.load(f)

        # Get the time values from the data
        time_values = [d["time"] for d in data["values"]]
        plt.axis([None, None, 0, 80])
        global_time_values = len(time_values)

        # Plot the time values for geospatial requests
        plt.plot(time_values)

    # Show the plot
    # Customize the x-axis tick locations and labels
    plt.xticks(np.arange(0, global_time_values + 1, 10))
    plt.legend(["Point", "LineString", "MultiLineString"], loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.savefig('./figures/{}_linechart.png'.format(database))

def generateBarDiagram(database):
    """
    Generates a bar diagram for the geospatial requests
    """
    x = np.array(["Point", "LineString", "MultiLineString"])
    y = []
    se = []

    # Set the title of the plot
    if database == "mysql":
        plt.title("MySQL mean latency and standard error in milliseconds over 100 attempt")
    elif database == "mongodb":
        plt.title("MongoDB mean latency and standard error in milliseconds over 100 attempt")

    # Set the labels of the plot
    plt.xlabel("Amount of requests")
    plt.ylabel("Time (ms)")

    # Get the files for the points
    points = ["./{}/point/geospatial_test_data.json".format(database), "./{}/linestring/geospatial_test_data.json".format(database), "./{}/multilinestring/geospatial_test_data.json".format(database)]

    # Loop through the files
    for file in points:
        # Load the data from the json file
        with open(file, 'r') as f:
            data = json.load(f)

        # Get the time values from the data
        time_values = [d["time"] for d in data["values"]]
        plt.axis([None, None, 0, 80])

        # Plot the time values for geospatial requests
        y.append(np.mean(time_values))
        se.append(np.std(time_values))

    # Show the plot
    # Customize the x-axis tick locations and labels
    plt.legend(["Point", "LineString", "MultiLineString"], loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()

    # Convert the list to a numpy array
    y = np.array(y)
    se = np.array(se)

    # Plot the bar diagram
    plt.errorbar(x, y, yerr=se, fmt='none', color='black', capsize=5)
    plt.bar(x,y)
    plt.savefig('./figures/{}_SE.png'.format(database))

generateLineDiagram("mongodb")
generateBarDiagram("mongodb")