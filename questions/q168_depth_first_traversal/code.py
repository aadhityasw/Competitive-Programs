# This is an Undirected Graph

class Solution:

    def recursiveDFS(self, visited, adj, u) :
        if u not in visited :
            visited.append(u)

            for v in adj[u] :
                self.recursiveDFS(visited, adj, v)

    def dfsOfGraph(self, V, adj):
        visited = []
        self.recursiveDFS(visited, adj, 0)
        return visited


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
