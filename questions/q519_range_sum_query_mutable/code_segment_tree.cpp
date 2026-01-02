class NumArray {
public:
    map<int, int> tree;
    int numEle;
    int n;

    NumArray(vector<int>& nums) {
        n = (nums.size()) * (nums.size()+1);
        numEle = nums.size();
        buildTree(1, nums, 0, nums.size()-1);
    }

    int buildTree(int curNode, vector<int>& nums, int start, int end) {
        if (start == end) {
            tree[curNode] = nums[start];
        }
        else {
            int mid = start + (end - start)/2;
            tree[curNode] = buildTree(curNode*2, nums, start, mid) + buildTree(curNode*2+1, nums, mid+1, end);
        }

        return tree[curNode];
    }
    
    void update(int index, int val) {
        updateTreeRecursive(1, 0, numEle-1, index, val);
    }

    int updateTreeRecursive(int curNode, int start, int end, int index, int val) {
        if (!(start <= index && index <= end)) {
            return tree[curNode];
        }
        else if (start == index && end == index) {
            tree[curNode] = val;
            return tree[curNode];
        }
        else {
            int mid = start + (end - start)/2;
            tree[curNode] = updateTreeRecursive(curNode*2, start, mid, index, val) + updateTreeRecursive(curNode*2+1, mid+1, end, index, val);
            return tree[curNode];
        }
    }
    
    int sumRange(int left, int right) {
        return findSumRecursive(1, 0, numEle-1, left, right);
    }

    int findSumRecursive(int curNode, int start, int end, int left, int right) {
        if (start > left || end < right || left > end || right < start) {
            return 0;
        }
        else if (start == left && end == right) {
            return tree[curNode];
        }
        else {
            int mid = start + (end - start)/2;
            if (left > mid) {
                return findSumRecursive(curNode*2+1, mid+1, end, left, right);
            }
            else if (right <= mid) {
                return findSumRecursive(curNode*2, start, mid, left, right);
            }
            else {
                return findSumRecursive(curNode*2, start, mid, left, mid) + findSumRecursive(curNode*2+1, mid+1, end, mid+1, right);
            }
            
        }
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
