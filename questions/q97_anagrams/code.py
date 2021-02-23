def isAnagram(a,b):
    a_dict = {}
    b_dict = {}
    
    for ch in a :
        if ch in a_dict :
            a_dict[ch] += 1
        else :
            a_dict[ch] = 1
    
    for ch in b :
        if ch in b_dict :
            b_dict[ch] += 1
        else :
            b_dict[ch] = 1
    
    if len(a_dict) != len(b_dict) :
        return False
    
    for ch in a_dict :
        if ch not in b_dict or b_dict[ch] != a_dict[ch] :
            return False
    return True


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
        a,b=map(str,input().strip().split())
        if(isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
