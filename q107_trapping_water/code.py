def trappingWater(arr,n):

    leftMax = 0
    rightMax = 0
    left = 0
    right = 0
    total = 0

    while left < right :

        leftMax = max(leftMax, arr[left])
        rightMax = max(rightMax, arr[right])

        if leftMax > rightMax :
            total += (rightMax - arr[right])
            right -= 1
        else :
            total += (leftMax - arr[left])
            left += 1
    
    return total
