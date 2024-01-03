import networkx as nx
import matplotlib.pyplot as plt


# Defining a Class
class GraphVisualization:
    def __init__(self):

        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.visual = []
        self.node_list = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addNode(self, a):
        self.node_list.append(a)

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()


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

G = GraphVisualization()
for node, data in tunnel_map.items():

    for node2 in data["routes"]:
        G.addEdge(
            node + ": " + str(data["flow_rate"]),
            node2 + ": " + str(tunnel_map[node2]["flow_rate"]),
        )

G.visualize()
