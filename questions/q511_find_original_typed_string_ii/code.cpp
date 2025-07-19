class Solution {
public:

    vector<int> getLetterFrequencies(string word) {
        vector<int> freq;

        if (word.length() == 0) {
            return freq;
        }

        int s=0, e=0;
        while (s < word.length()) {
            e = s+1;
            while (e < word.length() && word[e] == word[e-1]) {
                e++;
            }
            freq.push_back(e-s);
            s = e;
        }

        return freq;
    }


    int possibleStringCount(string word, int k) {
        vector<int> freq = getLetterFrequencies(word);
        int nf = freq.size();

        int mod = (pow(10, 9) + 7);

        // Get total counts of permutations
        long totalCount = 1;
        for (int f : freq) {
            totalCount = (totalCount * f) % mod;
        }

        if (nf >= k) {
            return totalCount;
        }

        // One way to form an empty string
        vector<int> dp1(k, 1);
        vector<int> dp2(k, 0);

        // Form the DP table for size<=k
        for(int i=1; i<=nf; i++) {
            for (int j=1; j<k; j++) {
                dp2[j] = dp1[j-1] - ((freq[i-1] < j)? dp1[j-freq[i-1]-1] : 0);
                if (dp2[j] < 0) {
                    dp2[j] += mod;
                }
                dp2[j] = (dp2[j-1] + dp2[j]) % mod;
            }

            std::copy(dp2.begin(), dp2.end(), dp1.begin());
        }

        // Get count of all permutations of size less than k
        int lessCounts = 0;
        lessCounts = dp1[k-1];

        int ans = (int) ((totalCount - lessCounts) % mod);
        if (ans < 0) {
            ans += mod;
        }
        return ans;
    }
};
