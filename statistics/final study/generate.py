import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import numpy as np
import pandas as pd
from io import StringIO
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import seaborn as sns


def generateLineDiagram(database):
    """
    Generates a line diagram for the geospatial requests
    """
    # Reset plt
    plt.clf()
    global_time_values = 0

    # Set the title of the plot
    if database == "mysql":
        plt.title("MySQL fetch query latency in milliseconds over 1000 attempts")
    elif database == "mongodb":
        plt.title("MongoDB fetch query latency in milliseconds over 1000 attempts")

    # Set the labels of the plot
    plt.xlabel("Amount of requests")
    plt.ylabel("Time (ms)")

    # Get the files for the points
    points = [
        "./{}/point/times.txt".format(database),
        "./{}/linestring/times.txt".format(database),
        "./{}/polygon/times.txt".format(database),
        "./{}/multipoint/times.txt".format(database),
        "./{}/multilinestring/times.txt".format(database),
        "./{}/multipolygon/times.txt".format(database),
    ]

    # Set colors
    colors = ["#1f77b4", "#2ca02c", "#9467bd", "#ff7f0e", "#d62728", "#8c564b"]

    # Loop through the files
    for file in points:
        # Get the time values from the data
        time_values = pd.read_csv(file, header=None)
        plt.axis([None, None, 0, 120])
        global_time_values = len(time_values)

        # Plot the time values for geospatial requests
        plt.plot(time_values, color=colors[points.index(file)])

    # Show the plot
    # Customize the x-axis tick locations and labels rotated 45 degrees
    plt.xticks(np.arange(0, global_time_values + 1, 100), rotation=45)

    # Shrink current axis's height by 10% on the bottom
    ax = plt.subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

    # Put a legend below current axis
    ax.legend(
        [
            "Point",
            "LineString",
            "Polygon",
            "MultiPoint",
            "MultiLineString",
            "MultiPolygon",
        ],
        loc="upper center",
        bbox_to_anchor=(0.5, -0.20),
        fancybox=True,
        shadow=True,
        ncol=5,
    )
    plt.savefig("./figures/{}_linechart.png".format(database), bbox_inches="tight")


def generateBarDiagram(database):
    """
    Generates a bar diagram for the geospatial requests
    """
    # Reset plt
    plt.clf()

    x = np.array(
        [
            "Point",
            "LineString",
            "Polygon",
            "MultiPoint",
            "MultiLineString",
            "MultiPolygon",
        ]
    )
    means = []
    std = []

    # Set the title of the plot
    if database == "mysql":
        plt.title(
            "MySQL fetch query latency standard deviation in milliseconds over 1000 attempts"
        )
    elif database == "mongodb":
        plt.title(
            "MongoDB fetch query latency standard deviation in milliseconds over 1000 attempts"
        )

    # Set the labels of the plot
    plt.ylabel("Time (ms)")

    # Get the files for the points
    points = [
        "./{}/point/times.txt".format(database),
        "./{}/linestring/times.txt".format(database),
        "./{}/polygon/times.txt".format(database),
        "./{}/multipoint/times.txt".format(database),
        "./{}/multilinestring/times.txt".format(database),
        "./{}/multipolygon/times.txt".format(database),
    ]

    # Loop through the files
    for file in points:
        # Get the time values from the data
        time_values = pd.read_csv(file, header=None)
        plt.axis([None, None, 0, 120])

        # Plot the time values for geospatial requests
        means.append(time_values.mean()[0])

        # Standard error
        std.append(time_values.std()[0])

    # Convert the list to a numpy array
    means = np.array(means)
    std = np.array(std)
    plt.xticks(rotation=30)

    # Plot the bar diagram
    plt.errorbar(x, means, yerr=std, fmt="none", color="black", capsize=5)
    # Fix colors
    plt.bar(
        x,
        means,
        color=["#1f77b4", "#2ca02c", "#9467bd", "#ff7f0e", "#d62728", "#8c564b"],
    )
    # plt.bar(x,means, color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])
    plt.savefig("./figures/{}_STD.png".format(database), bbox_inches="tight")


