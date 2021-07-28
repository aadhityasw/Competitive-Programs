class Solution:
    def maxProfit(self, prices) -> int:
        
        n = len(prices)
        k = 2
        
        # Initialize the table
        table = [[0 for _ in range(n+1)] for _ in range(k+1)]
        
        # Fill the table values
        for i in range(1, k+1) :
            # For each day fill the values of having `i` transactions
            for j in range(1, n) :
                # We start the transaction on the l'th day (buy) and end on the j'th day (sell), here we choose an appropriate value of `l` for the current day `j`
                min_buy_price = prices[0]
                for l in range(1, j+1) :
                    min_buy_price = min(
                        min_buy_price,
                        prices[l] - table[i-1][l-1]
                    )
                
                # Choose to whether sell a stock today on buying it on l`th day, or to just not do a transaction on the j`th day
                table[i][j] = max(
                    table[i][j-1],
                    prices[j] - min_buy_price
                )
        
        # Return the maximum profit possible from 2 transactions
        return table[2][n-1]
