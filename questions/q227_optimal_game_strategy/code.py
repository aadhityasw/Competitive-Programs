"""
This code uses a Memoization approach with a DP table
The table[0][n] is our required value
table[front][rear] = (player1, player2) where player1 is the best score that they can obtain in the arr[front:rear] subset of arr
"""

#Function to find the maximum possible amount of money we can win.
def optimalStrategyOfGame(arr, n):

    table = [[(0, 0) for _ in range(n)] for _ in range(n)]

    i = n
    while i > 0 :
        for j in range(i) :
            # We fill the r'th row and c'th column in this iteration
            r = j
            c = j + n - i

            if r == c :
                # If we are filling the diagonal elements
                table[r][c] = (arr[r], 0)
            else :
                # All other cases

                # We choose the first number or arr[r] for this option
                option_1 = arr[r] + table[r+1][c][1]
                # We choose the last number or arr[c] for this option
                option_2 = arr[c] + table[r][c-1][1]

                # We fill the table according to the results of these options
                if option_1 >= option_2 :
                    # If taking the first value is favorable, then that value is for player 1
                    # And the player 2 recieves the favorable position for the remaining array
                    table[r][c] = (
                        option_1,
                        table[r+1][c][0]
                    )
                else :
                    # If taking the last value is favorable, then that value is for player 1
                    # And the player 2 recieves the favorable position for the remaining array
                    table[r][c] = (
                        option_2,
                        table[r][c-1][0]
                    )

        # After every iteration of this loop, we fill one less number in the table
        # This is because we fill only the upper diagonal portion of the table matrix
        i -= 1
    
    #for row in table :
    #    print(row)
    
    # Return the score of player 1 for the whole array
    return table[0][n-1][0]


import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        print(optimalStrategyOfGame(arr,n))
