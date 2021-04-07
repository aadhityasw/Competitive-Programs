class Solution:
    '''
        Your task is to  find the character in p that
        is present at the minimum index in string s.
        
        Function Arguments: s and p (given strings)
        Return Type: char or string
    
    '''
    
    def minIndexChar(self,stri, pat): 
        
        table = [0]*26
        
        for i in pat :
            table[ord(i)-97] += 1
            
        for i in range(len(stri)) :
            if table[ord(stri[i])-97] > 0 :
                return i
        return -1





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
        s=str(input())
        p=str(input())
        obj = Solution()
        ans = obj.minIndexChar(s,p)
        if(ans == -1):
            print("No character present")
        else:
            print(s[ans])
