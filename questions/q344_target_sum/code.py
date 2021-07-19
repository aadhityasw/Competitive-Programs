class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        
        n = len(nums)
        
        # Calculate the required sum
        total_sum = sum(nums)
        required_sum = (target + total_sum) / 2
        
        if required_sum != int(required_sum) :
            return 0
        required_sum = int(required_sum)
        
        # Form the DP table
        table = [[0 for _ in range(required_sum + 1)] for _ in range(n + 1)]
        for i in range(n + 1) :
            table[i][0] = 1
        
        # Fill the table
        for i in range(1, n+1) :
            for j in range(1, required_sum + 1) :
                if nums[i-1] != 0 and nums[i-1] <= j :
                    table[i][j] += table[i-1][j - nums[i-1]]
                table[i][j] += table[i-1][j]
        
        # Return the required value
        return table[n][required_sum] * (2 ** (nums.count(0)))
