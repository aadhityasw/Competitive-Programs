class Solution:
    def maxProfit(self, prices) -> int:
        
        profit = 0
        n = len(prices)
        
        i = 0
        while i < n :
            # Find the lowest price to buy
            while i+1 < n and prices[i] > prices[i+1] :
                i += 1
            buy = i
            
            # Find the highest price to sell
            while i+1 < n and prices[i] < prices[i+1] :
                i += 1
            sell = i
            
            # Add the profit of our current transaction
            profit += (prices[sell] - prices[buy])
            i += 1
        
        # Return the overall profit obtained
        return profit
