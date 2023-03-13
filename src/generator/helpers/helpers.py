import sys
import getopt


help_text = '''
Usage: python main.py [OPTIONS]

Options:
-a, --amount INTEGER: Number of geometries to generate (default: 1)
-t, --type TEXT [REQUIRED]: Type of geometry to generate, must be one of 'point', 'multipoint', 'linestring', 'multilinestring', 'polygon' or 'multipolygon'
-h, --help: Displays this text
-p, --points INTEGER: The amount of points to generate for a linestring or polygon (default: 4, minimum: 4)

Example usage:
python main.py --amount 10 --type linestring --points 10
'''


def command_line_parser():
    amount = 1
    type = "point"
    points = 4
    instances = 10
    seed = 420

    if len(sys.argv) > 1:
        arguments, values = getopt.getopt(sys.argv[1:], "a:t:p:i:h", [
                                          "amount=", "type=", "points=", "instances", "help"])
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-a", "--amount"):
                # Check if value is a number
                try:
                    int(currentValue)
                except ValueError:
                    print(
                        "Invalid value on argument '-a' or '--amount', value must be a number")
                    exit(1)
            elif currentArgument in ("-p", "--points"):
                # Check if value is a number
                try:
                    int(currentValue)
                except ValueError:
                    print(
                        "Invalid value on argument '-p' or '--points', value must be a number")
                    exit(1)

                # Continue if value is a nubmer
                amount = int(currentValue)
            elif currentArgument in ("-t", "--type"):
                if currentValue not in ["point", "multipoint", "linestring", "multilinestring", "polygon", "multipolygon"]:
                    print(
                        "Invalid option on argument '-t' or '--type', must be either 'point', 'multipoint', 'linestring', 'multilinestring', 'polygon' or 'multipolygon'")
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

            elif currentArgument in ("-i", "--instances"):
                # Check if value is a number
                try:
                    int(currentValue)
                except ValueError:
                    print(
                        "Invalid value on argument '-i' or '--instances', value must be a number")
                    exit(1)

                # Continue if value is a nubmer
                instances = currentValue

            elif currentArgument in ("-h", "--help"):
                print(help_text)
                exit(0)
    else:
        print(help_text)
        exit(1)

    return amount, type, points, instances, seed


def createSeperator(text, matchStringLength, customLength=None):
    """
    Creates seperators (i.e. =====) to make output prettier

    Args:
        text (string): The text to be in the middle of the equal signs
        matchStringLength (string): Text to match the length of (i.e. if this word is 30 characters, the return value of this function will be 30 characters too)
        customLength (number): A custom length of the return value of this function (overrides matchStringLength)
    Returns:
        separator, separator_line: Both the header (`====text====`) and footer (`============`)
    """
    if customLength:
        separator_length = customLength
    else:
        separator_length = len(matchStringLength)

    left_side = (separator_length - len(text)) // 2
    right_side = separator_length - len(text) - left_side
    separator = "=" * left_side + text + "=" * right_side
    separator_line = "=" * separator_length

    return separator, separator_line
