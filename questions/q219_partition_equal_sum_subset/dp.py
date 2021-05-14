class Solution:
    def equalPartition(self, N, arr):

        # Find the sum of the array
        summ = sum(arr)

        # If the sum is odd, then return false
        if summ % 2 != 0 :
            return 0
        
        # This is the number we need to obtain during the computation
        required = summ // 2

        # Form the DP table
        table = [[False for _ in range(N+1)] for _ in range(required+1)]

        for i in range(N+1) :
            table[0][i] = True
        
        for i in range(1, required+1) :
            for j in range(1, N+1) :
                # We keep the sum same and not remove the jth element in arr
                table[i][j] = table[i][j-1]

                if arr[j-1] <= i :
                    # We reduce the sum and find the remaining in the interval till one less than j
                    table[i][j] = table[i][j] or table[i - arr[j-1]][j-1]
        
        if table[required][N] :
            return 1
        else :
            return 0


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
