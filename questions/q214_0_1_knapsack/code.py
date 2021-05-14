"""
We will be using a bottom up approach here using Dynamic Programming.
"""


class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):

        # Initialize the table
        self.table = [[0 for _ in range(W + 1)] for _ in range(n+1)]

        # Fill the table
        for i in range(1, n+1) :
            for j in range(1, W+1) :
                if wt[i-1] > j :
                    # If we cannot fill the current item into the sack
                    self.table[i][j] = self.table[i-1][j]
                else :
                    # If the current item can be filled into the sack, we have two options either
                    #       Put the item into the sack, or
                    #       Not Put the item into the sack
                    self.table[i][j] = max(
                        val[i-1] + self.table[i-1][(j-wt[i-1])],
                        self.table[i-1][j]
                    )
        
        # Return the value at stage (W, n)
        return self.table[n][W]


import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
