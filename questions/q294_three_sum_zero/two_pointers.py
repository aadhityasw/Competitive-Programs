class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def threeSum(self, A):
        ans = set()

        A.sort()
        n = len(A)

        for i in range(n-2) :
            front = i+1
            rear = n-1

            while front < rear :
                cur_sum = A[i] + A[front] + A[rear]

                if cur_sum == 0 :
                    ans.add((A[i], A[front], A[rear]))
                    front += 1
                elif cur_sum < 0 :
                    front += 1
                else :
                    rear -= 1
            
        ans = list(ans)
        ans.sort()
        return ans
