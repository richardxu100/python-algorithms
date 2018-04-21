from Node import Node 

class Graph(object):
    
    def __init__(self):
        self.adjacencyList = []

   
    def addNode(self, name, neighbors):
        if name in self.adjacencyList:
            print("This node is already in the Graph!")
        else:
            newNode = Node(name)
            newNode.neighbors = neighbors
            self.adjacencyList.append(newNode)


    def dfs(self):
        [print(node.name) for node in self.adjacencyList]
        startingNodeName = input("Node to start on: ")
        startingNode = next(node for node in self.adjacencyList if node.name == startingNodeName)
        self.search(startingNode)
        # print(startingNode)


    def search(self, node):
        print("Node name: %s" % node.name)
        print("Node neighbors: %s" % node.neighbors)
        # node.visited = True
        # print("%s ->" % node.name)

        # for node in node.neighbors:
        #     if not node.visited:
        #         self.search(node)
