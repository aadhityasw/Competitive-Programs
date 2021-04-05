class Solution :

    def recursiveDetect(self, visited, u, adj) :

        for v in adj[u] :
            if len(visited) > 1 and v == visited[-2] :
                continue
            
            if v in visited :
                return True

            if self.recursiveDetect(visited+[v], v, adj) :
                return True
        
        return False

    def isCycle(self, V, adj):

        for i in range(V) :
            if self.recursiveDetect([i], i, adj) :
                return 1
        
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
        
        if ob.isCycle(V, adj):
            print(1)
        else:
            print(0)
