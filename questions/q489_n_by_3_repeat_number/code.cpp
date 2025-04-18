int Solution::repeatedNumber(const vector<int> &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details


		// Maintain a frequency of 2 values
		int pos1 = -1;
		int freq1 = 0;
		int pos2 = -1;
		int freq2 = 0;

		// Parse through the numbers
		for (int i=0; i<A.size(); i++) {
			if (pos1 == -1 && (pos2 == -1 || (pos2>=0 && A[pos2] != A[i]))) {
				pos1 = i;
				freq1++;
			}
			else if (A[pos1] == A[i]) {
				freq1++;
			}
			else if (pos2 == -1) {
				pos2 = i;
				freq2++;
			}
			else if (A[pos2] == A[i]) {
				freq2++;
			}
			else {
				// The current number is different from pos1 and pos2
				// So we ignore all the 3 numbers
				freq1--;
				freq2--;
				if (freq1 <= 0) {
					pos1 = -1;
                    freq1 = 0;
				}
				if (freq2 <= 0) {
					pos2 = -1;
                    freq2 = 0;
				}
			}
		}

		// Get the candidates
        // The last 2 at max left overs will be our solution candidates
        // But we must verify their frequency
		vector<int> candidates;
		if (pos1>=0) {
			candidates.push_back(pos1);
		}
		if (pos2>=0) {
			candidates.push_back(pos2);
		}

		// Find out if any of the candidates have more than n/3 instances
		for (int num : candidates) {
			int freq = 0;
			for (int i=0; i<A.size(); i++) {
				if (A[i] == A[num]) {
					freq++;
				}
			}
			if (freq > A.size()/3) {
				return A[num];
			}
		}

		return -1;
	}

