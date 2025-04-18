int Solution::minCut(string A) {
    // Get the length of the string
    int n = A.length();

    // Initialize a vector to store the max length palindrome starting from ith index
    // By default a palindrome of length = 1 can be formed
    vector<int> maxPalindromeSizeFromIndex(n, 1);

    // Find out all the palindromes possible from the substrings of A
    for (int i=0; i<n; i++) {
        // Odd length palindromes
        int start = i;
        int end = i;
        while (start>=0 && end<n && A[start] == A[end]) {
            maxPalindromeSizeFromIndex[start] = max(end - start + 1, maxPalindromeSizeFromIndex[start]);
            
            start --;
            end ++;
        }

        // Even Length palindromes
        start = i;
        end = i+1;
        while (start>=0 && end<n && A[start] == A[end]) {
            maxPalindromeSizeFromIndex[start] = max(end - start + 1, maxPalindromeSizeFromIndex[start]);
            
            start --;
            end ++;
        }
    }
    

    // Initialize a vector to store num cuts from ith index to the end
    vector<int> numCutsTillEndDP(n+1, 0);
    numCutsTillEndDP[n] = -1;
    for (int i=n-1; i>=0; i--) {
        numCutsTillEndDP[i] = min(
            numCutsTillEndDP[i + maxPalindromeSizeFromIndex[i]] + 1,
            numCutsTillEndDP[i+1] + 1
        );
    }
    
    return numCutsTillEndDP[0];
}

