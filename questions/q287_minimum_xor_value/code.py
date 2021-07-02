class Solution:
	# @param A : list of integers
	# @return an integer
    def findMinXor(self, A):
        n = len(A)
        A.sort()
        
        min_val = float("inf")
        for i in range(n-1) :
            min_val = min(min_val, A[i]^A[i+1])
        
        return min_val
    