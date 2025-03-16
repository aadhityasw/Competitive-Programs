class Solution {
    public:
        int findDuplicate(vector<int>& nums) {
            int n = nums.size()-1;
            int numBits = (log(n) / log(2)) + 1;
            int *actual = new int[numBits];
            int *current = new int[numBits];
    
            for (int i=0; i<numBits; i++) {
                for (int j = 1; j<= n; j++) {
                    int num = (j % (int)(pow(2, i+1))) / (pow(2, i));
                    if (num > 0) {
                        actual[i]++;
                    } 
                }
    
                for (int j=0; j<nums.size(); j++) {
                    int num = (nums[j] % (int)(pow(2, i+1))) / (pow(2, i));
                    if (num > 0) {
                        current[i]++;
                    }
                }
            }
            
            int ans = 0;
            for (int i=0; i<numBits; i++) {
                if (actual[i] < current[i]) {
                    ans += pow(2, i);
                }
            }
    
            return ans;
        }
    };
