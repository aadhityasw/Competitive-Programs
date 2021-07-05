from collections import Counter

class Solution:

    def countNumOnes(self, num) :
        """
        Given a number returns the number of ones in its binary representation
        """
        return Counter(bin(num))['1']


	# @param A : list of integers
	# @return an integer
    def cntBits(self, A):

        # For sum
        s = 0

        n = len(A)

        for i in range(n) :
            for j in range(i+1, n) :
                s = (s + self.countNumOnes(A[i]^A[j])) % 1000000007
        return (s*2) % 1000000007
