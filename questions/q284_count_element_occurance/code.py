class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        
        def search(A, B, searchFirst = True):
            low = 0
            high = len(A) - 1
            result = -1
            while low <= high:
                mid = low + (high-low)//2
                if A[mid] == B:
                    result = mid
                    if searchFirst:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif A[mid] < B:
                    low = mid + 1
                else:
                    high = mid - 1
            return result
            
        first = search(A,B)
        last = search(A,B,False)
        if first == -1:
            return 0
        else:
            return last-first+1
