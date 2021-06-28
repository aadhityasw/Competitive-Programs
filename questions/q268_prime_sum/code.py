class Solution:

    def isPrime(self, num) :

        for i in range(2, int(num**0.5)+1) :
            if num % i == 0 :
                return False
        return True


	# @param A : integer
	# @return a list of integers
    def primesum(self, A):

        # Loop through half way and find the smallest prime that meets the crieteria
        for i in range(2, A//2+1) :
            if self.isPrime(i) and self.isPrime(A-i) :
                return (i, A-i)
