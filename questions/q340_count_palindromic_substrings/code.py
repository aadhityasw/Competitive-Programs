class Solution:

    def CountPS(self, S, N):

        self.table = [[-1 for _ in range(N+1)] for _ in range(N+1)]
        
