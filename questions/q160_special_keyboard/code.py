#%%

# Version 1
# Not sure if this works for all cases

class Solution_Optimized:

    def optimalKeys(self, n):
        if n < 5 :
            return n
        
        else :
            return max(4*self.optimalKeys(n-5), 3*self.optimalKeys(n-4))



#%%

# Version 2
# Will Work for all cases


class Solution:

    def __init__(self) :
        self.dp = {}

    def optimalKeys(self, n):
        if n < 7 :
            self.dp[n] = n
            return n

        if n in self.dp :
            return self.dp[n]
        
        multiplier = 2
        max_val = 0
        for i in range(n-3, -1, -1) :
            if i not in self.dp :
                self.optimalKeys(i)
            
            max_val = max(max_val, multiplier * self.dp[i])
            multiplier += 1
        
        self.dp[n] = max_val
        return self.dp[n]
