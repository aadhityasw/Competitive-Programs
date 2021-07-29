class Solution:
    def merge(self, arr1, arr2, n, m): 
        
        # Find the number of swaps needed
        num_swaps = 0
        i = 0
        j = 0
        while i+j < n and j < m :
            if arr1[i] < arr2[j] :
                i += 1
            else :
                j += 1
                num_swaps += 1
        
        # Swap the last `num_swaps` elements of array 1 with the first `num_swaps` elements of array 2
        i = n - num_swaps
        j = 0
        while j < num_swaps :
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1
        
        # Sort both the arrays individually
        arr1.sort()
        arr2.sort()



if __name__ == "__main__":         
    tc=int(input())
    while tc > 0:
        n, m=map(int, (input().strip().split()))
        arr1=list(map(int , input().strip().split()))
        arr2=list(map(int , input().strip().split()))
        ob = Solution()
        ob.merge(arr1, arr2, n, m)
        for x in arr1:
            print(x, end=" ")
        for x in arr2:
            print(x, end=" ")
        print()
        tc=tc-1
