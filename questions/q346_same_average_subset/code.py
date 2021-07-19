class Solution:
    def splitArraySameAverage(self, nums) -> bool:
        

        # Find average of array
        n = len(nums)
        avg = sum(nums) / n

        # Calculate the maximum value of average that we can reach
        required = int(n * avg)

        # Next step is to form a dp table for the problem :
        # Find the minimum count of numbers needed to get a sum equal to "required"
        table = [None for _ in range(required+1)]

        # Initial conditions
        for i in range(1, required+1) :
            table[i] = (False, -1)
        table[0] = (True, 0)
        
        # Fill the DP table
        for i in range(1, n+1) :
            for j in range(required, 0, -1) :
                if nums[i-1] <= j :
                    option = table[j - nums[i-1]]
                    if option[0] :
                        if table[j][0] :
                            table[j] = (True, max(1 + option[1], table[j][1]))
                        else :
                            table[j] = (True, (1 + option[1]))
                
                if table[j][0] :
                    cur_val = j / table[j][1]
                    if cur_val == avg and table[j][1] < n :
                        return True
            print(table)
        
        # Return False if we cant do it
        return False


# Fails this case
# [3,4,9,4,4,3,9,8,5,3]
