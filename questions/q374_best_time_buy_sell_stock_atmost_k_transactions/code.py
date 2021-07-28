class Solution:
    def maxProfit(self, k: int, prices) -> int:
        
        if len(prices) < 2 :
            return 0
        
        n = len(prices)
        
        # Initialize the table
        table = [[0 for _ in range(n+1)] for _ in range(k+1)]
        
        # Fill the table values
        for i in range(1, k+1) :
            
            # We compute this as we traverse through the prices list for each day
            min_buy_price = prices[0]
            
            # For each day fill the values of having `i` transactions
            for j in range(1, n) :

                # This is the change from the previous code
                # We compute this as we move forward in the prices array rather than performing repeated computations
                min_buy_price = min(
                    min_buy_price,
                    prices[j] - table[i-1][j-1]
                )
                
                # Choose to whether sell a stock today on buying it on l`th day, or to just not do a transaction on the j`th day
                table[i][j] = max(
                    table[i][j-1],
                    prices[j] - min_buy_price
                )
        
        # Return the maximum profit possible from 2 transactions
        return table[k][n-1]
