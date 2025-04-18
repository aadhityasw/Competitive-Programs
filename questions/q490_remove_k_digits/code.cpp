// Uses a monotonic increasing stack

class Solution {
	public:
	string removeKdigits(string num, int k) {
		
		// Get the total number of digits
		int digits = num.length();

		// Declare a stack to store the digits from left to right in increasing order
		stack<int> incDigitStack;

		// Process the digits
		// If we see a larger digit, enter into stack, else pop and reduce k as we will ignore that digit
		int i = 0;
		while (i<digits) {
			if (incDigitStack.empty() || incDigitStack.top() <= num[i] || k==0) {
				incDigitStack.push(num[i]);
				i++;
			}
			else {
				incDigitStack.pop();
				k--;
			}
		}

		// If we have not yet removed k elements
		while (k > 0) {
			incDigitStack.pop();
			k--;
		}

		// Extract digits from the stack and make the result number
		string result = "";
		while (!incDigitStack.empty()) {
			result.push_back(incDigitStack.top());
			incDigitStack.pop();
		}
		reverse(result.begin(), result.end());

		// Post-processing
		// Remove leading zeros
		int leadingZeros = 0;
		while (leadingZeros < result.size() && result[leadingZeros] == '0') {
			leadingZeros++;
		}
		if (leadingZeros < result.size()) {
			result = result.substr(leadingZeros);
		}
		else if (leadingZeros == result.size()) {
			result = "0";
		}
		
		// If the result is empty, then add a zero
		if (result.length() == 0) {
			result = "0";
		}

		return result;
	}
};
