"""
dp[M][K] means that, given K eggs and M moves,
what is the maximum number of floor that we can check.

The dp equation is:
dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1,
which means we take 1 move to a floor,
if egg breaks, then we can check dp[m - 1][k - 1] floors.
if egg doesn't breaks, then we can check dp[m - 1][k] floors.
"""



class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):

        # Each element is the number of floors which can be covered given `i` eggs <= table[i]
        table = [0] * (n+1)
        
        i = 0
        # While we have not yet reached the required floor's reach, we continue
        while table[n] < k :
            # We find the new reach if we can take another step
            for j in range(n, 0, -1) :
                table[j] += table[j-1] + 1
            i += 1
        
        return i



import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
