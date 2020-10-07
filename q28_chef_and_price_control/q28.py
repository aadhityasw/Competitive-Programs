# Codechef June2020

# PRICECON
# https://www.codechef.com/problems/PRICECON
# Chef and Price Control

"""

Chef has N items in his shop (numbered 1 through N); for each valid i, the price of the i-th item is Pi. Since Chef has very loyal customers, all N items are guaranteed to be sold regardless of their price.

However, the government introduced a price ceiling K, which means that for each item i such that Pi>K, its price should be reduced from Pi to K.

Chef's revenue is the sum of prices of all the items he sells. Find the amount of revenue which Chef loses because of this price ceiling.

"""

test = int(input())
for t in range(test) :
    n, k = list(map(int, input().strip().split()))
    parr = list(map(int, input().strip().split()))
    loss = 0
    for p in parr :
        if p > k :
            loss += (p-k)
    print(loss)
