class Solution:
    def longestPalindrome(self, s: str) -> str:
        window = ""
        length = len(s)
        while length > 0 :
            window = s[:length]
            if window == window[::-1] :
                return window
            for i in range(length, len(s)) :
                window = window[1:] + s[i]
                if window == window[::-1] :
                    return window
            length -= 1
