class Solution:
    def cloneTree(self, root):
        
        self.store = {}
        queue = [root]
        
        # Form the initial tree without random pointers
        while len(queue) > 0 :
            old_node = queue.pop()
            if old_node in self.store :
                new_node = self.store[old_node]
            else :
                new_node = Node(old_node.data)
                self.store[old_node] = new_node
            
            if old_node.left :
                old_left = old_node.left
                if old_left in self.store :
                    new_left = self.store[old_left]
                else :
                    new_left = Node(old_left.data)
                    self.store[old_left] = new_left
                new_node.left = new_left
                queue.append(old_left)
            
            if old_node.right :
                old_right = old_node.right
                if old_right in self.store :
                    new_right = self.store[old_right]
                else :
                    new_right = Node(old_right.data)
                    self.store[old_right] = new_right
                new_node.right = new_right
                queue.append(old_right)
        
        # Add all the random pointers
        queue = [root]
        while len(queue) > 0 :
            old_node = queue.pop(0)
            new_node = self.store[old_node]
            if old_node.random is not None :
                if old_node.random in self.store :
                    new_rnd = self.store[old_node.random]
                else :
                    new_rnd = Node(old_node.random.data)
                    self.store[old_node.random] = new_rnd
                new_node.random = new_rnd
            
            if old_node.left :
                queue.append(old_node.left)
            if old_node.right :
                queue.append(old_node.right)
        
        return self.store[root]
        




     
        
        
class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.random=None

    def __str__(self):
        return str(self.data)

def printInord(a,b):
    if (not a and not b):
        return 1
        
    if(a and b) :
        t=int((a.data==b.data) and printInord(a.left,b.left) and printInord(a.right,b.right))
        
        if(a.random and b.random) :
            return int(t and a.random.data==b.random.data)
            
        if (a.random==b.random) :
            return t
            
        return 0
    #if a.random.data==b.random.data and printInord(a.left,b.left) and printInord(a.right,b.right):
        #return 1
    return 0


if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        map=dict()

        n=int(input())
        arrnode=[x for x in input().split()]

        root=None
        i=0
        while i<3*n:

            n1,n2,lr=int(arrnode[i]),int(arrnode[i+1]),arrnode[i+2]

            if n1 in map:
                parent=map[n1]
            else:
                parent = Node(n1)
                map[n1] = parent

                if not root:
                    root = parent


            child=Node(n2)
            map[n2]=child

            if lr=='R':
                parent.right=child

            elif lr=='L':
                parent.left=child

            else:
                parent.random=map[n2]


            i+=3

        ansTree=Solution().cloneTree(root)

        if ansTree==root:
            print(0)
        else:
            print(printInord(root,ansTree))
