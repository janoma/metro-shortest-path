from .context import network
from .context import Station, Color

import unittest


class NetworkTestSuite(unittest.TestCase):
    """Test cases for creating a metro network."""

    def testNonexistingFile(self):
        self.assertRaises(FileNotFoundError,
                network.readNetworkFromFile, "tests/nonexisting_file.json")

    def testEmptyNetworkNoLines(self):
        metro = network.readNetworkFromFile("tests/empty_network_no_lines.json")
        self.assertEqual(len(metro), 0)

    def testEmptyNetworkNoStations(self):
        metro = network.readNetworkFromFile("tests/two_lines_no_stations.json")
        self.assertEqual(len(metro), 2)

    def testNetworkFromAssignment(self):
        metro = network.readNetworkFromFile("tests/network_from_assignment.json")
        self.assertEqual(len(metro), 2)
        self.assertIn("line_1", metro)
        self.assertIn("line_2", metro)
        self.assertEqual(len(metro["line_1"]), 6)
        self.assertEqual(len(metro["line_2"]), 5)

    def testLine1FromAssignment(self):
        metro = network.readNetworkFromFile("tests/network_from_assignment.json")
        l1 = metro["line_1"]
        self.assertEqual(l1[0].get("id"), "A")
        self.assertEqual(l1[0].get("color"), None) # implicit null in A
        self.assertEqual(l1[1].get("id"), "B")
        self.assertEqual(l1[1].get("color"), None) # explicit null in B

    def testLine2FromAssignment(self):
        metro = network.readNetworkFromFile("tests/network_from_assignment.json")
        l2 = metro["line_2"]
        self.assertEqual(l2[1].get("id"), "G")
        self.assertEqual(l2[1].get("color"), "green")
        self.assertEqual(l2[2].get("id"), "H")
        self.assertEqual(l2[2].get("color"), "red")

    def testEmptyStationsGraph(self):
        lines = network.readNetworkFromFile("tests/empty_network_no_lines.json")
        stations = network.linesToStationsGraph(lines)
        self.assertEqual(len(stations), 0)

    def testSingleLineSingleStation(self):
        lines = network.readNetworkFromFile("tests/single_line_single_station.json")
        stations = network.linesToStationsGraph(lines)
        self.assertEqual(len(stations), 1)
        self.assertEqual(list(stations.keys())[0], Station("A"))
        self.assertEqual(stations[Station("A")], set())

    def testSingleLineTwoStations(self):
        lines = network.readNetworkFromFile("tests/single_line_two_stations.json")
        stations = network.linesToStationsGraph(lines)
        self.assertEqual(len(stations), 2)
        a = list(stations.keys())[0]
        b = list(stations.keys())[1]
        self.assertEqual(a, Station("A"))
        self.assertEqual(b, Station("B", "red"))
        self.assertEqual(len(stations[a]), 1)
        self.assertEqual(len(stations[b]), 1)
        self.assertEqual(stations[a].pop(), b)
        self.assertEqual(stations[b].pop(), a)

    def testSingleLineThreeStations(self):
        lines = network.readNetworkFromFile("tests/single_line_three_stations.json")
        stations = network.linesToStationsGraph(lines)
        a = Station("A", "green")
        b = Station("B", "red")
        c = Station("C")
        expected = {a : set([b]), b : set([a, c]), c : set([b])}
        self.assertEqual(stations, expected)

    def testTwoLinesOneCommonStation(self):
        lines = network.readNetworkFromFile("tests/two_lines_one_common_station.json")
        stations = network.linesToStationsGraph(lines)
        a = Station("A")
        b = Station("B")
        c = Station("C")
        d = Station("D")
        expected = {a : set([b, d]), b : set([a, c]), c : set([b]), d : set([a])}
        self.assertEqual(stations, expected)

    def testTwoLinesCommonStationInTheMiddle(self):
        lines = network.readNetworkFromFile("tests/two_lines_common_station_in_the_middle.json")
        stations = network.linesToStationsGraph(lines)
        a = Station("A")
        b = Station("B")
        c = Station("C")
        d = Station("D")
        e = Station("E")
        expected = {
                a : set([b]),
                b : set([a, c, d, e]),
                c : set([b]),
                d : set([b]),
                e : set([b])}
        self.assertEqual(stations, expected)

    def testCaseFromAssignment(self):
        lines = network.readNetworkFromFile("tests/network_from_assignment.json")
        stations = network.linesToStationsGraph(lines)
        a = Station("A")
        b = Station("B")
        c = Station("C")
        d = Station("D")
        e = Station("E")
        f = Station("F")
        g = Station("G", "green")
        h = Station("H", "red")
        i = Station("I", "green")
        expected = {
                a : set([b]),
                b : set([a, c]),
                c : set([b, d, g]),
                d : set([c, e]),
                e : set([d, f]),
                f : set([e, i]),
                g : set([c, h]),
                h : set([g, i]),
                i : set([f, h])}
        self.assertEqual(stations, expected)


if __name__ == '__main__':
    unittest.main()
