class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)

        for i in range(n) :
            j = n-1
            while (height[i]*(j-i) > max_area) :
                if min(height[i], height[j])*(j-i) > max_area :
                    max_area = min(height[i], height[j])*(j-i)
                j -= 1
        
        return max_area
