import sys
import getopt


def command_line_parser():
    amount = 1
    type = "point"
    points = 4

    if len(sys.argv) > 1:
        arguments, values = getopt.getopt(sys.argv[1:], "a:t:p:h:", [
                                          "amount=", "type=", "points=", "help"])
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-a", "--amount"):
                try:
                    int(currentValue)
                except ValueError:
                    print(
                        "Invalid value on argument '-p' or '--points', value must be a number")
                    exit(1)

                # Continue if value is a nubmer
                amount = int(currentValue)
            elif currentArgument in ("-t", "--type"):
                if currentValue not in ["point", "linestring", "polygon"]:
                    print(
                        "Invalid option on argument '-t' or '--type', must be either 'point', 'linestring' or 'polygon'")
                    exit(1)
                else:
                    type = currentValue
            elif currentArgument in ("-p", "--points"):
                # Check if value is a number
                try:
                    int(currentValue)
                except ValueError:
                    print(
                        "Invalid value on argument '-p' or '--points', value must be a number")
                    exit(1)

                # Check if value is over 4 as polygons must have at least 4 points
                if int(currentValue) < 4:
                    print(
                        "Invalid value on argument '-p' or '--points', value must be 4 or higher")
                    exit(1)

                # Continue if value is a nubmer
                points = int(currentValue)

            elif currentArgument in ("-h", "--help"):
                print('''
    This script generates spatial data of a given type and amount. It takes the following optional arguments:

    -a, --amount : number of geometries to generate (default: 1)
    -t, --type : type of geometry to generate, must be one of 'point', 'linestring', or 'polygon' (default: '')
    -h, --help :displays this text

    Example usage:
    python script.py --amount 10 --type linestring
                ''')
                exit(0)
    else:
        print("No arguments were given")
        exit(1)

    return amount, type, points
