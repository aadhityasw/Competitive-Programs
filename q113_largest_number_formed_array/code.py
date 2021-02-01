class Solution() :
    def merge_sort(self, arr, f, r) :
        
        if f == r :
            return

        mid = (f + r) // 2
        if mid > f :
            self.merge_sort(arr, f, mid-1)
            self.merge_sort(arr, mid, r)
        
        a = 0
        b = 0
        if mid == f :
            copy1 = [arr[f]]
            copy2 = [arr[r]]
        else :
            copy1 = arr[f:mid]
            copy2 = arr[mid:r+1]
        pos = f

        while a < len(copy1) and b < len(copy2) :
            if int(str(copy1[a]) + str(copy2[b])) > int(str(copy2[b]) + str(copy1[a])) :
                arr[pos] = copy1[a]
                a += 1
            else :
                arr[pos] = copy2[b]
                b += 1
            pos += 1
        
        while a < len(copy1) :
            arr[pos] = copy1[a]
            a += 1
            pos += 1
        
        while b < len(copy2) :
            arr[pos] = copy2[b]
            b += 1
            pos += 1
        

    def printLargest(self,arr):

        n = len(arr)
        self.merge_sort(arr, 0, n-1)

        st = ''.join(arr)
        return st



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(arr)
        print(ans)
        tc -= 1
