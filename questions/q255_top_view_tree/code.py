class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


views = {}

def traverse(node, x, y) :
    global views

    if node is None :
        return

    if x in views :
        if views[x][1] > y :
            views[x] = (node.info, y)
    else :
        views[x] = (node.info, y)
    
    traverse(node.left, x-1, y+1)
    traverse(node.right, x+1, y+1)


def topView(root):
    global views

    traverse(root, 0, 0)

    for k in range(min(views.keys()), max(views.keys())+1) :
        print(views[k][0], end=" ")



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
