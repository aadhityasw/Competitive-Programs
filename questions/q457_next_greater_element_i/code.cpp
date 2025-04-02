class Solution {
    public:
        vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
            stack<int> numStack;
            map<int, int> numToGr;
    
            for (int i=nums2.size()-1; i>=0; i--) {
                while (!numStack.empty() && numStack.top() <= nums2[i]) {
                    numStack.pop();
                }
    
                if (numStack.empty()) {
                    numStack.push(nums2[i]);
                    numToGr[nums2[i]] = -1;
                }
                else {
                    numToGr[nums2[i]] = numStack.top();
                    numStack.push(nums2[i]);
                }
            }
    
            vector<int> ans;
            for (int num : nums1) {
                ans.push_back(numToGr[num]);
            }
            return ans;
        }
    };
