"""
Here, we simplify the DP table to be of just one dimension, and thus save more space.
This approach does essentially the same as the last code, but in just a shorter time.

Here we analysed that for each subset of the coins (i - loop) all the iterations prior to the (j < S[i]) condition is waste.
So we run the inner loop from `S[i]` till `n` only.

Here the state of the `table` after `i th` iteration will be equivalent to the `i th` row of the `table` in the previous approach.
"""


class Solution:
    def count(self, S, m, n): 

        # Initialize the DP table
        table = [0 for _ in range(n+1)]
        # Equivalent to initializing the first column to 1's
        table[0] = 1

        for i in range(m) :
            for j in range(S[i], n+1) :
                # When j = S[i] i.e the first iteration, it is equivalent to `table[i][j] = table[i-1][j]`
                # For the remaining iterations of this loop, it is equivalent to `table[i][j] += table[i][j-S[i-1]]`
                table[j] += table[j-S[i]]
            
        # Return the number of options for the whole amount
        return table[n]


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
