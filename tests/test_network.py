from .context import network

import unittest


class NetworkTestSuite(unittest.TestCase):
    """Test cases for creating a metro network."""

    def testNonexistingFile(self):
        self.assertRaises(FileNotFoundError,
                network.read_network_from_file, "tests/nonexisting_file.json")

    def testEmptyNetworkNoLines(self):
        metro = network.read_network_from_file("tests/empty_network_no_lines.json")
        self.assertEqual(len(metro), 0)

    def testEmptyNetworkNoStations(self):
        metro = network.read_network_from_file("tests/two_lines_no_stations.json")
        self.assertEqual(len(metro), 2)

    def testNetworkFromAssignment(self):
        metro = network.read_network_from_file("tests/network_from_assignment.json")
        self.assertEqual(len(metro), 2)
        self.assertIn("line_1", metro)
        self.assertIn("line_2", metro)
        self.assertEqual(len(metro["line_1"]), 6)
        self.assertEqual(len(metro["line_2"]), 5)

    def testLine1FromAssignment(self):
        metro = network.read_network_from_file("tests/network_from_assignment.json")
        l1 = metro["line_1"]
        self.assertEqual(l1[0].get("id"), "A")
        self.assertEqual(l1[0].get("color"), None) # implicit null in A
        self.assertEqual(l1[1].get("id"), "B")
        self.assertEqual(l1[1].get("color"), None) # explicit null in B

    def testLine2FromAssignment(self):
        metro = network.read_network_from_file("tests/network_from_assignment.json")
        l2 = metro["line_2"]
        self.assertEqual(l2[1].get("id"), "G")
        self.assertEqual(l2[1].get("color"), "green")
        self.assertEqual(l2[2].get("id"), "H")
        self.assertEqual(l2[2].get("color"), "red")

if __name__ == '__main__':
    unittest.main()
