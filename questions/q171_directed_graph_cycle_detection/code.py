class Solution :

    def recursiveDetect(self, path, u, adj) :
        
        self.visited[u] = True
        path[u] = True

        for v in adj[u] :
            
            if self.visited[v] :
                if path[v] :
                    return True
                continue

            if self.recursiveDetect(path, v, adj) :
                return True
        
        path[u] = False
        return False
        

    def isCyclic(self, V, adj):
        self.visited = [False] * V
        path = [False] * V

        for i in range(V) :
            if not self.visited[i] :
                if self.recursiveDetect(path, i, adj) :
                    return 1
                self.visited[i] = True
        
        return 0



import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
