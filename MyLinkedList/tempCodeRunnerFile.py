        newNode = Node(data)
        newNode.nextNode = self.head 
        self.head = newNode
        self.count += 1