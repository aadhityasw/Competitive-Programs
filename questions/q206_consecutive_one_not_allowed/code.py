class Solution:

    def countStrings(self,n):
        a = 1
        b = 1
        
        for _ in range(n) :
            c = (a + b) % 1000000007
            a, b = b, c
        
        return b




# Driver code 
if __name__ == "__main__":         
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
