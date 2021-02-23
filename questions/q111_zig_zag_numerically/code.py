class Solution:

    def zigZag(self,arr, n):
        
        i = 0
        while i < n-1 :
            if i % 2 and arr[i+1] >= arr[i] :
                arr[i], arr[i+1] = arr[i+1], arr[i]
            elif i % 2 == 0 and arr[i+1] <= arr[i] :
                arr[i], arr[i+1] = arr[i+1], arr[i]
            
            i += 1
