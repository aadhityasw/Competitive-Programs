class Solution:

    def findNumberOfDays(self, arr, capacity) :
        """
        Finds the number of days needed to ship all the packages with a truck of given capacity

        Parameters
        ----------
        arr - a list of package weights
        capacity - the truck's capacity

        Return
        ------
        days - the number of days to ship all packages
        """

        # Initialize a variable to store the day count, and the capacity shipped in the current day
        days = 0
        cur_weight = 0

        # Traverse through the packages to find the number of days required
        for num in arr :
            if num > capacity :
                return float("inf")
            cur_weight += num
            if cur_weight > capacity :
                days += 1
                cur_weight = num
        
        # Return the number of days required
        return days + 1


    def leastWeightCapacity(self, arr, N, D):

        # Find the sum of all the packages
        total_weight = sum(arr)

        # The minimum capacity of the truck needed to finish the job in `D` days is to be found
        # We can apply a binary search, to search in the range[0 ... total_weight] for the minimum capacity

        front = 0
        rear = total_weight
        ans = float("inf")
        while front <= rear :
            mid = (front + rear) // 2

            # The mid value is the current capacity of the truck
            capacity = mid

            # Find the number of days required with this truck
            required_days = self.findNumberOfDays(arr, capacity)

            # If this value is acceptable
            if required_days <= D :
                # We store the current capacity value as it can be our answer
                ans = capacity

                # We also proceed woth our search to see if we can do the same with a lower capacity value
                rear = mid - 1
            
            else :
                # If the required days is too high, we increase the capacity
                front = mid + 1
        
        # Return the minimum capacity found during the search
        return ans




if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        D=int(input())
        
        ob = Solution()
        print(ob.leastWeightCapacity(arr,N,D))
