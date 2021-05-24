class Solution:
    
    def recursiveTraverse(self, root, n1, n2) :

        if root is None :
            return (None, (False, False))

        ans = [False, False]

        if root.data == n1 :
            ans[0] = True
        if root.data == n2 :
            ans[1] = True
        
        l = self.recursiveTraverse(root.left, n1, n2)
        if l[1][0] and l[1][1] :
            return l

        r = self.recursiveTraverse(root.right, n1, n2)
        if r[1][0] and r[1][1] :
            return r

        ans[0] = ans[0] or l[1][0] or r[1][0]
        ans[1] = ans[1] or l[1][1] or r[1][1]
        
        if ans[0] and ans[1] :
            return (root, ans)
        else :
            return (None, ans)


    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        
        return self.recursiveTraverse(root, n1, n2)[0]
        
        





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
        a,b=list(map(int,input().split()))
        s=input()
        root=buildTree(s)
        k=Solution().lca(root,a,b)
        print(k.data)
