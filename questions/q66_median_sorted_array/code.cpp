class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int aMin = 0;
        int aMax = nums1.size();
        int leftHalfLength = (nums1.size() + nums2.size() + 1) / 2;

        while (aMin <= aMax) {
            int aVal = aMin + (aMax - aMin)/2;
            int bVal = leftHalfLength - aVal;

            int aLeftEnd = (aVal > 0)? nums1[aVal - 1] : INT_MIN;
            int aRightStart = (aVal < nums1.size())? nums1[aVal] : INT_MIN;
            int bLeftEnd = (bVal > 0)? nums2[bVal - 1] : INT_MIN;
            int bRightStart = (bVal < nums2.size())? nums2[bVal] : INT_MIN;

            
            if (aRightStart != INT_MIN && bLeftEnd != INT_MIN && aRightStart < bLeftEnd) {
                aMin = aVal + 1;
            }
            else if (aLeftEnd != INT_MIN && bRightStart != INT_MIN && bRightStart < aLeftEnd) {
                aMax = aVal - 1;
            }
            else {
                int leftHalfEnd = (aLeftEnd == INT_MIN)? bLeftEnd : (bLeftEnd == INT_MIN)? aLeftEnd : max(aLeftEnd, bLeftEnd);
                int rightHalfStart = (aRightStart == INT_MIN)? bRightStart : (bRightStart == INT_MIN)? aRightStart : min(aRightStart, bRightStart);

                if ((nums1.size() + nums2.size()) % 2 == 0) {
                    return (double)(leftHalfEnd + rightHalfStart) / 2;
                }
                else {
                    return leftHalfEnd;
                }
            }
        }

        return -1;
    }
};
