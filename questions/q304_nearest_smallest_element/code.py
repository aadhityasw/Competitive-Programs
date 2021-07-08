class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):

        n = len(A)
        stack = []
        res = []

        for i in range(n) :
            while len(stack) > 0 and stack[-1] >= A[i] :
                stack.pop()
            if len(stack) > 0 :
                res.append(stack[-1])
            else :
                res.append(-1)
            stack.append(A[i])
        
        return res
