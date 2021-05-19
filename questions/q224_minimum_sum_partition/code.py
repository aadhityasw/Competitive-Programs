class Solution:
    def minDiffernce(self, arr, n):
        
        if n == 1 :
            return arr[0]

        arr.sort()

        # Find the sum of elements in arr
        summ = sum(arr)
        # We are required to find a subset whose sum is closest to required
        required = summ / 2

        # Initialize the DP table
        table = [[0 for _ in range(int(required)+1)] for _ in range(n+1)]
        table[0][0] = 1

        # Fill the DP table
        for i in range(1, n+1) :
            for j in range(int(required) + 1) :
                table[i][j] = table[i-1][j] 
                if j >= arr[i-1] :
                    table[i][j] = table[i][j] or table[i-1][j - arr[i-1]]
        
        # Find the largest number from the DP table which can be formed by the subset
        i = int(required)
        while i > 0 :
            for j in range(n+1) :
                if table[j][i] == 1 :
                    num = int(2 * abs(required - i))
                    return num
            i -= 1

        return -1


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minDiffernce(arr, N)
        print(ans)
