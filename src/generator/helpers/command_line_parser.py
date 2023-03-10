import sys, getopt

def command_line_parser():
    amount = 1
    type = "point"

    if len(sys.argv) > 1:
        arguments, values = getopt.getopt(sys.argv[1:], "a:t:h:", ["amount=", "type=", "help"])
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-a", "--amount"):
                try:
                    int(currentValue)
                except ValueError:
                    print("Value must be an innt")
                amount = int(currentValue)
            elif currentArgument in ("-t", "--type"):
                if currentValue not in ["point", "linestring", "polygon"]:
                    print("Invalid option on argument '-t' or '--type', must be either 'point', 'linestring' or 'polygon'") 
                    exit(1)
                else:
                    type = currentValue

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

    return amount, type

    