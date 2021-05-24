class Solution:
    def smallestWindow(self, s, p):

        # Form a board for p, and also get the number of unique characters in p
        p_board = [0] * 256
        num_p_unique = 0
        for i in p :
            p_board[ord(i)] += 1
            if p_board[ord(i)] == 1 :
                num_p_unique += 1
        
        s_board = [0] * 256
        count = 0
        window_start = 0
        start = 0
        min_length = len(s) + 1

        for i in range(len(s)) :

            s_board[ord(s[i])] += 1
            # Gets count of all the unique characters of p that are present in the window in full capacity
            if (p_board[ord(s[i])] > 0) and (s_board[ord(s[i])] == p_board[ord(s[i])]) :
                count += 1
            
            if count == num_p_unique :
                # Minimize the window
                while (s_board[ord(s[window_start])] > p_board[ord(s[window_start])]) or (p_board[ord(s[window_start])] == 0) :
                    s_board[ord(s[window_start])] -= 1
                    window_start += 1
                
                # Update the min_length, so that it stays minimum of all windows found
                if (i - window_start + 1) < min_length :
                    start = window_start
                min_length = min(min_length, (i - window_start + 1))

        if min_length > len(s) :
            return "-1"
        
        return  s[start : start+min_length]


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
        ob = Solution()
        print(ob.smallestWindow(s,p))