def generateStepDiagram(database):
    """
    Generates a bar diagram for the geospatial requests
    """
    # Reset plt
    plt.clf()

    x = np.array([100, 500, 400, 400 * 5, 400, 400 * 5])
    means = []

    # Set the title of the plot
    if database == "mysql":
        plt.title("MySQL time in milliseconds with number of points")
    elif database == "mongodb":
        plt.title("MongoDB time in milliseconds with number of points")

    # Set the labels of the plot
    plt.ylabel("Time (ms)")
    plt.xlabel("Amount of points")

    # Get the files for the points
    points = [
        "./{}/point/times.txt".format(database),
        "./{}/multipoint/times.txt".format(database),
        "./{}/linestring/times.txt".format(database),
        "./{}/multilinestring/times.txt".format(database),
        "./{}/polygon/times.txt".format(database),
        "./{}/multipolygon/times.txt".format(database),
    ]

    # Loop through the files
    for file in points:
        # Get the time values from the data
        time_values = pd.read_csv(file, header=None)
        plt.axis([None, None, 0, 120])

        # Plot the time values for geospatial requests
        means.append(time_values.mean()[0])

    # Convert the list to a numpy array
    means = np.array(means)

    # Fix colors and scatter plots
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    for i in range(len(x)):
        plt.scatter(x[i], means[i], color=colors[i])

    # Shrink current axis's height by 10% on the bottom
    ax = plt.subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

    # Put a legend below current axis
    ax.legend(
        [
            "Point",
            "MultiPoint",
            "LineString",
            "MultiLineString",
            "Polygon",
            "MultiPolygon",
        ],
        loc="upper center",
        bbox_to_anchor=(0.5, -0.20),
        fancybox=True,
        shadow=True,
        ncol=5,
    )

    ax.set_axisbelow(True)
    plt.grid()

    plt.savefig("./figures/{}_steps.png".format(database), bbox_inches="tight")


def anova(*data):  # * indicates, 0, 1 , 2 .. arguments
    if len(data) == 2:
        statistic, pvalue = stats.f_oneway(data[0], data[1])
    elif len(data) == 3:
        statistic, pvalue = stats.f_oneway(data[0], data[1], data[2])
    elif len(data) == 4:
        statistic, pvalue = stats.f_oneway(data[0], data[1], data[2], data[3])

    print("ANOVA Statistic " + str(statistic) + " and p-value " + str(pvalue))

    if pvalue < 0.05:  # alpha = 0.05
        return True
    else:
        return False


def getMeans():
    # Get the files
    points_mysql = [
        "./mysql/point/times.txt",
        "./mysql/multipoint/times.txt",
        "./mysql/linestring/times.txt",
        "./mysql/multilinestring/times.txt",
        "./mysql/polygon/times.txt",
        "./mysql/multipolygon/times.txt",
    ]
    points_mongodb = [
        "./mongodb/point/times.txt",
        "./mongodb/multipoint/times.txt",
        "./mongodb/linestring/times.txt",
        "./mongodb/multilinestring/times.txt",
        "./mongodb/polygon/times.txt",
        "./mongodb/multipolygon/times.txt",
    ]

    # Loop through the files - MongoDB
    for file in range(len(points_mongodb)):
        df_mongodb = pd.read_csv(points_mongodb[file], header=None)
        df_mysql = pd.read_csv(points_mysql[file], header=None)

        # Get the means
        mean_mongodb = df_mongodb.mean()
        mean_mysql = df_mysql.mean()

        # Print the results
        print(
            "Results for type: "
            + points_mongodb[file].split("/")[2].split(".")[0].upper()
        )

        # Print the means
        print("MongoDB: " + str(mean_mongodb[0]))
        print("MySQL: " + str(mean_mysql[0]))


