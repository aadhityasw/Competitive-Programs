class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        summ = 0
        n = len(A)
        table = {}

        max_leng = 0
        for i, num in enumerate(A) :
            if num == 0 :
                summ -= 1
            else :
                summ += 1
            
            if summ == 1 :
                max_leng = i+1
            
            if summ not in table :
                table[summ] = i
            
            if summ-1 in table :
                max_leng = max(max_leng, (i - table[summ-1]))
        
        return max_leng
