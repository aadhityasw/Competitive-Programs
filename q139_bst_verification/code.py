def checkLeft(root, val) :
    flag = True
    
    if root.left :
        flag = flag and (root.data > root.left.data)
        if flag :
            flag = flag and checkLeft(root.left, root.data)
    
    if flag and root.right :
        flag = flag and (root.data < root.right.data) and (root.right.data < val)
        if flag :
            flag = flag and checkRight(root.right, root.data)
    
    return flag


def checkRight(root, val) :
    flag = True
    
    if root.left :
        flag = flag and (root.data > root.left.data) and (root.left.data > val)
        if flag :
            flag = flag and checkLeft(root.left, root.data)
    
    if flag and root.right :
        flag = flag and (root.data < root.right.data)
        if flag :
            flag = flag and checkRight(root.right, root.data)
    
    return flag
    

# return True if the given tree is a BST, else return False
def isBST(root):
    flag = True
    
    if root.right :
        flag = flag and root.data < root.right.data
        if flag :
            flag = flag and checkRight(root.right, root.data)
    
    if flag and root.left :
        flag = flag and root.data > root.left.data
        if flag :
            flag = flag and checkLeft(root.left, root.data)
    
    return flag



from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        if isBST(root):
            print(1) 
        else:
            print(0)
