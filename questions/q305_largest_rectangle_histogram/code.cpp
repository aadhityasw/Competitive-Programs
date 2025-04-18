class Solution {
	public:
	int largestRectangleArea(vector<int>& heights) {
		// Make a copy of heights and add two more heights of 0 to the end for ease
		vector<int> arr;
		arr.push_back(0);
		for (int height : heights) {
			arr.push_back(height);
		}
		arr.push_back(0);

		// Get the total count now
		int n = arr.size();

		// Create a stack to store increasing height's indicies
		stack<int> hStack;
		// Push 0 as it would act as the smallest number of height 0
		hStack.push(0);

		// Find and store the maxArea
		int maxArea = 0;

		// Parse through the heights
		for (int i=1; i<n; i++) {
			while (arr[i] < arr[hStack.top()]) {
				// Height is the top element from stack
				// Width goes from 1 before i to the second top of stack
				// Because there will be hStack.top()'s height from i till the second top position in the stack
				int curHeight = arr[hStack.top()];
				hStack.pop();
				int curWidth = i - hStack.top() - 1;
				
				maxArea = max(maxArea, curHeight*curWidth);
			}
			hStack.push(i);
		}

		return maxArea;
	}
};
