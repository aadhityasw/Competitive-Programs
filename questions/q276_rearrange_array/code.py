class Solution:

    def get(self, A, n, i) :
        return A[i] % n

    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):

        n = len(A)
        for i in range(n) :
            original_number = self.get(A, n, i)
            A[i] = (self.get(A, n, original_number) * n) + original_number
        
        for i in range(n) :
            A[i] = A[i] // n
        return A
