class Solution:
    def __init__(self) :
        self.foundSplit = False
    
    def search(self, A : list, l : int, h : int, key : int):
        
        # Find the place where the sorted array starts
        if self.foundSplit == False :
            self.foundSplit = True
            
            if A[0] >= A[h-1] :
                i = h
                while i > 0 and A[i] > A[i-1] :
                    i -= 1
                split_point = i
            
                if key >= A[0] :
                    return self.search(A, l, split_point, key)
                else :
                    return self.search(A, split_point+1, h, key)
            else :
                return self.search(A, l, h, key)
            
        else :
            
            if l > h :
                return -1
            
            mid = (l + h) // 2
            if key > A[mid] :
                return self.search(A, mid+1, h, key)
            elif key < A[mid] :
                return self.search(A, l, mid-1, key)
            else :
                return mid




if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
