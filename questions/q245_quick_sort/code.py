
class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        
        if low < high :
            pt = self.partition(arr, low, high)

            self.quickSort(arr, low, pt-1)
            self.quickSort(arr, pt+1, high)
    

    def partition(self,arr,low,high):

        pos = low-1
        pivot = high

        for i in range(low, high) :
            if arr[i] <= arr[pivot] :
                pos += 1
                arr[pos], arr[i] = arr[i], arr[pos]
        
        arr[pivot], arr[pos+1] = arr[pos+1], arr[pivot]
        return pos+1



if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
