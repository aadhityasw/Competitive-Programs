class Solution:
	# @param A : tuple of integers
	# @return an integer
    def trap(self, A):

        stack = []
        n = len(A)
        count = 0

        i = 0
        while i < n and A[i] == 0 :
            i += 1
        
        while i < n :
            val = A[i]
            i += 1
            while i < n and A[i] <= val :
                stack.append(A[i])
                i += 1
            
            if i < n :
                val = min(val, A[i])
                while len(stack) > 0 :
                    count += (val - stack.pop())
                
                stack.append(A[i])

        if len(stack) > 0 :
            val = stack.pop()
            while len(stack) > 0 :
                if stack[-1] > val :
                    val = stack.pop()
                else :
                    count += (val -  stack.pop())
        
        return count
