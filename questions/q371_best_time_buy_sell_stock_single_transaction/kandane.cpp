class Solution {
	public:
	int maxProfit(vector<int>& prices) {
		// Initialize variable to store the best buy price and max profit till now
		int buyPrice = prices[0];
		int profit = 0;

		// For every price determine if it can be a good buy price, else, update the best possible profit till now
		for (int p : prices) {
			if (p < buyPrice) {
				buyPrice = p;
			}
			else {
				profit = max(profit, p-buyPrice);
			}
		}

		return profit;
	}
};
