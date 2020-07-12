import copy

from . import Station, Color, Network
from . import colorFromStr

def findShortestRoutesFromStation(
        graph: dict,
        start: Station) -> dict:
    # Creating the set as set(graph.keys()) doesn't work, so using
    # a small trick to compute the union of an empty set with the key set
    queue = set() | graph.keys()

    # For the relevant notion of distance here,
    # where the distance between neighbors is at most 1,
    # the size of the graph plus one works as infinity
    infinity = 1 + len(graph)
    dist = dict(zip(queue, [infinity] * len(queue)))

    # This is the mapping we'll be returning
    prev = dict()

    dist[start] = 0
    while len(queue) > 0:
        u = min(queue, key = lambda s: dist[s])
        queue.remove(u)

        for v in graph[u] & queue:
            # Technically, this could be dist[u] + weight(u, v),
            # but the weight in this case is always 1.
            alt = dist[u] + 1
            if alt <  dist[v]:
                dist[v] = alt
                prev[v] = u

    return prev

def findShortestRouteImpl(
        graph: dict,
        start: Station,
        end: Station,
        color: Color):
    assert start in graph
    assert end in graph

    # Get rid of some annoying corner cases right away
    if start == end:
        if color is not None and color != start.color:
            # This is basically a prankster query
            return None
        return [start]

    # Let's make our life easier: remove nodes that would be unreachable
    # if a color was requested, and assume a direct connection from the
    # previously-disconnected nodes that were immediately before and after them
    workingGraph = copy.deepcopy(graph)
    if color is not None:
        for station, neighbors in graph.items():
            for neighbor in neighbors:
                if neighbor.color is not None and neighbor.color != color:
                    workingGraph[station] |= graph[neighbor]
                    workingGraph[station].remove(station)

        # Now we remove the unreachable stations
        for station in graph.keys():
            if station.color is not None and station.color != color:
                workingGraph.pop(station)
                for neighbors in workingGraph.values():
                    neighbors.discard(station)

    # Dijkstra's way is the simple way: find shortest path from the start
    # station to all others, then traverse in reverse from end station
    prev = findShortestRoutesFromStation(workingGraph, start)

    # Ill-formed query: end station is not reachable from start station
    if end not in prev:
        return None

    route = list()
    u = end
    while u in prev:
        route.insert(0, u)
        u = prev[u]

    # We should've arrived at the starting node
    assert u == start
    route.insert(0, start)

    return route

def findShortestRoute(
        metro: Network,
        start: str,
        end: str,
        colorStr: str = None) -> list:
    startStation = metro.findStation(start)
    endStation = metro.findStation(end)
    color = colorFromStr(colorStr)

    assert startStation is not None
    assert endStation is not None

    return findShortestRouteImpl(
            metro.stations, startStation, endStation, color)
