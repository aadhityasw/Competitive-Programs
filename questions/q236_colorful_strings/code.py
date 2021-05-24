class Solution:

    def __init__(self):
        self.fact = {}
        self.fact[0] = 1
        self.fact[1] = 1
    
    def calculateFactorial(self, n) :
        """
        Given a number, finds its factorial using recursion and memoization.

        Parameters
        ----------
        n - the number for which factorial is to be found
        """

        if n in self.fact :
            return self.fact[n]
            
        self.fact[n] = n * self.calculateFactorial(n-1)
        
        return self.fact[n]

    def findPermutations(self, n, r, b, g) :
        """
        Given n, r, g, b find the number of ways this can be arranged.

        Parameters
        ----------
        n - total number of colors that needs to be arranged
        r - total number of red colored balls available
        g - total number of green colored balls available
        b - total number of blue colored balls available
        """

        return int(self.calculateFactorial(n) / (self.calculateFactorial(r) * self.calculateFactorial(g) * self.calculateFactorial(b)))


    def possibleStrings(self, n, r, b, g):

        # Initialize the answer to be 0
        total = 0

        # Remaining that we need to distribute
        remaining = n - r - g - b

        # Find the total of all combinations
        for i in range(remaining+1) :
            for j in range(remaining - i+1) :
                total += self.findPermutations(n, r+i, b+j, g+remaining-i-j)

        return total

        

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,r,g,b = input().split()
        n=int(n)
        r=int(r)
        g=int(g)
        b=int(b)
        
        ob = Solution()
        print(ob.possibleStrings(n, r, b, g))
