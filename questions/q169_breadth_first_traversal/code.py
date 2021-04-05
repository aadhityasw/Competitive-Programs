class Solution:

    def bfsOfGraph(self, V, adj):
        visited = []
        queue = [0]

        while len(queue) > 0 :
            u = queue.pop(0)
            if u not in visited :
                visited.append(u)

                for v in adj[u] :
                    queue.append(v)

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
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
