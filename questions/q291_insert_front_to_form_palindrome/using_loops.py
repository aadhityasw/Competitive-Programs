class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if len(A) <= 1:
            return 0
        i, j, j_start = 0, len(A)-1, len(A)-1
        while i < j:
            if A[i] == A[j]:
                i += 1
                j -= 1
            else:
                j = j_start - 1
                j_start = j
                i = 0
        return len(A) - 1 - j_start
