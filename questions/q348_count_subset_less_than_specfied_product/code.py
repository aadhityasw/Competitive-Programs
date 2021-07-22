class Solution:
    def numOfSubsets(self, arr, N, K):
        
        table = [[0 for _ in range(K+1)] for _ in range(N+1)]
        
        for i in range(1, N+1) :
            for j in range(1, K+1) :
                if arr[i-1] <= j :
                    table[i][j] += table[i-1][j//arr[i-1]] + 1
                table[i][j] += table[i-1][j]
        
        return table[N][K]



if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        K=int(input())
        
        ob = Solution()
        print(ob.numOfSubsets(arr,N,K))
