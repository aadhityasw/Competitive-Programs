
class Solution:
    def getCount(self, N):
        
        # Initialize the count, and the number of terms in the window
        count = 0
        L = 1
        
        while ((L * (L + 1) / 2) < N) :
            a = ((1.0 * N) - (L * (L + 1) / 2)) / (L + 1)
            if a == int(a) :
                count += 1
            L += 1
        
        return count





if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.getCount(N))
