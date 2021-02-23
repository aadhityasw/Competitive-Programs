class KthLargest:

    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        for num in nums :
            self.add(num)

    def add(self, val) :
        if len(self.heap) == self.k :
            if self.heap[0] < val :
                self.heap[0] = val
                self.minHeapify(0)
            return self.heap[0]
        self.heap.append(val)
        self.buildMinHeap(self.parent(len(self.heap)-1))
        if len(self.heap) == self.k :
            return self.heap[0]
    
    def parent(self, pos) :
        """ Returns the position of a parent node, given the position of a child. """
        return (pos - 1) // 2
    
    def left(self, pos) :
        """ Returns the position of the left child node, given the position of a parent node. """
        return (pos * 2) + 1
    
    def right(self, pos) :
        """ Returns the position of the right child node, given the position of a parent node. """
        return (pos * 2) + 2

    def buildMinHeap(self, node) :
        """
        Follows a bottom up approach to re-arrange the values of the heap, to reattain its min-heap property.
        It is called everytime a new element has to be inserted into the heap. 
        """
        minpos = node
        if (self.left(node) < len(self.heap)) and (self.heap[minpos] > self.heap[self.left(node)]) :
            minpos = self.left(node)
        if (self.right(node) < len(self.heap)) and (self.heap[minpos] > self.heap[self.right(node)]) :
            minpos = self.right(node)
        if minpos != node :
            self.heap[minpos], self.heap[node] = self.heap[node], self.heap[minpos]
            if node != 0 :
                self.buildMinHeap(self.parent(node))

    def minHeapify(self, node) :
        """
        Follows a top-down approach to re-arrange the values of the heap, to reattain its min-heap property.
        It is called everytime a new element replaces the root element. 
        """
        minpos = node
        if (self.left(node) < len(self.heap)) and (self.heap[minpos] > self.heap[self.left(node)]) :
            minpos = self.left(node)
        if (self.right(node) < len(self.heap)) and (self.heap[minpos] > self.heap[self.right(node)]) :
            minpos = self.right(node)
        if minpos != node :
            self.heap[minpos], self.heap[node] = self.heap[node], self.heap[minpos]
            self.minHeapify(minpos)


T = int(input())
for tes in range(T) :
    k, n = map(int, input().split())
    ob = KthLargest(k, [])
    arr = list(map(int, input().split()))
    for num in arr :
        val = ob.add(num)
        if val is None :
            print(-1, end=' ')
        else :
            print(val, end=' ')
    print()
