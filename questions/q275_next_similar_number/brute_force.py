class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        n = len(A)

        pos = None
        i = n-1
        while i >= 0 :
            j = i-1
            while j >= 0 :
                if A[i] > A[j] :
                    if pos is None :
                        pos = (i, j)
                    elif pos[1] < j :
                        pos = (i, j)
                j -= 1
            i -= 1
        
        if pos is None :
            return "-1"
        
        i, j = pos

        remaining = ""
        freq = [0]*10
        for ch in A[j:i]+A[i+1:] :
            freq[ord(ch)-48] += 1
        for k in range(10) :
            remaining += (chr(k+48))*freq[k]
        
        ans = A[:j] + A[i] + remaining
        return ans
