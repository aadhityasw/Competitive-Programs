#include<map>

class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        int n = nums.size();
        int ans=0;

        map<int, int> freq;
        for (int i=0;i<n; i++) {
            for (int j=i+1; j<n; j++) {
                int prod = nums[i] * nums[j];
                ans += freq[prod]*8;
                freq[prod]++;
            }
        }
        return ans;
    }
};
