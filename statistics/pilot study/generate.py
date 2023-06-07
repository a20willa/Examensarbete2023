import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import numpy as np
import pandas as pd

def generateLineDiagram(database):
    """
    Generates a line diagram for the geospatial requests
    """
    # Reset plt
    plt.clf()
    global_time_values = 0

    # Set the title of the plot
    if database == "mysql":
        plt.title("MySQL fetch query latency in milliseconds over 100 attempts")
    elif database == "mongodb":
        plt.title("MongoDB fetch query latency in milliseconds over 100 attempts")

    # Set the labels of the plot
    plt.xlabel("Amount of requests")
    plt.ylabel("Time (ms)")

    # Get the files for the points
    points = ["./{}/point/times.txt".format(database), "./{}/linestring/times.txt".format(database), "./{}/multilinestring/times.txt".format(database)]

    # Set colors
    colors = ['#1f77b4', '#2ca02c', '#d62728']

    # Loop through the files
    for file in points:
        # Get the time values from the data
        time_values = pd.read_csv(file, header=None)
        plt.axis([None, None, 0, 120])
        global_time_values = len(time_values)

        # Plot the time values for geospatial requests
        plt.plot(time_values, color=colors[points.index(file)])

    # Show the plot
    # Customize the x-axis tick locations and labels
    plt.xticks(np.arange(0, global_time_values + 1, 10))
    ax = plt.subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                    box.width, box.height * 0.9])

    # Put a legend below current axis
    ax.legend(["Point", "LineString", "MultiLineString"],loc='upper center', bbox_to_anchor=(0.5, -0.15),
            fancybox=True, shadow=True, ncol=5)
    plt.savefig('./figures/{}_linechart.png'.format(database), bbox_inches='tight')

def generateBarDiagram(database):
    """
    Generates a bar diagram for the geospatial requests
    """
    # Reset plt
    plt.clf()

    x = np.array(["Point", "LineString", "MultiLineString"])
    means = []
    std = []

    # Set the title of the plot
    if database == "mysql":
        plt.title("MySQL fetch query standard deviation in milliseconds over 100 attempts")
    elif database == "mongodb":
        plt.title("MongoDB fetch query standard deviation in milliseconds over 100 attempts")

    # Set the labels of the plot
    plt.ylabel("Time (ms)")

    # Get the files for the points
    points = ["./{}/point/times.txt".format(database), "./{}/linestring/times.txt".format(database), "./{}/multilinestring/times.txt".format(database)]

    # Loop through the files
    for file in points:
        # Get the time values from the data
        time_values = pd.read_csv(file, header=None)
        plt.axis([None, None, 0, 120])

        # Plot the time values for geospatial requests
        means.append(time_values.mean()[0])

        # Standard error
        std.append(time_values.std()[0])

    # Show the plot
    # Customize the x-axis tick locations and labels
    plt.legend(["Point", "LineString", "MultiLineString"], loc='center left', bbox_to_anchor=(1, 0.5))

    # Convert the list to a numpy array
    means = np.array(means)
    std = np.array(std)

    # Plot the bar diagram
    plt.errorbar(x, means, yerr=std, fmt='none', color='black', capsize=5)
    # Fix colors
    plt.bar(x,means, color=['#1f77b4', '#2ca02c', '#d62728'])
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
    # Get the pilot study files
    points_mysql = ["./mysql/point/times.txt", "./mysql/linestring/times.txt", "./mysql/multilinestring/times.txt"]
    points_mongodb = ["./mongodb/point/times.txt", "./mongodb/linestring/times.txt", "./mongodb/multilinestring/times.txt"]

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
    # Get the pilot study files
    points_mysql = ["./mysql/point/times.txt", "./mysql/linestring/times.txt", "./mysql/multilinestring/times.txt"]
    points_mongodb = ["./mongodb/point/times.txt", "./mongodb/linestring/times.txt", "./mongodb/multilinestring/times.txt"]

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

getAnova()
# getMeans()

generateLineDiagram("mongodb")
generateLineDiagram("mysql")
generateBarDiagram("mongodb")
generateBarDiagram("mysql")