from Node import Node 

class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.counter = 0

    # O(N)
    def traverseList(self):
        currentNode = self.head 

        while currentNode is not None:
            print("%d" % currentNode.data)
            currentNode = currentNode.nextNode

    # O(1)
    def insertStart(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head 
            self.head = newNode
        self.counter += 1

    # O(1)
    def size(self):
        return self.counter

    # O(N)
    def insertEnd(self, data):
        if self.head is None:
            return self.insertStart(data)

        newNode = Node(data)
        current = self.head 

        while current.nextNode is not None:
            current = current.nextNode

        current.nextNode = newNode 
        self.counter += 1
    
    # O(N), if head O(1)
    def remove(self, data):
        if self.head: # head isn't None, populated
            if data == self.head.data:
                self.head = self.head.nextNode 
            else:
                self.head.remove(data, self.head)
            self.counter -= 1
