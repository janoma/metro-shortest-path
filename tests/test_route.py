from .context import network, route
from .context import Station, Network

import unittest


class RouteTestSuite(unittest.TestCase):
    """Test cases for computing shortest metro routes."""

    def testSingleStationNoColor(self):
        metro = Network("tests/single_line_single_station.json")
        r = route.findShortestRoute(metro, "A", "A")
        expected = list(map(metro.findStation, ["A"]))
        self.assertEqual(r, expected)

    def testTwoStationsNoColor(self):
        metro = Network("tests/single_line_two_stations.json")
        r = route.findShortestRoute(metro, "A", "B")
        expected = list(map(metro.findStation, ["A", "B"]))
        self.assertEqual(r, expected)

    def testThreeStationsNoColor(self):
        metro = Network("tests/single_line_three_stations.json")
        r = route.findShortestRoute(metro, "A", "C")
        expected = list(map(metro.findStation, ["A", "B", "C"]))
        self.assertEqual(r, expected)

    # Any of the two routes is a shortest route here
    def testThreeStationsWithAlternativeNoColor(self):
        metro = Network("tests/simple_alternative.json")
        r = route.findShortestRoute(metro, "A", "C")
        expected1 = list(map(metro.findStation, ["A", "B", "C"]))
        expected2 = list(map(metro.findStation, ["A", "D", "C"]))
        self.assertTrue(r == expected1 or r == expected2)

    def testSingleStationCorrespondingColor(self):
        metro = Network("tests/single_station_red.json")
        r = route.findShortestRoute(metro, "A", "A", "red")
        expected = list(map(metro.findStation, ["A"]))
        self.assertEqual(r, expected)

    # Ill-formed query, green train doesn't stop in a red station
    def testSingleStationWrongColor(self):
        metro = Network("tests/single_station_red.json")
        r = route.findShortestRoute(metro, "A", "A", "green")
        self.assertEqual(r, None)

    def testTwoStationsCorrespondingColor(self):
        metro = Network("tests/single_line_two_stations.json")
        r = route.findShortestRoute(metro, "A", "B", "red")
        expected = list(map(metro.findStation, ["A", "B"]))
        self.assertEqual(r, expected)

    # Ill-formed query, green train doesn't stop in a red station
    def testTwoStationsWrongColor(self):
        metro = Network("tests/single_line_two_stations.json")
        r = route.findShortestRoute(metro, "A", "B", "green")
        self.assertEqual(r, None)

    def testThreeStationsJumpingTheMiddleOne(self):
        metro = Network("tests/single_line_three_stations.json")
        r = route.findShortestRoute(metro, "A", "C", "green")
        expected = list(map(metro.findStation, ["A", "C"]))
        self.assertEqual(r, expected)

    def testShortestPathIsThroughLine2(self):
        metro = Network("tests/long_line_1_short_line_2.json")
        r = route.findShortestRoute(metro, "A", "F")
        expected = list(map(metro.findStation, ["A", "G", "F"]))
        self.assertEqual(r, expected)

    def testShortestPathIsThroughLine2GoingBack(self):
        metro = Network("tests/long_line_1_short_line_2.json")
        r = route.findShortestRoute(metro, "B", "F")
        expected = list(map(metro.findStation, ["B", "A", "G", "F"]))
        self.assertEqual(r, expected)

    def testShortestPathIsThroughLine1GoingBack(self):
        metro = Network("tests/long_line_1_short_line_2.json")
        r = route.findShortestRoute(metro, "G", "C")
        expected = list(map(metro.findStation, ["G", "A", "B", "C"]))
        self.assertEqual(r, expected)

    def testCaseFromAssignmentWithRedColor(self):
        metro = Network("tests/network_from_assignment.json")
        r = route.findShortestRoute(metro, "A", "F", "red")
        expected = list(map(metro.findStation, ["A", "B", "C", "H", "F"]))
        self.assertEqual(r, expected)

    def testCaseFromAssignmentWithGreenColor(self):
        metro = Network("tests/network_from_assignment.json")
        r = route.findShortestRoute(metro, "A", "F", "green")
        expected1 = list(map(metro.findStation, ["A", "B", "C", "D", "E", "F"]))
        expected2 = list(map(metro.findStation, ["A", "B", "C", "G", "I", "F"]))
        self.assertTrue(r == expected1 or r == expected2)

    def testCaseFromAssignmentWithNoColor(self):
        metro = Network("tests/network_from_assignment.json")
        r = route.findShortestRoute(metro, "A", "F")
        expected1 = list(map(metro.findStation, ["A", "B", "C", "D", "E", "F"]))
        expected2 = list(map(metro.findStation, ["A", "B", "C", "G", "I", "F"]))
        self.assertTrue(r == expected1 or r == expected2)


if __name__ == '__main__':
    unittest.main()
