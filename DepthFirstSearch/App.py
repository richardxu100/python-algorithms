import DFS
from Graph import Graph

myGraph = Graph()
myGraph.addNode("A", ["B", "C"])
myGraph.addNode("B", ["A"])
myGraph.addNode("C", ["A", "E"])
myGraph.addNode("D", ["B"])
myGraph.addNode("E", ["A"])

myGraph.dfs()

# from Node import Node

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.neighbors.append(node2)
node1.neighbors.append(node3)
node2.neighbors.append(node4)
node4.neighbors.append(node5)

# DFS.dfs(node1)

