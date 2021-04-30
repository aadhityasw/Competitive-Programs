class Solution:
    
    def recurse(self, node, visited, V, adj) :
        visited[node] = True
        
        for i in adj[node] :
            if not visited[i] :
                self.recurse(i, visited, V, adj)
        
        self.stack.append(node)
    
    
    # Your task is to complete this function
    # Function should return Topologically Sorted List
    # Graph(adj) is a list of List
    # V is no of Vertices
    def topoSort(self, V, adj):
        self.stack = []
        
        visited = [False]*V
        
        for i in range(V) :
            if not visited[i] :
                self.recurse(i, visited, V, adj)
        
        self.stack.reverse()
        #print(self.stack)
        return self.stack



import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
