"""
This code uses a Memoization approach with a DP table of 1 dimension
The table[n] is our required value after n iterations
At an iteration `i`, the values in table are the values of table[i] of the previous approach
"""


#Function to find the maximum possible amount of money we can win.
def optimalStrategyOfGame(arr, N):
    board = [None for _ in range(N)]
    
    for i in range(N-1, -1, -1) :
        board[i] = (arr[i], 0)
        for j in range(i+1, N) :
            if board[j-1][1] + arr[j] < board[j][1] + arr[i] :
                board[j] = (
                    board[j][1] + arr[i],
                    board[j][0]
                )
            else :
                board[j] = (
                    board[j-1][1] + arr[j],
                    board[j-1][0]
                )
    
    return board[N-1][0]


import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        print(optimalStrategyOfGame(arr,n))
