# Geeks for Geeks

class Solution:
    def minCoins(self, coins, M, V):

        table = [[-1 for _ in range(V+1)] for _ in range(M+1)]

        for i in range(M+1) :
            table[i][0] = 0
        
        for i in range(1, M+1) :
            for j in range(1, V+1) :
                # If we have already satisfied the change value in the coins[0...i-2] range of change values
                v1 = table[i-1][j]
                if v1 >= 0 :
                    table[i][j] = v1
                
                # We include this coins[i-1] and check if we can find change for the value (j - coins[i-1]) using the coins[0...i] only, note : this is the difference in unbounded knapsack
                # We take the minimum of these two options if both are possible to get the minimum number of coins needed
                if coins[i-1] <= j :
                    v2 = table[i][j - coins[i-1]]
                    if v2 >= 0 :
                        if table[i][j] >= 0 :
                            table[i][j] = min(table[i][j], (1 + v2))
                        else :
                            table[i][j] = 1 + v2

        return table[M][V]



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        v,m = input().split()
        v,m = int(v), int(m)
        coins = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minCoins(coins,m,v)
        print(ans)
