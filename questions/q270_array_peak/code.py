class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        n = len(A)

        left = [0] * n
        right = [0] * n

        left[0] = A[0]
        right[n-1] = A[n-1]

        for i in range(1, n) :
            left[i] = max(left[i-1], A[i])
        for i in range(n-2, -1, -1) :
            right[i] = min(right[i+1], A[i])
        
        for i in range(1, n-1) :
            if A[i] > left[i-1] and A[i] < right[i+1] :
                return 1
        
        return 0



A = [ 5706, 26963, 24465, 29359, 16828, 26501, 28146, 18468, 9962, 2996, 492, 11479, 23282, 19170, 15725, 6335 ]
ob = Solution()
print(ob.perfectPeak(A))
