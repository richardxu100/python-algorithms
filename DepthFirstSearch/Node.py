class Node(object):
    
    def __init__(self, name):
        self.name = name 
        self.neighbors = []
        self.visited = False 

    