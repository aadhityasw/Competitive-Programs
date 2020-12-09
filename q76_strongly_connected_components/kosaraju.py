from collections import defaultdict


def DFS(adj, vertex, visited, stack) :
    if visited[vertex] :
        return
    visited[vertex] = True
    for i in adj[vertex] :
        if not visited[i] :
            DFS(adj, i, visited, stack)
    stack.append(vertex)


def reverse_graph(adj, V) :
    opp_graph = {}
    for u in adj :
        if u not in opp_graph :
            opp_graph[u] = []
        for v in adj[u] :
            if v in opp_graph :
                opp_graph[v].append(u)
            else :
                opp_graph[v] = [u]
    return opp_graph


def DFS2(adj, vertex, visited) :
    visited[vertex] = True
    for v in adj[vertex] :
        if not visited[v] :
            DFS2(adj, v, visited)


def countSCCs (adj, V):
    visited = [False for i in range(V)]
    stack = []
    for i in range(V) :
        DFS(adj, i, visited, stack)

    reversed_adj = reverse_graph(adj, V)

    visited = [False for i in range(V)]
    num_SCC = 0
    while len(stack) > 0 :
        vertex = stack[-1]
        stack = stack[:-1]
        if not visited[vertex] :
            DFS2(reversed_adj, vertex, visited)
            num_SCC += 1
    
    return num_SCC


def creategraph(n, arr, graph) :
    i = 0
    while i < 2 * e :
        graph[arr[i]].append(arr[i+1])
        i += 2


t = int(input())
for i in range(t):
    n,e = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    graph = defaultdict(list)
    creategraph(e, arr, graph)
    print (countSCCs(graph, n))
