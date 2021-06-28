class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):

        max_sum = -1 * float("inf")
        elements = []

        n = len(A)

        pos = 0
        while pos < n :
            while pos< n and A[pos] < 0 :
                pos += 1
            
            start = pos
            s = 0
            while pos < n and A[pos] >= 0 :
                s += A[pos]
                pos += 1
            
            if s > max_sum or elements is None :
                max_sum = s
                elements = A[start : pos]
            elif s == max_sum :
                if pos-start+1 > len(elements) :
                    elements = A[start : pos]
                elif pos-start+1 == len(elements) and A[start] < elements[0] :
                    elements = A[start : pos]
        
        return elements
