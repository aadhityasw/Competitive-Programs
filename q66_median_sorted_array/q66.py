#%%
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) :
        nums = []
        while (len(nums1) and len(nums2)) :
            if nums1[0] < nums2[0] :
                nums.append(nums1[0])
                nums1 = nums1[1:]
            else :
                nums.append(nums2[0])
                nums2 = nums2[1:]
        
        if len(nums1) :
            nums += nums1
        else :
            nums += nums2

        if len(nums) % 2 == 0 :
            median = (nums[(len(nums) // 2) - 1] + nums[len(nums) // 2]) / 2
        else :
            median = nums[len(nums) // 2]
        return median



#%%

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) :
        m, n = len(nums1), len(nums2)
        # Ensures that (n, nums2) is the longer array
        if m > n :
            m, nums1, n, nums2 = n, nums2, m, nums1

        # If one array is empty
        if m == 0 :
            if n % 2 == 0 :
                return (nums2[n // 2] + nums2[(n // 2) - 1]) / 2
            return nums2[n // 2]
        
        left_half_length = (m + n + 1) // 2

        # nums1 can contribute to either 0 up until all of its elements to the left half
        aMinCount = 0
        aMaxCount = m

        while (aMinCount <= aMaxCount) :
            aCount = aMinCount + int((aMaxCount - aMinCount) / 2);
            bCount = left_half_length - aCount

            if aCount > 0 and nums1[aCount - 1] > nums2[bCount] :
                aMaxCount = aCount - 1
            elif aCount < m and nums2[bCount - 1] > nums1[aCount] :
                aMinCount = aCount + 1
            else :
                if aCount == 0 :
                    leftHalfEnd = nums2[bCount - 1]
                elif bCount == 0 :
                    leftHalfEnd = nums1[aCount - 1]
                else :
                    leftHalfEnd = max(nums1[aCount - 1], nums2[bCount - 1])
                
                if (m + n) % 2 :
                    # If the length of merged array is odd

                    return (leftHalfEnd)
                else :
                    if aCount == m :
                        rightHalfStart = nums2[bCount]
                    elif bCount == n :
                        rightHalfStart = nums1[aCount]
                    else :
                        rightHalfStart = min(nums1[aCount], nums2[bCount])

                    return (leftHalfEnd + rightHalfStart) / 2.0
