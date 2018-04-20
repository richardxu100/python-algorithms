class Node(object):

    def __init__(self, data):
        self.data = data 
        self.nextNode = None 

    def remove(self, data):
        # if self.data == data:
        # previousNode.nextNode = self.nextNode 
        del self.data 
        del self.nextNode
        # else:
            # remove(data, self)