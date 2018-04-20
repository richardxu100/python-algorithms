from Node import Node

class BST(object):
    def __init__(self):
        self.rootNode = None 
        self.size = 0


    def insert(self, data):
        if not self.rootNode:
            self.rootNode = Node(data)
        else: 
            self.insertNode(self.rootNode, data)
        self.size += 1
                
    
    def insertNode(self, currentNode, data):
        if data <= currentNode.data:
            if not currentNode.leftChild:
                currentNode.leftChild = Node(data)
            else:
                self.insertNode(currentNode.leftChild, data)
        else:
            if not currentNode.rightChild:
                currentNode.rightChild = Node(data)
            else:
                self.insertNode(currentNode.rightChild, data)


    def getSize(self):
        return self.size


    def getRoot(self):
        return self.rootNode
    
    # def remove(self, dataToRemove):

    def getMax(self):
        currentNode = self.rootNode
        while currentNode.rightChild:
            currentNode = currentNode.rightChild
        return currentNode.data

    
    def getMin(self):
        currentNode = self.rootNode
        while currentNode.leftChild:
            currentNode = currentNode.leftChild
        return currentNode.data


    def traverseInOrder(self):
        self.traverse(self.rootNode)
    

    def traverse(self, currentNode):
        if currentNode.leftChild:
            self.traverse(currentNode.leftChild) # can't return this recursive method, because then nothing afterward runs
        
        print(currentNode.data)

        if currentNode.rightChild:
            self.traverse(currentNode.rightChild)

        # if self.leftChild:
        #     return self.traverseInOrder(self.leftChild)
        
        # print(self.data)

        # if self.rightChild:
        #     return self.traverseInOrder(self.rightChild)

        
