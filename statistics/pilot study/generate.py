import matplotlib.pyplot as plt
import json
import numpy as np
from scipy.stats import f_oneway

def generateLineDiagram(database):
    """
    Generates a line diagram for the geospatial requests
    """
    # Reset plt
    plt.clf()
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
    # Reset plt
    plt.clf()

    x = np.array(["Point", "LineString", "MultiLineString"])
    y = []
    se = []

    # Set the title of the plot
    if database == "mysql":
        plt.title("MySQL standard error in milliseconds over 100 attempt")
    elif database == "mongodb":
        plt.title("MongoDB standard error in milliseconds over 100 attempt")

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

def performAnovaTest():
    # Define the data for MongoDB and MySQL
    all_means = []
    mongodb_means = []
    mysql_means = []

    # Get the files for the points
    points_mongodb = ["./mysql/point/geospatial_test_data.json", "./mysql/linestring/geospatial_test_data.json", "./mysql/multilinestring/geospatial_test_data.json"]
    point_mysql = ["./mongodb/point/geospatial_test_data.json", "./mongodb/linestring/geospatial_test_data.json", "./mongodb/multilinestring/geospatial_test_data.json"]
    
    # Loop through the files - MongoDB
    for file in points_mongodb:
        # Load the data from the json file
        with open(file, 'r') as f:
            data = json.load(f)

        # Get the time values from the data
        time_values = [d["time"] for d in data["values"]]
        plt.axis([None, None, 0, 80])

        # Plot the time values for geospatial requests
        mongodb_means.append(np.mean(time_values))

    # Loop through the files - MySQL
    for file in point_mysql:
        # Load the data from the json file
        with open(file, 'r') as f:
            data = json.load(f)

        # Get the time values from the data
        time_values = [d["time"] for d in data["values"]]
        plt.axis([None, None, 0, 80])

        # Plot the time values for geospatial requests
        mysql_means.append(np.mean(time_values))

    # Add the means to the list
    all_means.append(mysql_means)
    all_means.append(mongodb_means)

    # Perform one-way ANOVA test
    f_stat, p_val = f_oneway(*all_means)

    # Print the results
    print("F statistic:", f_stat)
    print("p-value:", p_val)


# Anova tests
performAnovaTest()

# Line diagrams
generateLineDiagram("mongodb")
generateLineDiagram("mysql")
# Bar diagrams
generateBarDiagram("mongodb")
generateBarDiagram("mysql")