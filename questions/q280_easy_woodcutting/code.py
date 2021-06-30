class Solution:

    def findCutLength(self, A, leng) :

        return sum([ele - leng if ele >= leng else 0 for ele in A])

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        front = 0
        rear = max(A)

        while front < rear :
            mid = (front + rear) // 2
            val = self.findCutLength(A, mid)
            if val > B :
                front = mid
            elif val == B :
                return mid
            else :
                rear = mid
            if front == rear-1 :
                if self.findCutLength(A, front) > B :
                    return front
                return rear
        
        return front
