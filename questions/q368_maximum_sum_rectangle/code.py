
"""                 Solution causes a TLE Error              """


class Solution:

    def Kadanes(self, arr) :
        """
        Given an array of numbers, returns the maximum sum that can be formed from a subarray.

        Parameters
        ----------
        arr - a list of numbers

        Return
        ------
        max_sum - the maximum sum possible from a subarray of the provided array
        """

        # Initialize the max_sum and current sum
        max_sum = float("-inf")
        cur_sum = 0

        # Find the maximum subarray sum by traversing through the array
        for num in arr :
            cur_sum += num
            
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0 :
                cur_sum = 0
        
        # Return the maximum sum
        return max_sum


    def maximumSumRectangle(self, r, c, matrix):

        # Initialize a variable to store the maximum sum
        max_sum = float("-inf")

        # For each row find the maximum sum subarray from 0 till that row of the matrix
        for i in range(r) :

            # Initialize the array to be the size of the columns
            arr = [0]*c

            # For each row below, find the maximum sum subarray from row[i:j]
            for j in range(i, r) :

                # Add all the elements of the row 'j' to the matrix
                for k in range(c) :
                    arr[k] += matrix[j][k]
            
                # Use Kadanes on this array to find the maximum sum
                max_sum = max(
                    max_sum,
                    self.Kadanes(arr)
                )

        # Return the maximum sum of the subarray from the matrix
        return max_sum
