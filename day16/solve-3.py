import networkx as nx
from joblib import Parallel, delayed
import networkx as nx
import matplotlib.pyplot as plt

tunnel_map = {"AA": {"flow_rate": 0, "routs": ["DD", "II", "BB"]}}
tunnel_map = {}
f = open("tiny.txt")
for line in f.readlines():
    specs = line.strip().split(";")
    valve_spec = specs[0].split()
    rout_detail = specs[1]

    valve_name = valve_spec[1]
    tunnel_map[valve_name] = {}

    flow_rate = int(valve_spec[4].split("=")[1])
    tunnel_map[valve_name]["flow_rate"] = flow_rate

    _routes = rout_detail.split()[4:]
    routes = []
    for route in _routes:
        route = route.strip(", ")
        routes.append(route)

    tunnel_map[valve_name]["routes"] = routes


def calc_pressure_release(open_valves, tunnel_map):
    release = 0
    for valve in open_valves:
        release += tunnel_map[valve]["flow_rate"]
    return release


G = nx.Graph()
for node, data in tunnel_map.items():
    if tunnel_map[node]["flow_rate"] > 0:
        G.add_edge(node, node)
    for node2 in data["routes"]:
        G.add_edge(node, node2)


def findPaths2(G, u, n):
    if n == 0:
        return [[u]]
    paths = [
        [u] + path
        for neighbor in G.neighbors(u)
        for path in findPaths2(G, neighbor, n - 1)
        if u not in path
    ]
    return paths


def findPaths(G, u, n, excludeSet=None):
    if excludeSet == None:
        excludeSet = set([u])
    else:
        excludeSet.add(u)
    if n == 0:
        return [[u]]
    paths = [
        [u] + path
        for neighbor in G.neighbors(u)
        if neighbor not in excludeSet
        for path in findPaths(G, neighbor, n - 1, excludeSet)
    ]
    excludeSet.remove(u)
    return paths


options = findPaths(G, "AA", 7)

n = G.neighbors("BB")
for i in options:
    print(i)
