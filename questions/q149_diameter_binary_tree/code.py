max_diameter = 0

def traverse(root):

    global max_diameter

    if root is None :
        return 0
    
    l = traverse(root.left)
    r = traverse(root.right)

    # We calculate between end nodes and not leaf nodes
    if (l + r + 1) > max_diameter :
        max_diameter = (l + r + 1)

    return max(l, r) + 1


def diameter(root) :

    global max_diameter
    max_diameter = 0

    traverse(root)

    return max_diameter
