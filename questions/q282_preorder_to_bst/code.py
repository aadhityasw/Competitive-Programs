def constructTree(pre, size):
    
    # Initialize a stack
    stack = []

    # Process the first element
    root = Node(pre[0])
    stack.append(root)

    for i in range(1, size) :
        if pre[i] < stack[-1].data :
            ptr = Node(pre[i])
            stack[-1].left = ptr
            stack.append(ptr)
        elif pre[i] > stack[-1].data :
            ptr = stack[-1]
            while len(stack) > 0 and stack[-1].data < pre[i] :
                ptr = stack[-1]
                stack.pop()
            ptr2 = Node(pre[i])
            ptr.right = ptr2
            stack.append(ptr2)
    
    return root


class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data,end=' ')

if __name__ == '__main__':
    t=int(input())

    for _tcs in range(t):
        size=int(input())
        pre=[int(x)for x in input().split()]

        root=constructTree(pre,size)

        postOrd(root)
        print()
