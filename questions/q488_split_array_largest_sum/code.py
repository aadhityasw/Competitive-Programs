class Solution:
    def getNumGroups(self, nums: List[int], m: int) -> int:
        curK = 0
        rSum = 0

        for num in nums :
            if num > m :
                return float('inf')
            elif (rSum + num) > m :
                curK += 1
                rSum = num
            else :
                rSum += num
        
        return curK+1


    def splitArray(self, nums: List[int], k: int) -> int:
        l = 0
        r = sum(nums)

        while l < r :
            m = l + (r-l)//2

            curK = self.getNumGroups(nums, m)

            if curK > k :
                l = m+1
            else :
                r = m
        
        return l
