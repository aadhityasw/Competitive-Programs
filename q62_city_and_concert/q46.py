#%%

# Brute Force

class Solution:
    def recursiveTraverse(self, A, path_cost, visited) :
        min_cost = A[visited[-1]-1]
        for d, c in path_cost[visited[-1]] :
            if d not in visited :
                min_cost = min(min_cost, (2*c) + self.recursiveTraverse(A, path_cost, visited+[d]))
        return min_cost
    
    
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        path_cost = {a:[] for a in range(1, n+1)}
        for s, d, c in B :
            path_cost[s].append((d, c))
            path_cost[d].append((s, c))
        min_cost_arr = []
        for i in range(1, n+1) :
            min_cost_arr.append(self.recursiveTraverse(A, path_cost, [i]))
        return min_cost_arr
