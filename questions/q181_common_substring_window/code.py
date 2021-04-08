class Solution:
    def smallestWindow(self, s, p):

        p_board = [0] * 256
        for i in p :
            p_board[ord(i)] += 1
        
        s_board = [0] * 256
        count = 0
        window_start = 0
        start = 0
        min_length = len(s) + 1

        for i in range(len(s)) :

            s_board[ord(s[i])] += 1
            if (p_board[ord(s[i])] > 0) and (s_board[ord(s[i])] == p_board[ord(s[i])]) :
                count += 1
            
            if count == len(p) :
                # Minimize the window

                while (s_board[ord(s[window_start])] > p_board[ord(s[window_start])]) or (p_board[ord(s[window_start])] == 0) :
                    if (s_board[ord(s[window_start])] > p_board[ord(s[window_start])]) and (p_board[ord(s[window_start])] != 0) :
                        s_board[ord(s[window_start])] -= 1
                    window_start += 1
                
                if (i - window_start + 1) < min_length :
                    start = window_start
                min_length = min(min_length, (i - window_start + 1))

        if min_length > len(s) :
            return "-1"
        
        return  s[start : start+min_length]
