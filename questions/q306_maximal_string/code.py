class Solution:

    def __init__(self) :
        self.max_string = None

    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):

        if B <= 0 :
            if self.max_string is None :
                self.max_string = A
            else :
                if A > self.max_string :
                    self.max_string = A
            return self.max_string

        n = len(A)

        for i in range(n) :
            for j in range(i+1, n) :
                if A[j] > A[i] :
                    self.solve(A[:i]+A[j]+A[i+1:j]+A[i]+A[j+1:], B-1)
        
        return self.max_string
