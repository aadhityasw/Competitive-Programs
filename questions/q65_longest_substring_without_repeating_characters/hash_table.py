class Solution:
	# @param A : string
	# @return an integer
    def lengthOfLongestSubstring(self, A):

        table = [0]*256
        n = len(A)

        front = 0
        rear = -1
        max_length = 1
        while rear < n-1 :
            while rear+1 < n and table[ord(A[rear+1])] == 0 :
                rear += 1
                table[ord(A[rear])] += 1
            
            max_length = max(max_length, (rear - front + 1))
            
            while front <= rear and rear < n-1 :
                table[ord(A[front])] -= 1
                front += 1
                if A[front-1] == A[rear+1] :
                    break
        
        return max_length
