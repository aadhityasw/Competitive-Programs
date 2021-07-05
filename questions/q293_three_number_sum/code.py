class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):

        A.sort()
        n = len(A)

        min_diff = float("inf")
        closest_value = float("inf")

        for i in range(n-2) :
            front = i+1
            rear = n-1

            while front < rear :
                cur_sum = A[i] + A[front] + A[rear]

                if cur_sum == B :
                    return cur_sum
                
                if abs(B - cur_sum) < min_diff :
                    min_diff = abs(B - cur_sum)
                    closest_value = cur_sum
                
                if cur_sum < B :
                    front += 1
                else :
                    rear -= 1
            
        return closest_value
