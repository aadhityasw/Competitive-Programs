class Solution:

    def __init__(self):
        self.buffer = {}


	# @param A : string
	# @param B : string
	# @return an integer
    def isMatch(self, A, B):

        i, j = len(A)-1, len(B)-1
        if i == j == -1 :
            self.buffer[(i, j)] = True
            return self.buffer[(i, j)]
        elif i == -1 :
            if B[j] == '*' :
                self.isMatch(A, B[:-2])
                self.buffer[(i, j)] = self.buffer[(i, j-2)]
            else :
                self.buffer[(i, j)] = False
            return self.buffer[(i, j)]
        elif j == -1 :
            self.buffer[(i, j)] = False
            return self.buffer[(i, j)]

        if (i, j) in self.buffer :
            return self.buffer[(i, j)]
        
        if A[i] == B[j] or B[j] == '?' :
            self.isMatch(A[:-1], B[:-1])
            self.buffer[(i, j)] = self.buffer[(i-1, j-1)]
        elif B[j] == '*' :
            self.isMatch(A, B[:-2])
            self.buffer[(i, j)] = self.buffer[(i, j-2)]
            if A[i] == B[j-1] or B[j-1] == '.' :
                self.isMatch(A[:-1], B)
                self.buffer[(i, j)] = self.buffer[(i, j)] or self.buffer[(i-1, j)]
        else :
            self.buffer[(i, j)] = False

        return self.buffer[(i, j)]
