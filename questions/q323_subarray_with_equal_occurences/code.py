class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        table = {}

        summ = 0
        count = 0
        for i, num in enumerate(A) :
            if num == B :
                summ += 1
            elif num == C :
                summ -= 1
            
            if summ in table :
                table[summ] += 1
            else :
                table[summ] = 1
            
            # If summ is not zero, then we should not include the current position in the count
            count += table[summ]
            if summ != 0 :
                count -= 1
            

        return count
