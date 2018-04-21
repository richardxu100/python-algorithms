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
    
    def remove(self, data):
        # empty tree
        if not self.rootNode:
            print("Can't delete from an empty tree!")
            return 

		# data is in root node
        elif self.rootNode.data == data:
            if not self.rootNode.leftChild and not self.rootNode.rightChild:
                self.rootNode = None
                self.size -= 1
            elif self.rootNode.leftChild and not self.rootNode.rightChild:
                self.rootNode = self.rootNode.leftChild
                self.size -= 1
            elif self.rootNode.rightChild and not self.rootNode.leftChild:
                self.rootNode = self.rootNode.rightChild
                self.size -= 1
            else: # has left and right child, will replace with rightmost left child
                delNodeParent = self.rootNode.leftChild
                if not delNodeParent.rightChild:
                    self.rootNode.data = delNodeParent.data
                    if delNodeParent.leftChild:
                        self.rootNode.leftChild = delNodeParent.leftChild   
                    else:
                        self.rootNode.leftChild = None # Remove the old delNode reference
                    self.size -= 1    
                while delNodeParent.rightChild:
                    if delNodeParent.rightChild.rightChild:                
                        delNodeParent = delNodeParent.rightChild
                    else:
                        self.rootNode.data = delNodeParent.rightChild.data 
                        if delNodeParent.rightChild.leftChild:
                            delNodeParent.rightChild = delNodeParent.rightChild.leftChild
                        else: # when there are no leftChilds
                            delNodeParent.rightChild = None
                        self.size -= 1
            return True
                
		delNodeParent = None
		delNode = self.root

		# # find node to remove
		while delNode and delNode.data != data:
            delNodeParent = delNode
            if data < delNode.data:
                delNode = delNode.leftChild
            elif data > delNode.data:
                delNode = delNode.rightChild

		# # case 1: data not found
		if not delNode:
            return print("The data isn't in the binary search tree!")

		# # case 2: remove-node has no children
		elif not delNode.leftChild and not delNode.rightChild:
            if data < delNodeParent.data:
                delNodeParent.leftChild = None 
            else:
                delNodeParent.rightChild = None 
            self.size -= 1

		# # case 3: remove-node has left child only
		elif not delNode.rightChild and delNode.leftChild:
            if data < delNodeParent.data: # think about this
                delNodeParent.leftChild = delNode.leftChild
            else:
                delNodeParent.rightChild = delNode.leftChild
            self.size -= 1

		# # case 4: remove-node has right child only
		elif delNode.rightChild and not delNode.leftChild:
            if data < delNodeParent.data:
                delNodeParent.leftChild = delNode.rightChild
            else:
                delNodeParent.rightChild = delNode.rightChild
            self.size -= 1
            
		# # case 5: remove-node has left and right children
        else:
            delNodeParent = self.rootNode.leftChild
            if not delNodeParent.rightChild:
                self.rootNode.data = delNodeParent.data
                if delNodeParent.leftChild:
                    self.rootNode.leftChild = delNodeParent.leftChild
                else:
                    self.rootNode.leftChild = None  # Remove the old delNode reference
                self.size -= 1
            while delNodeParent.rightChild:
                if delNodeParent.rightChild.rightChild:
                    delNodeParent = delNodeParent.rightChild
                else:
                    self.rootNode.data = delNodeParent.rightChild.data
                    if delNodeParent.rightChild.leftChild:
                        delNodeParent.rightChild = delNodeParent.rightChild.leftChild
                    else:  # when there are no leftChilds
                        delNodeParent.rightChild = None
                    self.size -= 1
		# # else:
		# 	delNodeParent = node
		# 	delNode = node.rightChild
		# 	while delNode.leftChild:
		# 		delNodeParent = delNode
		# 		delNode = delNode.leftChild

		# 	node.value = delNode.value
		# 	if delNode.rightChild:
		# 		if delNodeParent.value > delNode.value:
		# 			delNodeParent.leftChild = delNode.rightChild
		# 		elif delNodeParent.value < delNode.value:
		# 			delNodeParent.rightChild = delNode.rightChild
		# 	else:
		# 		if delNode.value < delNodeParent.value:
		# 			delNodeParent.leftChild = None
		# 		else:
		# 			delNodeParent.rightChild = None



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
        self.__traverse(self.rootNode)
    

    def __traverse(self, currentNode): # a private method
        if self.size == 0:
            return print("Can't traverse an empty BST.")
        if currentNode.leftChild:
            self.__traverse(currentNode.leftChild) # can't return this recursive method, because then nothing afterward runs
        
        print(currentNode.data)

        if currentNode.rightChild:
            self.__traverse(currentNode.rightChild)


        
