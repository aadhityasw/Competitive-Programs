def serialize(root, A):
    
    queue = [root]
    
    while len(queue) > 0 :
        
        ptr = queue.pop(0)
        
        if ptr is None :
            A.append(-1)
            continue
        A.append(ptr.data)
        
        queue.append(ptr.left)
        queue.append(ptr.right)
    
    
def deSerialize(A):
    d = A.pop(0)
    root = Node(d)
    queue = [root]
    
    while len(A) > 0 :
        
        ptr = queue.pop(0)
        
        d = A.pop(0)
        if d > 0 :
            ptr2 = Node(d)
            queue.append(ptr2)
        else :
            ptr2 = None
        ptr.left = ptr2
        
        if len(A) == 0 :
            break
        
        d = A.pop(0)
        if d > 0 :
            ptr3 = Node(d)
            queue.append(ptr3)
        else :
            ptr3 = None
        ptr.right = ptr3
    
    return root
    


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
    

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def _deleteTree(node): 
    if (node == None): 
        return
  
    # first delete both subtrees  
    _deleteTree(node.left) 
    _deleteTree(node.right) 
    node.left=None
    node.right=None
    # then delete the node  
     
    
      
# Deletes a tree and sets the root as NULL 
def deleteTree(node_ref): 
    _deleteTree(node_ref) 
    node_ref = None
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        root=buildTree(input())
        A=[]
        serialize(root, A)
        deleteTree(root)
        root = None
        r=deSerialize(A)
        inorder(r)
        print()
