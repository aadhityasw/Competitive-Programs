class Solution:

    def getMaxSum(self, nums: List[int], s, e) -> List[int] :
        if (s > e) :
            return [0, 0, 0]
        elif s == e :
            self.maxSum = max(self.maxSum, nums[s])
            return [nums[s], nums[s], nums[s]]
        else :
            mid = s + ((e - s)//2)
            left = self.getMaxSum(nums, s, mid)
            right = self.getMaxSum(nums, mid+1, e)

            self.maxSum = max(self.maxSum, left[2]+right[0], left[2], right[0])

            cur = [
                max(left[0], left[1]+right[0]),
                left[1]+right[1],
                max(left[2]+right[1], right[2])
            ]
            return cur

    def maxSubArray(self, nums: List[int]) -> int:
        self.maxSum = float('-inf')
        self.getMaxSum(nums, 0, len(nums)-1)
        return self.maxSum
