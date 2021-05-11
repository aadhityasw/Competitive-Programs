class Solution:
    def closestToZero (self,arr, n):
        # If we have less than 2 numbers then exit
        if n < 2 :
            return

        pos = []
        neg = []

        # Split the array into arrays of positive and negative numbers
        for i in range(n) :
            if arr[i] < 0 :
                neg.append(arr[i])
            else :
                pos.append(arr[i])
        
        # Sort the numbers
        pos.sort()
        neg.sort(reverse=True)

        # If any of the category have empty array, then we just return the sum of the first two elements of the other array
        if len(pos) == 0 :
            return neg[0] + neg[1]
        elif len(neg) == 0 :
            return pos[0] + pos[1]
        
        # Initialize the min_sum to be either infinity or the minimum of the sum of the first two elements of the positive and negative arrays
        if len(pos) >= 2 and len(neg) >= 2 :
            if abs((neg[0] + neg[1])) < (pos[0] + pos[1]) :
                min_sum = (neg[0] + neg[1])
            else :
                min_sum = (pos[0] + pos[1])
        elif len(pos) >= 2 :
            min_sum = (pos[0] + pos[1])
        elif len(neg) >= 2 :
            min_sum = (neg[0] + neg[1])
        else :
            min_sum = float("inf")

        # Loop through both the arrays simultaneously using two pointers to find the closest sum to zero
        i = 0
        j = 0
        while i < len(pos) and j < len(neg) :
            if abs(min_sum) > abs(pos[i] + neg[j]) :
                min_sum = pos[i] + neg[j]
            elif abs(min_sum) == abs(pos[i] + neg[j]) :
                min_sum = max(min_sum, (pos[i] + neg[j]))
            
            if min_sum == 0 :
                return min_sum

            if pos[i] < abs(neg[j]) :
                i += 1
            else :
                j += 1

        # To proceed if there are any remaining in positive numbers array, We compare these with the largest absolute negative number until the sum begins to diverge
        while i < len(pos) :
            if abs(min_sum) > abs(pos[i] + neg[-1]) :
                min_sum = pos[i] + neg[-1]
            elif abs(min_sum) == abs(pos[i] + neg[-1]) :
                min_sum = max(min_sum, (pos[i] + neg[-1]))
            else :
                break
            i += 1
        # To proceed if there are any remaining in negative numbers array, We compare these with the largest positive number until the sum begins to diverge
        while j < len(neg) :
            if abs(min_sum) > abs(pos[-1] + neg[j]) :
                min_sum = pos[-1] + neg[j]
            elif abs(min_sum) == abs(pos[-1] + neg[j]) :
                min_sum = max(min_sum, (pos[-1] + neg[j]))
            else :
                break
            j += 1

        # Return the sum closest to zero
        return min_sum



t = int (input ())
for tc in range(t):
    n = int (input ())
    arr = list(map(int, input().split()))
    ob = Solution()
    print (ob.closestToZero (arr, n))
