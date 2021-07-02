from bisect import bisect_left
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        p = [1] * (max(A) + 1)
        for i in range(1, len(p)):
            for j in range(i, len(p), i):
                p[j] = (p[j] * i) % 1000000007
        # Find intervals
        stack = []
        l = [-1] * len(A)
        r = [len(A)] * len(A)
        for idx, val in enumerate(A):
            while len(stack):
                stackIdex, stackValue = stack[-1]
                if stackValue < val:
                    r[stackIdex] = idx
                    stack.pop()
                else:
                    l[idx] = stackIdex
                    break
            stack.append((idx, val))
        # Populate G, but don't sort yet
        g = [(p[A[i]], (i - lr[0]) * (lr[1] - i)) for i, lr in enumerate(zip(l, r))]
        # Sort and compress
        length = 0
        G = []
        for p, count in sorted(g, reverse=True):
            length += count
            G += [(length, p)]
        # Do queries
        Q = []
        return [G[bisect_left(G, (q,0))][1] for q in B]
