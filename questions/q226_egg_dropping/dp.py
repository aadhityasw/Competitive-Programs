"""
This program utilizes a bottom-up DP based approach.
"""


class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):

        if k <= 1 or n == 1 :
            return k

        table = [[float("inf") for _ in range(k+1)] for _ in range(n+1)]

        for i in range(1, n+1) :
            table[i][0] = 0
            table[i][1] = 1

        for i in range(1, k+1) :
            table[1][i] = i
        
        for i in range(2, n+1) :
            for j in range(2, k+1) :
                for l in range(1, j+1) :
                    cur_droppings = max(
                        table[i-1][l-1], # Check less than current index, if the egg breaks
                        table[i][j-l]  # Check above, if the egg does not break
                    ) + 1
                    table[i][j] = min(table[i][j], cur_droppings)
        
        return table[n][k]


import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
