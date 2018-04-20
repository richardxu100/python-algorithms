from Node import Node

class LinkedList(object):

    def __init__(self):
        self.count = 0
        self.head = None

    # O(N)
    def traverseList(self):
        if self.head:
            currentNode = self.head
            while currentNode is not None:
                print("Node: %d" % currentNode.data)
                currentNode = currentNode.nextNode

        # O(1)
    def insertStart(self, data):
        newNode = Node(data)
        newNode.nextNode = self.head
        self.head = newNode
        self.count += 1

    # O(1)
    def size(self):
        return self.count

    # O(N)
    def insertEnd(self, data):
        if not self.head:
            self.insertStart(data)
        else:
            currentNode = self.head
            newNode = Node(data)
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
            currentNode.nextNode = newNode
            self.count += 1

    # O(N), if head O(1)
    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.nextNode
        else:
            currentNode = self.head
            while currentNode.nextNode and currentNode.nextNode.data != data:
                currentNode = currentNode.nextNode
            if currentNode.nextNode and currentNode.nextNode.data == data:
                deletedNode = currentNode.nextNode
                currentNode.nextNode = deletedNode.nextNode 
                deletedNode.remove(deletedNode.data)
                self.count -= 1
            else:
                print("That value couldn't be found in the Linked List!")