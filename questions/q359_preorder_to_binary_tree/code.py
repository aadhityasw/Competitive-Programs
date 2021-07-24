def constructTree(pre, preLN, n):
    
    stack = []
    
    # Add the first node as the root node
    root = Node(pre[0])
    stack.append(root)
    
    
    i = 1
    while i < n :
        node = Node(pre[i])
        
        while len(stack) > 0 and stack[-1].left and stack[-1].right :
            stack.pop()
        
        if stack[-1].left is None :
            stack[-1].left = node
        else :
            stack[-1].right = node
        
        if preLN[i] == 'N' :
            stack.append(node)
        
        i += 1
    
    return root
    
    
    
    

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.data,end=' ')
    printInorder(root.right)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        pre = list(map(int, input().strip().split()))  # nodes
        preln=list(map(str, input().strip().split()))   # leaf or not
        # construct the tree according to given list
        root=constructTree(pre, preln, n)
        printInorder(root)
        print()
