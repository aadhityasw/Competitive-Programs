def isRotated(s,p):
    #code here
    if len(s) < 2 :
        if s == p :
            return 1
        return 0
    res = s[2:] + s[:2]
    res1 = s[-2:] + s[:-2]
    if res == p or res1 == p :
        return 1
    return 0



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
        if(isRotated(s,p)):
            print(1)
        else:
            print(0)
