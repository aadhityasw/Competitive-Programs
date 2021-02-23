class Solution:    
    def reverseInGroups(self, arr, N, K):
        i = 0
        while i < N :
            if i + K < N :
                nextPos = i + K
                j = i + K - 1
            else :
                nextPos = N
                j = N - 1
                
            while i < j :
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
                j -= 1
                
            i = nextPos



import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()
