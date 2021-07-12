class Solution:
	# @param A : string
	# @return an integer
    def anytwo(self, A):

        n = len(A)
        if n <= 1 :
            return 0
        
        table = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n+1) :
            for j in range(1, n+1) :
                if A[i-1] == A[j-1] and i != j :
                    table[i][j] = 1 + table[i-1][j-1]
                elif i != j :
                    table[i][j] = max(table[i-1][j], table[i][j-1])
                if table[i][j] > 1 :
                    return 1
        return 0
