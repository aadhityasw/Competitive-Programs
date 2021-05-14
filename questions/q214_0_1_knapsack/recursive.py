"""
We use a Top - Down approach by using a DP table along with the standard recursive approach.
"""


class Solution:

    def __init__(self):
        self.table = None
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):

        # Initialize the table of it has not yet been done
        if self.table is None :
            self.table = [[-1 for _ in range(W + 1)] for _ in range(n)]
        
        # Base condition, if no other element left to add into sack, return 0
        if n == 0 :
            return 0
        
        # If the value has not already been found, then find it
        if self.table[n-1][W] == -1 :
            if wt[n-1] > W :
                # If we cannot fill the current item into the sack
                self.table[n-1][W] = self.knapSack(W, wt, val, n-1)
            else :
                # If the current item can be filled into the sack, we have two options either
                #       Put the item into the sack, or
                #       Not Put the item into the sack
                self.table[n-1][W] = max(
                    val[n-1] + self.knapSack((W - wt[n-1]), wt, val, n-1),
                    self.knapSack(W, wt, val, n-1)
                )
        
        # Return the value at this stage (of W, and n)
        return self.table[n-1][W]





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
