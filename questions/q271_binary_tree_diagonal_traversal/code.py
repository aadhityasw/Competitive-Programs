
def calcDiagonalIndex(position) :
    """
    Given the position of the node, returns the index of the diagonal it belongs to.
    """

    # Calculate the index
    diag_index = (position[1] -  position[0]) // 2

    # Return the index
    return diag_index


def traverse(root, position, diagonals) :
    """
    Given the root and its position, we traverse through its children adding them to the appropriate diagonal.
    """

    # Calculate the diagonal it belongs to
    diag_index = calcDiagonalIndex(position)

    # Insert this value into the appropriate diagonal
    if diag_index in diagonals :
        diagonals[diag_index].append(root.data)
    else :
        diagonals[diag_index] = [root.data]
    
    # Destructure the position
    x, y = position

    # Traverse to its children
    if root.left :
        traverse(root.left, (x-1, y+1), diagonals)
    if root.right :
        traverse(root.right, (x+1, y+1), diagonals)


def diagonal(root):
    #:param root: root of the given tree.
    #return: print out the diagonal traversal,  no need to print new line

    # To store all the diagonals seperately
    diagonals = {}

    # Traverse the tree and save the values in the appropriate diagonals array
    traverse(root, (0, 0), diagonals)

    # Initialize an array to store the complete diagonals list
    answer = []

    # Loop to each diagonal and form the elements in the required order
    for k in sorted(diagonals.keys()) :
        answer.extend(diagonals[k])
    
    # Return the final array
    return answer






import sys
sys.setrecursionlimit(50000)
#Contributed by Sudarshan Sharma
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
        diagonalNode = diagonal(root)
        for node in diagonalNode:
            print(node,end=' ')
        print()
