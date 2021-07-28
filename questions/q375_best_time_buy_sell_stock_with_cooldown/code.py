class Solution:
    def maxProfit(self, prices) -> int:
        
        # We define the states
        sold = 0
        hold = float("-inf")
        rest = 0
        
        n = len(prices)
        for i in range(n) :
            prev_sp = sold
            sold = hold + prices[i]
            hold = max(hold, rest - prices[i])
            rest = max(rest, prev_sp)
        
        # We leave out can_sell, because, we cannot exit without completing a transaction
        return max(sold, rest)
