from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def generateLineDiagram():
    """
    Generates a line diagram for the geospatial requests
    """
    # Reset plt
    plt.clf()

    # Set the labels of the plot
    plt.title("Demonstration of plugins causing spikes (LineString - MongoDB)")
    plt.xlabel("Amount of requests")
    plt.ylabel("Time (ms)")

    # Get the files for the points
    points = ["./mongodb_icognito.txt", "./mongodb_normal.txt"]

    # Set colors
    colors = ['#499e1f', '#ce1d1d']

    # Loop through the files
    for file in points:
        # Get the time values from the data
        time_values = pd.read_csv(file, header=None)
        plt.axis([None, None, 0, 80])
        global_time_values = len(time_values)

        # Plot the time values for geospatial requests
        plt.plot(time_values, color=colors[points.index(file)])

    # Show the plot
    # Customize the x-axis tick locations and labels
    plt.xticks(np.arange(0, global_time_values + 1, 100))
    ax = plt.subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                    box.width, box.height * 0.9])

    # Put a legend below current axis
    ax.legend(["Without plugins", "With plugins"],loc='upper center', bbox_to_anchor=(0.5, -0.15),
            fancybox=True, shadow=True, ncol=5)
    plt.savefig('./figures/linechart.png')

generateLineDiagram()
