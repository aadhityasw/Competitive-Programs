def isEqual(root1, root2) :
    if root1 is None and root2 is None :
        return True
    
    if root1 and root2 :
        return((root1.data == root2.data) and (isEqual(root1.left, root2.right)) and (isEqual(root1.right, root2.left)))

    return False
    

# return true/false denoting whether the tree is Symmetric or not
def isSymmetric(root):
    if root is None :
        return True
    
    return isEqual(root.left, root.right)
