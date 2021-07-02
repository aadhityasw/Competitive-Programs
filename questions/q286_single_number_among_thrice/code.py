class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        res=0
        n=len(A)
        
        # Traverse for each bit position
        for i in range(0,32):
            
            sm=0
            # this is the mask, (3**bit_position)
            x=1<<i
            # Find the number of times this bit position has occured in the array numbers
            for j in range(0,n):
                if A[j]&x:
                    sm+=1
            # If the count of occurances is not a multiple of three, then the bit is set(1) in the number which occurs exactly once
            if sm%3:
                # We ensure that this bit is set in the result
                res=(res|x)
            
        # res will have all the bit positions 1 which have not occured in multiple of 3 times
        return res
