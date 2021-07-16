
#                           Logic is correct, but code does not run


class Solution:
    def countKdivPairs(self, arr, n, k):
        
        freq = [0]*k
        
        for num in arr :
            freq[num % k] += 1
        
        # For zero remainder
        summ = freq[0] * (freq[0] - 1) / 2
        
        # For K / 2 value
        if k % 2 == 0 :
            summ += (freq[k // 2] * (freq[k // 2] - 1) // 2)
            end = k // 2
        else :
            end = (k // 2) + 1
        
        for i in range(1, end) :
            summ += (freq[i] * freq[k - i])
        
        return summ


import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = int(input())
        ob= Solution()
        print(ob.countKdivPairs(a,n,k))
