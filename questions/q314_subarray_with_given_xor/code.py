class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        count = 0
        current_xor = 0
        n = len(A)
        table = {0 : 1}

        for i, num in enumerate(A) :
            current_xor = current_xor ^ num
            if current_xor ^ B in table :
                count += table[current_xor ^ B]
            if current_xor in table :
                table[current_xor] += 1
            else :
                table[current_xor] = 1
        
        return count

        