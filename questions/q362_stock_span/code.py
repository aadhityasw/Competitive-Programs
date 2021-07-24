class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        
        
        stack = [-1]
        ans = []
        for i in range(n) :
            
            pos = i
            while len(stack) > 1 :
                if a[stack[-1]] <= a[i] :
                    stack.pop()
                    pos = stack[-1] + 1
                else :
                    break
            
            ans.append(i - pos + 1)
            stack.append(i)
        
        return ans
            
            
            
            
            
            
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

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        obj = Solution()
        ans = obj.calculateSpan(a, n)
        print(*ans)
