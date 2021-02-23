def ispar(x):
    open_bracket = ['{', '[', '(']
    close_bracket = ['}', ']', ')']
    arr = []
    for ch in x :
        if ch in open_bracket :
            arr.append(ch)
        else :
            if len(arr) == 0 :
                return False
            if open_bracket[close_bracket.index(ch)] == arr[-1] :
                arr.pop(-1)
            else :
                return False
    if len(arr) != 0 :
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


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        s = str(input())
        if ispar(s):
            print("balanced")
        else:
            print("not balanced")
