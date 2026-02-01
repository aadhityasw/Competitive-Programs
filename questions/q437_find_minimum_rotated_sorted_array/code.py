class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r = len(nums)-1

        while l < r :
            m = l + (r-l)//2

            if nums[l] <= nums[m] and nums[r] <= nums[l] :
                l = m+1
            else :
                r = m
        
        return nums[l]
