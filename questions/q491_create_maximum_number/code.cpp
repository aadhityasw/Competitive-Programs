class Solution {
	public:

	vector<int> chooseLargestNumber(vector<int>& num, int c) {
		// We need to choose the greatest number of c digits from num

        // Initialize a vector to store the largest number
        vector<int> result;

        // Declare a stack for maintaining a decreasing order of digits
        stack<int> decDigitStack;

        // Get the number of digits in num
        int n = num.size();

        // Calculate the number of characters to remove
        int numDigitsToRemove = n - c;

        // If we have to remove all the digits, then just return empty vector
        if (numDigitsToRemove >= n) {
            return result;
        }

        // Find the largest number by parsing through num
        int i = 0;
        while (i < n) {
            if (decDigitStack.empty() || decDigitStack.top() >= num[i] || numDigitsToRemove == 0) {
                decDigitStack.push(num[i]);
                i++;
            }
            else {
                decDigitStack.pop();
                numDigitsToRemove--;
            }
        } 

        // If we are still not done removing enough digits
        while (numDigitsToRemove > 0) {
            decDigitStack.pop();
            numDigitsToRemove --;
        }

        // Move the elements from stack into result and return it
        while (!decDigitStack.empty()) {
            result.push_back(decDigitStack.top());
            decDigitStack.pop();
        }
        reverse(result.begin(), result.end());

        return result;
	}


	vector<int> mergePartialCandidates(vector<int>& num1, vector<int>& num2) {

		// Get the lengths of the 2 numbers
		int n1 = num1.size();
		int n2 = num2.size();

		// Initialize a vector to store the merged number
		vector<int> result;
		
		// Use a 2 pointer approach to merge the numbers
		int pos1 = 0, pos2 = 0;
		while (pos1 < n1 && pos2 < n2) {
			if (num1[pos1] < num2[pos2]) {
				result.push_back(num2[pos2]);
				pos2++;
			}
			else if (num1[pos1] > num2[pos2]){
				result.push_back(num1[pos1]);
				pos1++;
			}
            else {
                // If the current digits are equal
                // Find out which has the next bigger digit and take that
                int nextPos1 = pos1 + 1;
                int nextPos2 = pos2 + 1;
                
                // Loop through until the digits are same from there
                while (nextPos1 < n1 && nextPos2 < n2 && num1[nextPos1] == num2[nextPos2]) {
                    nextPos1++;
                    nextPos2++;
                }
                
                if (nextPos1 >= n1 && nextPos2 >= n2) {
                    // If both have gone beyond the edge, then take any
                    result.push_back(num1[pos1]);
				    pos1++;
                }
                else if (nextPos1 >= n1) {
                    // If we have gone beyond the edge in num1, then take the digit from num2
                    result.push_back(num2[pos2]);
				    pos2++;
                }
                else if (nextPos2 >= n2) {
                    // If we have gone beyond the edge in num2, then take the digit from num1
                    result.push_back(num1[pos1]);
				    pos1++;
                }
                else if (num1[nextPos1] > num2[nextPos2]) {
                    // If the next digit is larger in num1, then choose from num1
                    result.push_back(num1[pos1]);
				    pos1++;
                }
                else if (num1[nextPos1] < num2[nextPos2]) {
                    // If the next digit is larger in num2, then choose from num2
                    result.push_back(num2[pos2]);
				    pos2++;
                }
            }
		}

		// Add any leftovers into the merged number 
		while (pos1 < n1) {
			result.push_back(num1[pos1]);
			pos1++;
		}
        while (pos2 < n2) {
			result.push_back(num2[pos2]);
			pos2++;
		}

		// Return the merged number
		return result;
	}


	void updateOverallMaximumNumber(vector<int>& maximumNumber, vector<int>& candidateNumber) {
		
		// Get the number of digits
		int n = maximumNumber.size();

		// We compare every digit from left to right
		bool isCandidateGreater = false;
		for (int i=0; i<n; i++) {
			if (maximumNumber[i] < candidateNumber[i]) {
				isCandidateGreater = true;
				break;
			}
            else if (maximumNumber[i] > candidateNumber[i]) {
				isCandidateGreater = false;
				break;
			}
		}

		// If the candidate is greater, then we copy it into the maximum number
		if (isCandidateGreater) {
			maximumNumber = candidateNumber;
		}
	}


	
	vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {

		// Get the number of digits in num1 and num2
		int d1 = nums1.size();
		int d2 = nums2.size();

		// Initialize a vector to store the overall maximum number of k digits
		vector<int> maximumNumber(k, 0);
		
		// We need to choose a total of k digits from both num1 and num2
		// Which means there can be anywhere from (max(0, k-d2)) to (min(d1, k)) digits taken from num1 and the rest from num2
		// We parse every such combination of choices and then get the best decreasing subsequence from num1 and num2 
		for (int i=max(0, k-d2); i<=min(d1, k); i++) {
			int numDigitsFromNums1 = i;
			int numDigitsFromNums2 = k - i;

			// Get the partial candidates from nums1 and nums2
			vector<int> partialCandidateFromNums1 = chooseLargestNumber(nums1, numDigitsFromNums1);
			vector<int> partialCandidateFromNums2 = chooseLargestNumber(nums2, numDigitsFromNums2);

			// Merge these partial candidates to form the maximum number possible from these candidate's digits
			vector<int> candidateNumber = mergePartialCandidates(partialCandidateFromNums1, partialCandidateFromNums2);

			// Compare this candidate with our overall maximum and update the overall maximum if out current candidate is larger
			updateOverallMaximumNumber(maximumNumber, candidateNumber);
		}

		// Return the maximum number
		return maximumNumber;
	}
};
