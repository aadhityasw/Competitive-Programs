class Solution:
    
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):

        # Find the maximum among the elements
        maxi = max(arr)

        # If the maximum is less than 1, we return 1
        if maxi < 1 :
            return 1

        # Segregate the negative numbers
        pos = 0
        for i in range(n) :
            if arr[i] <= 0 :
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1
        
        # Loop through all the positive numbers and mark the numbers visited as the position
        # Say we have a number `1`, then we mark the number at position `pos + 1 - 1` by negating it.
        for i in range(pos, n) :
            cur = (pos + abs(arr[i]) - 1)
            # If the current index is not already visited, then visit and mark it
            if (pos <= cur < n) and (arr[cur] > 0) :
                arr[cur] *= -1
        
        # We loop through all the originally positive numbers and find the unmarked number
        for i in range(pos, n) :
            if arr[i] > 0 :
                return i - pos + 1
        
        # If all else fails we return one greater than the maximum
        return n - pos + 1






import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
