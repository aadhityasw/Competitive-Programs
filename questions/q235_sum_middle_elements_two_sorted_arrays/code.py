class Solution:
	def findMidSum(self, ar1, ar2, n): 
	    
	    arr = sorted(ar1 + ar2)
	    return arr[n-1] + arr[n]


if __name__ == "__main__":         
    tc=int(input())
    while tc > 0:
        n=int(input())
        ar1=list(map(int, input().strip().split()))
        ar2=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMidSum(ar1, ar2, n)
        print(ans)
        tc=tc-1
