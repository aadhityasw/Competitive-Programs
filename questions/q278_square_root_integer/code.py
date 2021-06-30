class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):

        front = 0
        end = A
        mid = 0
        while front < end :
            mid = (front + end) // 2
            #print(front, end, mid)
            if mid**2 > A :
                end = mid
            elif mid**2 == A :
                return mid
            else :
                front = mid
            if front == end - 1 :
                if end**2 == A :
                    return end
                return front
            
        return mid
