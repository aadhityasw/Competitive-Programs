class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):

        # If the number of floors is less than or equal to 1, then number of droppings is 1
        # If we have only 1 egg, then the number of droppings in worst case is equal to the number of floors
        if k <= 1 or n == 1 :
            return k

        min_droppings = float("inf")

        # Go on for each floor and check for what happens if the egg did or did not brake in that floor
        for i in range(1, k+1) :
            cur_droppings = max(
                self.eggDrop(n-1, i-1), # Check less than current index, if the egg breaks
                self.eggDrop(n, k-i)  # Check above, if the egg does not break
            ) + 1

            min_droppings = min(min_droppings, cur_droppings)
        
        return min_droppings


import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
