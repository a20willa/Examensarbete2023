import matplotlib.pyplot as plt
import json

def generateLineDiagram():
    """
    Generates a line diagram for the geospatial requests
    """
    # Load the data from the json file
    with open('statistics/geospatial_test_data.json', 'r') as f:
        data = json.load(f)

    # Get the time values from the data
    time_values = [d["time"] for d in data["values"]]

    # Plot the time values for geospatial requests
    plt.title("Time for geospatial requests")
    plt.xlabel("Amount of requests")
    plt.ylabel("Time (ms)")
    plt.plot(time_values)
    plt.xticks(range(len(time_values)), range(len(time_values)))

    # Show the plot
    plt.show()

generateLineDiagram()