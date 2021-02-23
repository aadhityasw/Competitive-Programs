class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        window = []
        max_count = 0
        for ch in s :
            if ch in window :
                while window[0] != ch :
                    window = window[1:]
                window = window[1:]
            window.append(ch)
            if len(window) > max_count :
                max_count = len(window)
        return max_count
