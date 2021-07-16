class Solution:
    def __init__(self) :
        self.store = set()
        
    def recurse(self, arr, n, stack) :
        if n == len(arr) :
            self.store.add(tuple(stack))
            return
        
        self.recurse(arr, n+1, stack+[arr[n]])
        self.recurse(arr, n+1, stack)
    
    #Function to find all possible unique subsets.
    def AllSubsets(self, arr,n):
        
        arr.sort()
        self.recurse(arr, 0, [])
        
        self.store = list(self.store)
        self.store.sort()
        return self.store



if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        obj  = Solution()
        result = obj.AllSubsets(a,n)
        for i in range(len(result)):
            print("(",end="")
            size = len(result[i])
            for j in range(size-1):
                print(result[i][j],end=" ")
            if(size):
                print(result[i][size-1],end=")")
            else:
                print(")",end="")
        print()
