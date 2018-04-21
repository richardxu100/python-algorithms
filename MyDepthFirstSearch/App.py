import DFS 
from Node import Node

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")

node1.neighbors.append(node2)
node1.neighbors.append(node3)
node3.neighbors.append(node6)
node2.neighbors.append(node4)
node4.neighbors.append(node5)

DFS.dfs(node1)