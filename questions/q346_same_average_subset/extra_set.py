# Let the array be  ....



class Solution:
    def splitArraySameAverage(self, nums) -> bool:
        

        # Find average of array
        n = len(nums)
        avg = sum(nums) / n

        # Calculate the maximum value of average that we can reach
        required = int(n * avg)

        # Next step is to form a dp table for the problem :
        # Find the minimum count of numbers needed to get a sum equal to "required"
        table = [[None for _ in range(required+1)] for _ in range(n+1)]

        # Initial conditions
        for i in range(1, required+1) :
            table[0][i] = [False, set()]
        for i in range(n+1) :
            table[i][0] = [True, {0}]
        
        # Fill the DP table
        for i in range(1, n+1) :
            for j in range(1, required+1) :
                table[i][j] = table[i-1][j]
                if nums[i-1] <= j :
                    option = table[i-1][j - nums[i-1]]
                    if option[0] :
                        if table[i][j][0] :
                            table[i][j] = [True, table[i][j][1].union({(1 + numb) for numb in option[1]})]
                        else :
                            table[i][j] = [True, {(1 + numb) for numb in option[1]}]
        
        # Find any "True" value with the required average
        for i in range(1, n+1) :
            for j in range(1, required+1) :
                if table[i][j][0] :
                    for c in table[i][j][1] :
                        cur_val = j / c
                        if cur_val == avg and c < n :
                            return True
        
        # Return False if we cant do it
        return False

