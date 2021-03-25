import math

class Solution:
    def numberOfPaths (self, n, m):
        return int(math.factorial(m+n-2) / (math.factorial(m-1) * math.factorial(n-1)))



        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        m, n = map(int, input().split())
        ans = ob.numberOfPaths(m, n)
        print(ans)
