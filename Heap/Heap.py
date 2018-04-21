class Heap(object):
    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0] * HEAP_SIZE
        self.currentPosition = -1


    def insert(self, item):
        if self.isFull():
            return print("Heap is full...")
        else:
            self.currentPosition += 1
            self.heap[self.currentPosition] = item 
            self.heapifyUp(self.currentPosition)
    

    def heapifyUp(self, index):
        parentIndex = int((index-1) / 2)
        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp 
            index = parentIndex
            parentIndex = int((index-1)/2)


    def pop(self):
        result = self.heap[0]
        self.currentPosition = self.currentPosition - 1
        self.heap[0] = self.heap[self.currentPosition]
        del self.heap[self.currentPosition+1]
        self.heapifyDown(0, -1)
        return result


    def isFull(self):
        return self.currentPosition == Heap.HEAP_SIZE:
        
            