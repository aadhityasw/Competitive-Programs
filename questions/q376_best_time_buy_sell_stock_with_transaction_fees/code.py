class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        # Initialize the sold and hold variables
        # Stores the current cash we have
        sold = 0
        # Stores the current cash we have after buying, but not selling a stock
        hold = -prices[0]
        
        # Find the maximum cash that we can get
        n = len(prices)
        for i in range(1, n) :
            sold = max(sold, hold + prices[i] - fee)
            hold = max(hold, sold - prices[i])
        
        return sold
