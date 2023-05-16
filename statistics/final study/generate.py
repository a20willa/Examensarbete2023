import matplotlib.pyplot as plt
import json
import numpy as np
import scipy.stats as stats
import numpy as np
import pandas as pd
from io import StringIO

def generateLineDiagram(database):
    """
    Generates a line diagram for the geospatial requests
    """
    # Reset plt
    plt.clf()
    global_time_values = 0

    # Set the title of the plot
    if database == "mysql":
        plt.title("MySQL latency in milliseconds over 1000 attempts")
    elif database == "mongodb":
        plt.title("MongoDB latency in milliseconds over 1000 attempts")

    # Set the labels of the plot
    plt.xlabel("Amount of requests")
    plt.ylabel("Time (ms)")

    # Get the files for the points
    points = ["./{}/point/times.txt".format(database), "./{}/multipoint/times.txt".format(database), "./{}/linestring/times.txt".format(database), "./{}/multilinestring/times.txt".format(database), "./{}/polygon/times.txt".format(database), "./{}/multipolygon/times.txt".format(database)]

    # Set colors
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

    # Loop through the files
    for file in points:
        # Get the time values from the data
        time_values = pd.read_csv(file, header=None)
        plt.axis([None, None, 0, 150])
        global_time_values = len(time_values)

        # Plot the time values for geospatial requests
        plt.plot(time_values, color=colors[points.index(file)])

    # Show the plot
    # Customize the x-axis tick locations and labels rotated 45 degrees
    plt.xticks(np.arange(0, global_time_values + 1, 100), rotation=45)
    plt.legend(["Point", "MultiPoint", "LineString", "MultiLineString", "Polygon", "MultiPolygon"], loc='upper right')
    plt.savefig('./figures/{}_linechart.png'.format(database), bbox_inches='tight')

def generateBarDiagram(database):
    """
    Generates a bar diagram for the geospatial requests
    """
    # Reset plt
    plt.clf()

    x = np.array(["Point", "MultiPoint", "LineString", "MultiLineString", "Polygon", "MultiPolygon"])
    means = []
    std = []

    # Set the title of the plot
    if database == "mysql":
        plt.title("MySQL standard deviation in milliseconds over 1000 attempts")
    elif database == "mongodb":
        plt.title("MongoDB standard deviation in milliseconds over 1000 attempts")

    # Set the labels of the plot
    plt.ylabel("Time (ms)")

    # Get the files for the points
    points = ["./{}/point/times.txt".format(database), "./{}/multipoint/times.txt".format(database), "./{}/linestring/times.txt".format(database), "./{}/multilinestring/times.txt".format(database), "./{}/polygon/times.txt".format(database), "./{}/multipolygon/times.txt".format(database)]

    # Loop through the files
    for file in points:
        # Get the time values from the data
        time_values = pd.read_csv(file, header=None)
        plt.axis([None, None, 0, 80])

        # Plot the time values for geospatial requests
        means.append(time_values.mean()[0])

        # Standard error
        std.append(time_values.std()[0])

    # Convert the list to a numpy array
    means = np.array(means)
    std = np.array(std)
    plt.xticks(rotation=30)

    # Plot the bar diagram
    plt.errorbar(x, means, yerr=std, fmt='none', color='black', capsize=5)
    # Fix colors
    plt.bar(x,means, color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])
    plt.savefig('./figures/{}_STD.png'.format(database), bbox_inches='tight')

def anova(*data):  # * indicates, 0, 1 , 2 .. arguments
    if len(data) == 2:
        statistic, pvalue = stats.f_oneway(data[0], data[1])
    elif len(data) == 3:
        statistic, pvalue = stats.f_oneway(data[0], data[1], data[2])
    elif len(data) == 4:
        statistic, pvalue = stats.f_oneway(data[0], data[1], data[2], data[3])

    print("ANOVA Statistic " + str(statistic)+ " and p-value "+ str(pvalue))

    if pvalue < 0.05:  # alpha = 0.05
        return True
    else:
        return False

