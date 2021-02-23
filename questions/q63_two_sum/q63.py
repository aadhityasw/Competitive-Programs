class Solution:
    def twoSum(self, nums, target: int) :
        table = {}
        for i in range(len(nums)) :
            if target - nums[i] in table :
                return [table[target - nums[i]], i]
            table[nums[i]] = i
