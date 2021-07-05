class Solution:

	# @param A : list of integers
	# @return an integer
    def cntBits(self, A):

        s = 0
        bit = 32

        while bit >= 0 :

            arr = [(num % (2**(bit+1))) // (2**bit) for num in A]
            num_ones = sum(arr)
            num_zeros = len(arr) - num_ones
            s = (s + (num_ones * num_zeros * 2)) % 1000000007
            #print(bit, s, freq)
            bit -= 1
        
        return s