def getMeans():
    # Get the files
    points_mysql = ["./mysql/point/times.txt", "./mysql/multipoint/times.txt", "./mysql/linestring/times.txt", "./mysql/multilinestring/times.txt", "./mysql/polygon/times.txt", "./mysql/multipolygon/times.txt"]
    points_mongodb = ["./mongodb/point/times.txt", "./mongodb/multipoint/times.txt", "./mongodb/linestring/times.txt", "./mongodb/multilinestring/times.txt", "./mongodb/polygon/times.txt", "./mongodb/multipolygon/times.txt"]

    # Loop through the files - MongoDB
    for file in range(len(points_mongodb)):
        df_mongodb = pd.read_csv(points_mongodb[file], header=None)
        df_mysql = pd.read_csv(points_mysql[file], header=None)

        # Get the means
        mean_mongodb = df_mongodb.mean()
        mean_mysql = df_mysql.mean()

        # Print the results
        print("Results for type: " + points_mongodb[file].split("/")[2].split(".")[0].upper())

        # Print the means
        print("MongoDB: " + str(mean_mongodb[0]))
        print("MySQL: " + str(mean_mysql[0]))

def getAnova():
     # Get the files
    points_mysql = ["./mysql/point/times.txt", "./mysql/multipoint/times.txt", "./mysql/linestring/times.txt", "./mysql/multilinestring/times.txt", "./mysql/polygon/times.txt", "./mysql/multipolygon/times.txt"]
    points_mongodb = ["./mongodb/point/times.txt", "./mongodb/multipoint/times.txt", "./mongodb/linestring/times.txt", "./mongodb/multilinestring/times.txt", "./mongodb/polygon/times.txt", "./mongodb/multipolygon/times.txt"]

    # Loop through the files - MongoDB
    for file in range(len(points_mongodb)):
        df_mongodb = pd.read_csv(points_mongodb[file], header=None)
        df_mysql = pd.read_csv(points_mysql[file], header=None)
        
        # Print the results
        print("Results for type: " + points_mongodb[file].split("/")[2].split(".")[0].upper())

        # Run Anova on data groups
        if (anova(df_mongodb, df_mysql)):
            print("The means are different")
        else:
            print("No differences in means")

        print("")

def getTotal():
    # Get the files
    points_mysql = ["./mysql/point/times.txt", "./mysql/multipoint/times.txt", "./mysql/linestring/times.txt", "./mysql/multilinestring/times.txt", "./mysql/polygon/times.txt", "./mysql/multipolygon/times.txt"]
    points_mongodb = ["./mongodb/point/times.txt", "./mongodb/multipoint/times.txt", "./mongodb/linestring/times.txt", "./mongodb/multilinestring/times.txt", "./mongodb/polygon/times.txt", "./mongodb/multipolygon/times.txt"]

    # Store sums
    sum_mongodb = 0
    sum_mysql = 0

    # Loop through the files - MongoDB
    for file in range(len(points_mongodb)):
        df_mongodb = pd.read_csv(points_mongodb[file], header=None)
        df_mysql = pd.read_csv(points_mysql[file], header=None)

        total_mongodb = df_mongodb.sum()
        total_mysql = df_mysql.sum()

        sum_mongodb += int(total_mongodb[0])
        sum_mysql += int(total_mysql[0])

    print("Sum for MongoDB: {}ms".format(str(sum_mongodb)))
    print("Sum for MySQL: {}ms".format(str(sum_mysql)))

    # Create bar diagram
    plt.title("Avarage total speed over 5 repetitions with all datatypes in (ms)")
    plt.bar(["MongoDB", "MySQL"], [sum_mongodb, sum_mysql], color = ["#299637", "#2994e6"])
    plt.savefig("./figures/total.png")

# getAnova()
# getMeans()

getTotal()

# generateLineDiagram("mongodb")
# generateLineDiagram("mysql")
# generateBarDiagram("mongodb")
# generateBarDiagram("mysql")