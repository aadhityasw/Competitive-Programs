class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        n = len(A)
        if n<3:
            return 0
        rightspval = [0]*n
        leftspval = [0]*n
        stack = []
        
        stack.append(0)
        for i in range(1,n):
            while stack and A[stack[-1]] < A[i]:
                rightspval[stack.pop()] = i
            stack.append(i)
        stack.clear()
        
        stack.append(n-1)
        for i in range(n-1,-1,-1):
            while stack and A[stack[-1]] < A[i]:
                leftspval[stack.pop()] = i
            stack.append(i)
        del(stack)
        
        maxi = -1
        for i in range(n):
            maxi = max(maxi, leftspval[i]*rightspval[i])
        return maxi%1000000007
