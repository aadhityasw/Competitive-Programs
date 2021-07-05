class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        # Initialize the pointers
        front = -1
        rear = -1
        n = len(A)

        # Perform the requiresd steps until the rear pointer is within the dimensions of the array
        while rear < n-1 and B > 0:
            if A[rear+1] == 1 :
                rear += 1
            elif A[rear+1] == 0 and B > 0 :
                rear += 1
                B -= 1
        #print(rear)
            
        if rear == n-1 :
            return n
        
        max_count = rear-front
        while rear < n-1 :
            #print(front, rear)
            while rear < n-1 and A[rear+1] == 1 :
                rear += 1
            max_count = max(max_count, rear-front)
            while A[front+1] == 1 and front < rear :
                front += 1
            front += 1
            rear += 1
        
        return max_count