def getAnova():
    # Get the files
    points_mysql = [
        "./mysql/point/times.txt",
        "./mysql/multipoint/times.txt",
        "./mysql/linestring/times.txt",
        "./mysql/multilinestring/times.txt",
        "./mysql/polygon/times.txt",
        "./mysql/multipolygon/times.txt",
    ]
    points_mongodb = [
        "./mongodb/point/times.txt",
        "./mongodb/multipoint/times.txt",
        "./mongodb/linestring/times.txt",
        "./mongodb/multilinestring/times.txt",
        "./mongodb/polygon/times.txt",
        "./mongodb/multipolygon/times.txt",
    ]

    # Loop through the files - MongoDB
    for file in range(len(points_mongodb)):
        df_mongodb = pd.read_csv(points_mongodb[file], header=None)
        df_mysql = pd.read_csv(points_mysql[file], header=None)

        # Print the results
        print(
            "Results for type: "
            + points_mongodb[file].split("/")[2].split(".")[0].upper()
        )

        # Run Anova on data groups
        if anova(df_mongodb, df_mysql):
            print("The means are different")
        else:
            print("No differences in means")

        print("")


def getTotal(type):
    # Get the files
    points_mysql = [
        "./mysql/point/times.txt",
        "./mysql/multipoint/times.txt",
        "./mysql/linestring/times.txt",
        "./mysql/multilinestring/times.txt",
        "./mysql/polygon/times.txt",
        "./mysql/multipolygon/times.txt",
    ]
    points_mongodb = [
        "./mongodb/point/times.txt",
        "./mongodb/multipoint/times.txt",
        "./mongodb/linestring/times.txt",
        "./mongodb/multilinestring/times.txt",
        "./mongodb/polygon/times.txt",
        "./mongodb/multipolygon/times.txt",
    ]

    # Store sums
    combined_mongodb = ""
    combined_mysql = ""

    # Loop through the files - MongoDB
    for file in range(len(points_mongodb)):
        with open(points_mongodb[file], "r") as file:
            combined_mongodb += file.read()

    # Loop through the files - MySQL
    for file in range(len(points_mysql)):
        with open(points_mysql[file], "r") as file:
            combined_mysql += file.read()

    # Read as df
    df_mongodb = pd.read_csv(StringIO(combined_mongodb), header=None)
    df_mysql = pd.read_csv(StringIO(combined_mysql), header=None)

    x = ["MongoDB", "MySQL"]
    means = np.array([df_mongodb.mean()[0], df_mysql.mean()[0]])
    if type == "std":
        std = np.array([df_mongodb.std()[0], df_mysql.std()[0]])
        plt.title(
            "MySQL and MongoDB fetch query latency standard deviation in milliseconds"
        )

    elif type == "sem":
        std = np.array([df_mongodb.sem()[0], df_mysql.sem()[0]])
        plt.title(
            "MySQL and MongoDB fetch query latency standard error in milliseconds"
        )

    # Create bar diagram
    plt.ylabel("Time (ms)")
    plt.errorbar(x, means, yerr=std, fmt="none", color="black", capsize=5)
    plt.bar(x, means, color=["#299637", "#2994e6"])
    plt.savefig("./figures/total.png")


def tuckeyTest():
    df = pd.read_csv('./mongodb/mongodb.csv', sep=",", header=None, names=["Point", "LineString", "Polygon", "MultiPoint", "MultiLineString", "MultiPolygon"])

    # Combine the data into a single column
    data = pd.melt(df, var_name='Group', value_name='Value')

    # Assign numeric values to each group
    group_labels, group_values = np.unique(data['Group'], return_inverse=True)

    # Perform Tukey test
    tukey_results = pairwise_tukeyhsd(data['Value'], data['Group'])
    
    # Convert confint array into a format suitable for plotting
    confint_min = tukey_results.confint[:, 0][group_values]
    confint_max = tukey_results.confint[:, 1][group_values]

    # Create dot plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(group_values, data['Value'], 'ko', markersize=4)  # Dots
    ax.vlines(group_values, confint_min, confint_max, colors='r', lw=1)  # Vertical lines

    # Set labels and title
    ax.set_xticks(np.arange(len(group_labels)))
    ax.set_xticklabels(group_labels)
    ax.set_xlabel('Group')
    ax.set_ylabel('Value')
    ax.set_title('Tukey Test')

    # Rotate x-axis labels if needed
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()

# getAnova()
# getMeans()
# getTotal("std")
# getTotal("sem")

# generateLineDiagram("mongodb")
# generateLineDiagram("mysql")
# generateBarDiagram("mongodb")
# generateBarDiagram("mysql")
# generateStepDiagram("mongodb")
# generateStepDiagram("mysql")

tuckeyTest()