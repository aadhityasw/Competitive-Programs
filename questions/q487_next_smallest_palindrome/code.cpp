class Solution {
	public:
	vector<int> generateNextPalindrome(int num[], int n) {
	    
	    // Initialize a vector to store the result
	    vector<int> result;
		
		// Base condition : If the number is all 9's then we will have to increase n
		int countNine = 0;
		for (int i=0; i<n; i++) {
		    if (num[i] == 9) {
		        countNine ++;
		    }
		}
		
		if (countNine == n) {
		    // New number is 1 followed by n 0's and we increment n to store the new length
		    // Basically add 1 to the original number
		    n++;
		    result.push_back(1);
		    for (int i=0; i<n-1; i++) {
		        result.push_back(0);
		    }
		}
		else {
		    // There wont be a change in dimension
		    // Just enter the elements of the array
		    for (int i=0; i<n; i++) {
		        result.push_back(num[i]);
		    }
		}
		
		// Determine the start and end indexes
		int left = (n-1)/2;
		int right = (n)/2;
		
		// Loop and compare the left and right indices to find if we need to increment the middle position
		bool needIncrement = false;
		bool isNumberGreaterThanOriginal = false;
		while (left >= 0) {
		    if (result[left] > result[right]) {
		        result[right] = result[left];
		        isNumberGreaterThanOriginal = true;
		    }
		    if (result[left] < result[right]) {
		        if (isNumberGreaterThanOriginal) {
		            result[right] = result[left];
		        }
		        else {
		            needIncrement = true;
		            break;
		        }
		    }
		    left--;
		    right++;
		}
		
		// Loop to do the increment
		left = (n-1)/2;
		int carry = (needIncrement || !isNumberGreaterThanOriginal)? 1 : 0;
		while (left >= 0 && carry>0) {
		    if (result[left] == 9 && carry>0) {
		        result[left] = 0;
		    }
		    else if (carry > 0) {
		        result[left]++;
		        carry = 0;
		    }
		    left--;
		}
		
		// Now loop to force make palindrome by copying left index into right
		left = (n-1)/2;
		right = n/2;
		while (left >= 0) {
		    if (result[left] != result[right]) {
		        result[right] = result[left];
		    }
		    left--;
		    right++;
		}
		
		return result;
	}
};
