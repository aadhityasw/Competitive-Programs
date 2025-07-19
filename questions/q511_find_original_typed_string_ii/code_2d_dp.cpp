// This causes memory limit exceeded as we store all the states
// (But actually we can just get away maintaining just 2 states, and this efficiency is done in the next question)
// This is better in terms of understanding the problem



class Solution {
public:

    vector<int> getLetterFrequencies(string word) {
        vector<int> freq;

        if (word.length() == 0) {
            return freq;
        }

        int c=1;
        for (int i=1; i<word.length(); i++) {
            if (word[i] == word[i-1]) {
                c++;
            }
            else {
                freq.push_back(c);
                c = 1;
            }
        }
        freq.push_back(c);

        return freq;
    }


    int possibleStringCount(string word, int k) {
        vector<int> freq = getLetterFrequencies(word);
        int nf = freq.size();

        vector<vector<int>> dp(nf+1, vector<int>(k));
        int mod = (pow(10, 9) + 7);

        // One way to form an empty string
        dp[0][0] = 1;

        // Form the DP table for size<=k
        for(int i=1; i<=nf; i++) {
            for (int j=1; j<k; j++) {
                for (int l=1; l<=min(freq[i-1],j); l++) {
                    dp[i][j] = (dp[i][j] + dp[i-1][j-l]) % mod;
                }
            }
        }

        // Get total counts of permutations
        long totalCount = 1;
        for (int f : freq) {
            totalCount = (totalCount * f) % mod;
        }

        // Get count of all permutations of size less than k
        int lessCounts = 0;
        for (int c : dp[nf]) {
            lessCounts = (lessCounts + c) % mod;
        }

        int ans = (int) ((totalCount - lessCounts) % mod);
        if (ans < 0) {
            ans += mod;
        }
        return ans;
    }
};
