

class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr, n):

        max_prod = arr[0]
        min_val = arr[0]
        max_val = arr[0]
        
        for i in range(1, n) :
            if arr[i] < 0 :
                min_val, max_val = max_val, min_val
            
            min_val = min(arr[i], min_val * arr[i])
            max_val = max(arr[i], max_val * arr[i])
            
            max_prod = max(max_val, max_prod)

        return max_prod




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

