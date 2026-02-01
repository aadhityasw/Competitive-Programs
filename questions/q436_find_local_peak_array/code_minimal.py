# Just the minimal barebones code
# Move in the direction of increasing numbers


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        while l <= r :
            m = l + (r-l)//2

            if (m == 0 or nums[m-1] < nums[m]) and (m == len(nums)-1 or nums[m+1] < nums[m]) :
                return m
            elif m > 0 and nums[m-1] > nums[m] :
                r = m-1
            else :
                l = m+1
                