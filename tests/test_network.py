from .context import network

import unittest


class NetworkTestSuite(unittest.TestCase):
    """Test cases for creating a metro network."""

    def test_nonexisting_file(self):
        self.assertRaises(FileNotFoundError,
                network.read_network_from_file, "tests/nonexisting_file.json")

    def test_empty_network_no_lines(self):
        metro = network.read_network_from_file("tests/empty_network_no_lines.json")
        assert len(metro) == 0

    def test_empty_network_no_stations(self):
        metro = network.read_network_from_file("tests/two_lines_no_stations.json")
        assert len(metro) == 2

    def test_network_from_assignment(self):
        metro = network.read_network_from_file("tests/network_from_assignment.json")
        assert len(metro) == 2
        assert "line_1" in metro
        assert "line_2" in metro
        assert len(metro["line_1"]) == 6
        assert len(metro["line_2"]) == 5

    def test_line_1_from_assignment(self):
        metro = network.read_network_from_file("tests/network_from_assignment.json")
        l1 = metro["line_1"]
        assert l1[0].get("id") == "A"
        assert l1[0].get("color") == None # implicit null in A
        assert l1[1].get("id") == "B"
        assert l1[1].get("color") == None # explicit null in B

    def test_line_2_from_assignment(self):
        metro = network.read_network_from_file("tests/network_from_assignment.json")
        l2 = metro["line_2"]
        assert l2[1].get("id") == "G"
        assert l2[1].get("color") == "green"
        assert l2[2].get("id") == "H"
        assert l2[2].get("color") == "red"

if __name__ == '__main__':
    unittest.main()
