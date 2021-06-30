"""
Problem with Binary Search implementation
"""



class Solution:

    def __init__(self):
        self.store = {}

    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C, level=0):

        # If number of digits needed is zero, then we return 0
        if B == 0 :
            return 0

        n = len(A)

        if C < 0 :
            return 0

        # If the array is empty return or not enough elements are present
        if n == 0 :
            return 0
        
        # If the answer is present in the store, then return it
        if level > 0 and (B, C) is self.store :
            return self.store[(B, C)]

        # If the number of digits is one, then it is the base case
        if B == 1 :

            # Find the position until  which it is possible to choose
            front = 0
            end = n-1
            mid = -1
            while front < end :
                mid = (front+end) // 2
                if A[mid] < C :
                    front = mid+1
                elif A[mid] > C :
                    end = mid-1
                else :
                    front = mid-1
                    end = mid-1
                    mid = mid-1
            
            return mid+1

            """# Loop till we find a number equal or greater than C
            i = -1
            while i < n-1 and A[i+1] < C :
                i += 1
            
            # Return the number of digits that can be useful
            return i+1"""
        
        # If the number of digits required is more, then we perform recursive disintergration of the problem
        
        # Initialize a variable to store the count of all cases
        total_count = 0

        # Binary search till 10*i is less than C so that another level is possible
        start = 0
        # In the zero'th level the first number cannot be 0
        if level == 0 :
            while A[start] == 0 :
                start += 1
        
        # Perform Binary Search
        front = start
        end = n-1
        mid = -1
        while front < end :
            mid = (front+end) // 2
            val = ((10**(B-1))*A[mid])
            if val < C :
                front = mid+1
            elif val > C :
                end = mid-1
            else :
                front = mid
                end = mid
        
        # Add for the previous elements, they will have full amount of combinations
        total_count += (n ** (B-1)) * (mid-start)

        # Find for the mid+1 th choice
        cur_count = self.solve(A, B-1, C-((10**(B-1))*A[mid]), level+1)
        total_count += cur_count


        """while i < n :
            if ((10**(B-1))*A[i]) <= C :
                cur_count = self.solve(A, B-1, C-((10**(B-1))*A[i]), level+1)
                total_count += cur_count
            i += 1"""
        
        # Store this value
        self.store[(B, C)] = total_count
        
        # Return the total count from all sub-parts
        return total_count

            

#A = [ 0, 1, 2, 3, 4, 5, 7, 8, 9 ]
#B = 9
#C = 51822

#A = [0, 1, 2, 5]
#B = 2
#C = 21

A = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
B = 9
C = 661261993


ob = Solution()
print(ob.solve(A, B, C))
