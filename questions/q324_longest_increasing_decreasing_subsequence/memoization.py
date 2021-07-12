class Solution:

    def forward(self, A, ind) :

        # If we are out of bounds, we return the current count
        if ind >= len(A) :
            return 0

        # If present in the store, we return it
        if self.forward_store[ind] is not None :
            return self.forward_store[ind]

        count = 0
        for i in range(ind) :
            if A[i] < A[ind] :
                count = max(
                    count,
                    self.forward(A, i)
                )
        
        count += 1
        self.forward_store[ind] = count
        return count


    def reverse(self, A, ind) :

        # If we are out of bounds, we return the current count
        if ind >= len(A) :
            return 0

        # If present in the store, we return it
        if self.reverse_store[ind] is not None :
            return self.reverse_store[ind]

        count = 0
        for i in range(ind+1, len(A)) :
            if A[i] < A[ind] :
                count = max(
                    count,
                    self.reverse(A, i)
                )
        
        count += 1
        self.reverse_store[ind] = count
        return count


	# @param A : tuple of integers
	# @return an integer
    def longestSubsequenceLength(self, A):
        
        n = len(A)
        self.forward_store = [None]*n
        self.reverse_store = [None]*n

        for i in range(n) :
            if self.forward_store[i] is None :
                self.forward(A, i)
            if self.reverse_store[i] is None :
                self.reverse(A, i)

        count = 0
        for i in range(n) :
            count = max(
                count,
                self.forward_store[i] + self.reverse_store[i] - 1
            )

        #print(self.forward_store)
        #print(self.reverse_store)
        return count
