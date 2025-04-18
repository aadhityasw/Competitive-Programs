// Causes Memory limit exceeded error for the last test case
// If I convert the recursion to loops, it causes TLE for the last test case

class Solution {
	public:

	string recurseChooseDigits(string num, int c) {
		// Get the number of digits currently
		int numDigits = num.length();

		if (c == 0) {
			return "";
		}
		else if (numDigits == c) {
			return num;
		}
        else if (numDigits < c) {
            return "0";
        }
		
		// Now we need to choose the least digit from first k+1 digits
		int leastDigitPos = 0;
		for (int i=0; i<numDigits-c+1; i++) {
			if (num[i] < num[leastDigitPos]) {
				leastDigitPos = i;
			}
		}

		// Store the result
		string result = "";
        result += num[leastDigitPos];
		result += recurseChooseDigits(num.substr(leastDigitPos+1), c-1);

		return result;
	}

	string removeKdigits(string num, int k) {
		// Get the length of num aka number of digits
		int digits = num.length();

		if (k >= digits) {
			return "0";
		}

		// We follow a greedy approach where we choose the smallest digit from the first n-(n-k-1) = k+1 digits and do this so on
		string result = recurseChooseDigits(num, digits-k);

		// Remove any trailing 0's
		int numTrailingZeros=0;
		while (result[numTrailingZeros] == '0') {
			numTrailingZeros++;
		}
		result = result.substr(numTrailingZeros);
        if (result == "") {
            result = "0";
        }

		return result;
	}
};
