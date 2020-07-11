from .context import network, route

import unittest


class RouteTestSuite(unittest.TestCase):
    """Test cases for computing shortest metro routes."""

    def testFromSingleStationNetwork(self):
        r = route.findShortestRoute("foo", "A", "B")
        self.assertEqual(len(r), 0)


if __name__ == '__main__':
    unittest.main()
