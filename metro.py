import argparse, pprint

from metro.network import Network
from metro.route import findShortestRoute

parser = argparse.ArgumentParser(
        description="Finds the shortest route between two metro stations")
parser.add_argument("-n",
        "--network",
        type=str,
        required=True,
        help="JSON file containing the metro network")
parser.add_argument("-s",
        "--start",
        type=str,
        required=True,
        help="The starting station")
parser.add_argument("-e",
        "--end",
        type=str,
        required=True,
        help="The end station")
parser.add_argument("-c",
        "--color",
        type=str,
        default=None,
        help="The color of the train for the ride")
args = parser.parse_args()

if __name__ == '__main__':
    # Call the route-finding function
    route = findShortestRoute(
            Network(args.network), args.start, args.end, args.color)

    # Print the obtained route
    pprinter = pprint.PrettyPrinter()
    pprinter.pprint(route)
