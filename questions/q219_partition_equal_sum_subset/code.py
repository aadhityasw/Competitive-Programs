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
        table = [0 for _ in range(required+1)]

        for i in range(N) :
            # Loop to cover all numbers above `arr[i]` and below `required`
            for j in range(required, arr[i], -1) :
                # If the (j - arr[i]) cost can be formed, then by including arr[i], we can form the sum j 
                if table[j - arr[i]] :
                    table[j] = True
            # If the current element is less than required, then it can help in forming required
            if arr[i] <= required :
                table[arr[i]] = True

            # Early return for better efficiency
            if table[required] :
                return 1
        
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
