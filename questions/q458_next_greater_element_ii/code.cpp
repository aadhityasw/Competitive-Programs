class Solution {
    public:
        vector<int> nextGreaterElements(vector<int>& nums) {
            stack<int> numStack;
            int n = nums.size();
            vector<int> ans(n, INT_MIN);
    
            // We consider the array to be linear and do the normal computation
            for (int i=n-1; i>=0; i--) {
                while (!numStack.empty() && numStack.top() <= nums[i]) {
                    numStack.pop();
                }
                
                if (!numStack.empty()) {
                    ans[i] = numStack.top();
                }
                numStack.push(nums[i]);
            }
    
            // Because it is a circular list, we traverse it again from last with the remaining stack from the previous traversal
            for (int i=n-1; i>=0; i--) {
                while (!numStack.empty() && numStack.top() <= nums[i]) {
                    numStack.pop();
                }
                
                if (ans[i] == INT_MIN) {
                    if (!numStack.empty()) {
                        ans[i] = numStack.top();
                    }
                    else {
                        ans[i] = -1;
                    }
                }
            }
    
            return ans;
        }
    };
