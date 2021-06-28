import math

class Solution:

    def hash(self, num) :
        return num % 100

    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        arr = [False] * A
        primes_hash = [[] for _ in range(102)]
        primes = []

        for i in range(2, A) :
            if not arr[i] :
                primes_hash[self.hash(i)].append(i)
                primes.append(i)
                j = 2
                while j*i < A :
                    arr[j*i] = True
                    j += 1
        
        for p in primes :
            if A-p in primes_hash[self.hash(A-p)] :
                return (p, A-p)

A = 184
ob = Solution()
print(ob.primesum(A))
