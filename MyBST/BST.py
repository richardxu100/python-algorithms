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
    
    # Will delete the leftmostRight child
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
                delNodeParent = self.rootNode.leftChild # leftMostRightChild
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
                
                
            


		# parent = None
		# node = self.root

		# # find node to remove
		# while node and node.value != data:
		# 	parent = node
		# 	if data < node.value:
		# 		node = node.leftChild
		# 	elif data > node.value:
		# 		node = node.rightChild

		# # case 1: data not found
		# if node is None or node.value != data:

		# # case 2: remove-node has no children
		# elif node.leftChild is None and node.rightChild is None:

		# # case 3: remove-node has left child only
		# elif node.leftChild and node.rightChild is None:

		# # case 4: remove-node has right child only
		# elif node.leftChild is None and node.rightChild:

		# # case 5: remove-node has left and right children
		# else:
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
        self.traverse(self.rootNode)
    

    def traverse(self, currentNode):
        if self.size == 0:
            return print("Can't traverse an empty BST.")
        if currentNode.leftChild:
            self.traverse(currentNode.leftChild) # can't return this recursive method, because then nothing afterward runs
        
        print(currentNode.data)

        if currentNode.rightChild:
            self.traverse(currentNode.rightChild)


        
