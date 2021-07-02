class Solution:

    def findPositionInArray(self, element, array) :
        """
        Given an array and a element, returns the count of numbers less than the element.
        """

        # If the element is less than the least, we return 0
        if element < array[0] :
            return 0

        # Find the length of the array
        n = len(array)

        # Perform the binary search
        front = 0
        rear = n-1
        while front < rear :
            mid = (front + rear + 1) // 2
            if array[mid] <= element :
                front = mid 
            else :
                rear = mid - 1
        
        # Return the count
        return front + 1


    def getCountLessThan(self, mid, A) :
        """
        Given a matrix and a element, returns the count of numbers less than the element across all rows.
        """

        # Initialize the count
        count = 0

        # Find the count for each row
        for row in A :
            count += self.findPositionInArray(mid, row)
        
        # Return this overall count
        return count


	# @param A : list of list of integers
	# @return an integer
    def findMedian(self, A):

        # Find the dimensions of the matrix
        m = len(A)
        if m == 0 :
            return
        n = len(A[0])

        # Find the goal position where we will find the median
        # We add 1 because we are given that (n*m) is odd
        goal = ((m * n) // 2) + 1

        # Find the minimum and maximum element in the matrix
        min_ele = float("inf")
        max_ele = -1 * float("inf")
        for row in A :
            min_ele = min(min_ele, row[0])
            max_ele = max(max_ele, row[-1])
        
        # Perform binary search till we reach the goal position
        front = min_ele
        rear = max_ele
        while front < rear :
            # Find the mid position
            mid = (front + rear) // 2

            # In each row find the count of numbers less than mid
            count = self.getCountLessThan(mid, A)

            # Compare this count with our goal and make the decisions
            if count < goal :
                front = mid + 1
            else :
                rear = mid
        
        return front
