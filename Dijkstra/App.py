from Vertex import Vertex
from Edge import Edge 
from Algorithm import Algorithm

node1 = Vertex("A")
node2 = Vertex("B")
node3 = Vertex("C")

edge1 = Edge(1, node1, node2)
edge2 = Edge(1, node2, node3)
edge3 = Edge(10, node1, node3)

node1.adjacencyList.append(edge1)
node1.adjacencyList.append(edge2)
node2.adjacencyList.append(edge3)

vertexList = {node1, node2, node3}

algorithm = Algorithm()

algorithm.calculateShortestPath(vertexList, node1)
algorithm.getShortestPathTo(node3)

