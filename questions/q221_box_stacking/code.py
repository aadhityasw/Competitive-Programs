class Solution:

    def formArray(self, height, width, length, n) :
        """
        Given the dimensions of the boxes, returns an array of all the possible combinations of the boxes by tilting.
        Each combination has max of 6 possibilities, and so the returned array will have maximum of 6*n elements, and will be sorted.
        Each element will be (area, length, width, height).
        """
        
        # Initialize the array
        arr = []

        # Fill the array
        for i in range(n) :
            # Width and Length is in the base
            arr.append(((width[i]*length[i]), max(length[i], width[i]), min(length[i], width[i]), height[i]))
            
            # Width and height is in the base
            if height[i] != length[i] :
                arr.append(((width[i]*height[i]), max(height[i], width[i]), min(height[i], width[i]), length[i]))

            # Length and height is in the base
            if height[i] != width[i] :
                arr.append(((height[i]*length[i]), max(length[i], height[i]), min(length[i], height[i]), width[i]))
        
        # Sort the array
        arr.sort()
        # Return the sorted array
        return arr
            

    def isLessThan(self, ele1, ele2) :
        """
        Takes two elements of the formed array, and returns True if `ele1 < ele2` based on the conditions.
        
        If `ele1 < ele2`, it means that `ele1` can be stacked on top of `ele2`.
        Each `ele` is (area, length, width, height).
        
        And Say ele1 < ele2 only if :
            ele1.area < ele2.area
            ele1.length < ele2.length
            ele1.width < ele2.width
        """

        if (ele1[0] < ele2[0]) and (ele1[1] < ele2[1]) and (ele1[2] < ele2[2]) :
            return True
        return False


    #Your task is to complete this function
    #Function should return an integer denoting the required answer
    def maxHeight(self,height, width, length, n):
        
        # Form the sorted array of all combinations of the boxes. Sorted in increasing order
        # Each element : (base_area, length, width, height)
        arr = self.formArray(height, width, length, n)
        num_combinations = len(arr)

        # Form the overall stacked_heights array
        stacked_height = [ele[3] for ele in arr]
        max_stacked_height = arr[0][3]

        # Loop through all combinations of boxes to find the right combination
        for i in range(1, num_combinations) :
            for j in range(i-1, -1, -1) :
                if self.isLessThan(arr[j], arr[i]) :
                    stacked_height[i] = max(stacked_height[i], (stacked_height[j] + arr[i][3]))
            max_stacked_height = max(max_stacked_height, stacked_height[i])
        
        # Return the maximum height that can be formed
        return max_stacked_height



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        i=0
        height=[]
        width=[]
        length=[]
        for i in range(0,3*n,3):
            height.append(arr[i])
            width.append(arr[i+1])
            length.append(arr[i+2])
        ob=Solution()
        print(ob.maxHeight(height, width, length, n))
