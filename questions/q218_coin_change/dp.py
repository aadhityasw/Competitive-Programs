class Solution:
    def count(self, S, m, n): 

        # Initialize the DP table
        table = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # Initialize the first column to 1's
        for i in range(m+1) :
            table[i][0] = 1

        for i in range(1, m+1) :
            for j in range(1, n+1) :
                table[i][j] = table[i-1][j]
                # If the current S[i-1] can be taken from the cost j, we do so and find the chances of the remaining (j - S[i-1]) amount
                if S[i-1] <= j :
                    table[i][j] += table[i][j-S[i-1]]
            
        # Return the number of options for the whole amount
        return table[m][n]


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
