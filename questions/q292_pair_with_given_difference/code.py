from collections import Counter

class Solution:

    def hashFunction(self, n) :
        return n % 1000


    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        if B == 0 :
            freq = Counter(A)
            for v in freq.values() :
                if v > 1 :
                    return 1
            return 0

        table = [[] for _ in range(1001)]
        for num in A :
            table[self.hashFunction(num)].append(num)
        
        for num in A :
            if ((num - B) in table[self.hashFunction(num - B)]) or  ((num + B) in table[self.hashFunction(num + B)]) :
                return 1
        return 0
