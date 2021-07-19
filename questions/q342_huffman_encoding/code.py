import heapq


class Node :
    def __init__(self, sym='', frequency = 0):
        self.left = None
        self.right = None
        self.symbol = sym
        self.freq = frequency
        self.huff = ''
    
    def __lt__(self, ob):
        return self.freq < ob.freq
    
    def __eq__(self, ob):
        return self.freq == ob.freq


class Solution:

    def saveEncodedValues(self, root, cur_path='') :

        cur_path += root.huff
        
        if root.left :
            self.saveEncodedValues(root.left, cur_path)
        if root.right :
            self.saveEncodedValues(root.right, cur_path)
        
        if root.left is None and root.right is None :
            self.encoded_values.append(cur_path)


    def huffmanCodes(self,S,f,N):

        # Create nodes and insert them into heap
        self.heap = []
        for sym, freq in zip(S, f) :
            heapq.heappush(self.heap, Node(sym, freq))
        
        # Pop nodes and form the internal nodes
        while len(self.heap) > 1 :
            ob1 = heapq.heappop(self.heap)
            ob2 = heapq.heappop(self.heap)

            internal_node = Node((ob1.symbol + ob2.symbol), (ob1.freq + ob2.freq))
            ob1.huff = '0'
            ob2.huff = '1'
            internal_node.left = ob1
            internal_node.right = ob2
            heapq.heappush(self.heap, internal_node)
        
        # Traverse through preorder and save the huffman values
        self.encoded_values = []
        self.saveEncodedValues(heapq.heappop(self.heap))
        return self.encoded_values








if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S= input()
        N= len(S);
        f= [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.huffmanCodes(S,f,N)
        for i in ans:
            print(i, end = " ")
        print()
