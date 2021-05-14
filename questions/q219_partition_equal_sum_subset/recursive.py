class Solution:

    def recursiveSearch(self, summ, n) :

        if summ == self.required or summ == 0  :
            return 1
            
        if n < 0 :
            return 0

        if self.visited[summ][n] :
            return 0
        
        self.visited[summ][n] = True

        return (
            self.recursiveSearch(summ, n-1) or
            self.recursiveSearch((summ - self.arr[n]), n-1) if summ > self.arr[n] else False
        )


    def equalPartition(self, N, arr):

        self.arr = arr

        # Find the sum of the array
        summ = sum(arr)

        # If the sum is odd, then return false
        if summ % 2 != 0 :
            return 0
        
        # This is the number we need to obtain during the computation
        self.required = summ // 2

        # Form the DP table
        self.visited = [[False for _ in range(N)] for _ in range(summ+1)]

        # Perform a Recursive search
        return self.recursiveSearch(summ, N-1)


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
