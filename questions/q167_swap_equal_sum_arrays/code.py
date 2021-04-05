class Solution:
    def findSwapValues(self,a, n, b, m):
        summA = sum(a)
        summB = sum(b)
        diff = (summA - summB)
        if diff % 2 != 0 :
            return -1
        diff = diff / 2

        # We need to find num1 in a and num2 in b such that
        # summA - num1 + num2 = summB - num2 + num1
        # Which brings us to
        # num1 - num2 = (summA - summB) / 2

        i = 0
        j = 0

        while i < n and j < m :
            d = a[i] - b[j]
            if d == diff :
                return 1
            elif d < diff :
                i += 1
            else :
                j += 1

        return -1
