class Solution {
    public:
        void nextPermutation(vector<int>& nums) {
            int pos = -1;
            for (int i = nums.size()-1; i> 0; i--) {
                if (nums[i-1] < nums[i]) {
                    pos = i-1;
                    break;
                }
            }
    
            int pos2 = pos;
            int f,b;
            if (pos == -1) {
                f=0;
            }
            else {
                for (int i = nums.size()-1; i>=0; i--) {
                    if (nums[i] > nums[pos] || i == pos) {
                        pos2 = i;
                        break;
                    }
                }
                int temp = nums[pos];
                nums[pos] = nums[pos2];
                nums[pos2] = temp;
                f = pos+1;
            }
            b = nums.size()-1;
    
            while (f < b) {
                int temp = nums[f];
                nums[f] = nums[b];
                nums[b] = temp;
                f++;
                b--;
            }
        }
    };
