class Solution:
    def canRepresentBST(self, arr, N):
        
        stack = []
        root = float("-inf")
        
        for i in range(N) :
            
            if arr[i] < root :
                return 0
            
            while len(stack) > 0 and stack[-1] < arr[i] :
                root = stack.pop()
            
            stack.append(arr[i])
        
        return 1


import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.canRepresentBST(arr, N))
