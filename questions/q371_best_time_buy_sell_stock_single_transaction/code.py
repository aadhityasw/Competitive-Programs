class Solution:
    def maxProfit(self, prices) -> int:
        
        n = len(prices)
        
        # Fill the left array with left min values
        leftMins = [0]*n
        min_val = float("inf")
        for i in range(n) :
            min_val = min(min_val, prices[i])
            leftMins[i] = min_val
        
        # Fill the right array with right max vals
        rightMaxs = [0]*n
        max_val = float("-inf")
        for i in range(n-1, -1, -1) :
            max_val = max(max_val, prices[i])
            rightMaxs[i] = max_val
        
        # Find the overall profit
        max_profit = 0
        for i in range(n) :
            max_profit = max(
                max_profit,
                rightMaxs[i] - leftMins[i]
            )
        
        return max_profit
