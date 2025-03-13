class Solution {
    public:
        bool canRobKHouses(int amt, vector<int>& nums, int k) {
            int numRobbed = 0;
    
            for (int i=0; i<nums.size(); ) {
                if (nums[i] <= amt) {
                    numRobbed++;
                    i+= 2;
                }
                else {
                    i++;
                }
            }
    
            if (numRobbed >= k) {
                return true;
            }
            return false;
        }
    
        int minCapability(vector<int>& nums, int k) {
            int maxMoney = 0;
            int n = nums.size();
    
            for (int i=0; i<n; i++) {
                if (nums[i]>maxMoney) {
                    maxMoney = nums[i];
                }
            }
            
            int s = 0;
            int e = maxMoney;
            int mid;
            while (s < e) {
                mid = (s+e)/2;
    
                if (canRobKHouses(mid, nums, k)) {
                    e = mid;
                }
                else {
                    s = mid+1;
                }
            }
    
            return s;
        }
    };
