import math

class Solution:
	# @param A : integer
	# @return an integer
    def isPalindrome(self, A):
        if A < 0 :
            return 0
        elif A < 10 :
            return 1

        n = int(math.log10(A))
        i = 0
        while i < n // 2 + n%2 :
            if ((A % (10 ** (i+1))) // (10 ** i)) != ((A // (10 ** (n-i))) % 10) :
                return 0
            i += 1
        
        return 1
