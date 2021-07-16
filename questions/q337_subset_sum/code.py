class Solution:
    def isSubsetSum (self, N, arr, summ):
        
        store = [[None for _ in range(summ+1)] for _ in range(N+1)]
        
        for i in range(summ+1) :
            store[0][i] = False
        for i in range(N+1) :
            store[i][0] = True
        
        for i in range(1, N+1) :
            for j in range(1, summ+1) :
                if arr[i-1] <= j :
                    store[i][j] = store[i-1][j] or store[i-1][j-arr[i-1]]
                else :
                    store[i][j] = store[i-1][j]
        
        return store[N][summ]


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
