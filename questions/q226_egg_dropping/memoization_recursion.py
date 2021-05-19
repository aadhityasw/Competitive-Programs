"""
This code follows an approach similar to the one in recursion, but adds a DP based Memoization table to reduce run-time.
"""


class Solution:

    def __init__(self):
        self.table = None
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        
        if self.table is None :
            self.table = [[float("inf") for _ in range(k+1)] for _ in range(n+1)]
        
        if k <= 1 or n == 1 :
            return k
        
        if self.table[n][k] != float("inf") :
            return self.table[n][k]

        # Go on for each floor and check for what happens if the egg did or did not brake in that floor
        for i in range(1, k+1) :
            cur_droppings = max(
                self.eggDrop(n-1, i-1), # Check less than current index, if the egg breaks
                self.eggDrop(n, k-i)  # Check above, if the egg does not break
            ) + 1

            self.table[n][k] = min(self.table[n][k], cur_droppings)
        
        return self.table[n][k]


import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
