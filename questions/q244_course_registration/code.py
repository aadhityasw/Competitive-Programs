class Node :
    def __init__(self, data=0):
        self.data = data
        self.prerequisites = set()


def recurse(i, nodes, visited, stack, path) :
    visited[i] = True

    for nod in nodes[i].prerequisites :
        if nod in path :
            return False
        if not visited[nod-1] :
            ans = recurse(nod-1, nodes, visited, stack, path+[(i+1)])
            if ans is False :
                return False
    
    stack.append((i+1))
    return True


def arrange(n, nodes) :
    stack = []
    visited = [False] * n

    for i in range(n) :
        if not visited[i] :
            if nodes[i] is not None :
                ans = recurse(i, nodes, visited, stack, [])
                if ans is False :
                    return None
            else :
                stack.append(i+1)
    
    return stack

T = int(input())
for _ in range(T) :
    n, m = map(int, input().strip().split())

    nodes = [None] * n

    for i in range(m) :
        src, dest = map(int, input().strip().split())
        if nodes[src-1] is None :
            nodes[src-1] = Node(src)
        if nodes[dest-1] is None :
            nodes[dest-1] = Node(dest)
        nodes[dest-1].prerequisites.add(src)

    ans = arrange(n, nodes)
    if ans is None :
        print("IMPOSSIBLE")
    else :
        print(" ".join([str(i) for i in ans]))
