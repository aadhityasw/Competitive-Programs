
"""
                            Not Working
"""


class Solution:

    def calcLineProp(self, p1, p2) :
        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2 :
            m = float("inf")
            c = x1
        elif y1 == y2 :
            m = 0
            c = y1
        else :
            m = (y2 - y1) * 1.0 / (x2 - x1)
            c = (y1 * 1.0 / (y2 - y1)) - (x1 * 1.0 / (x2 - x1))

        #print(p1, p2, m, c)
        m = round(m, 2)
        c = round(c, 2)
        return (m, c)



    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):

        table = {}
        n = len(A)

        if n == 1 :
            return 1

        for i in range(n) :
            for j in range(i+1, n) :
                line_prop = self.calcLineProp((A[i], B[i]), (A[j], B[j]))
                if line_prop in table :
                    table[line_prop].add(i)
                    table[line_prop].add(j)
                else :
                    table[line_prop] = {i, j}
        
        #print(table)
        max_len = 0
        for v in table.values() :
            max_len = max(max_len, len(list(v)))
        return max_len
