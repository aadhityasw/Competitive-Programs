"""
This solution is similar to the egg drop problem.
Uses Binary search in that manner.
"""

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        x = 0
        base = 10**3
        while base>0:
            while (x+base)**2<=A: x+= base
            base //= 2
        return x
