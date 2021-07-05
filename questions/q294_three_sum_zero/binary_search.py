class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def threeSum(self, A):
        ans = []

        A.sort()
        n = len(A)

        #print(A)
        for i in range(n-2) :
            if i > 0 and A[i] == A[i-1] :
                continue

            j = i+1
            while j < n-1 :
                front = j+1
                rear = n-1
                num = -1*(A[i] + A[j])

                while front <= rear :
                    mid = (front + rear) // 2

                    if A[mid] == num :
                        ans.append((A[i], A[j], A[mid]))
                        break
                    elif A[mid] < num :
                        front = mid + 1
                    else :
                        rear = mid - 1
                
                val = A[j]
                while j < n-1 and A[j] == val :
                    j += 1
            
        return ans



A = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
ob = Solution()
print(ob.threeSum(A))
