class Solution:
    
    def recursiveFind(self, arr, front, rear) :
        if front > rear :
            return
        mid = (front + rear) // 2
        if (mid > 0 and arr[mid-1] == arr[mid]) or (mid < len(arr)-1 and arr[mid+1] == arr[mid]) :
            left = self.recursiveFind(arr, front, mid-1)
            if left is None :
                return self.recursiveFind(arr, mid+1, rear)
            else :
                return left
        else :
            return arr[mid]
        
        return
        
        
    
    def findOnce(self,arr : list, n : int):
        
        return self.recursiveFind(arr, 0, n)


if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))
