class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        num = 0

        while i < len(s) and s[i] == ' ' :
            i += 1
        
        sign = 1
        if i < len(s) and s[i] == '-' :
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+' :
            sign = 1
            i += 1
        
        while i < len(s) and 48 <= ord(s[i]) <= 57 :
            num = num*10 + ord(s[i])-48
            i += 1
            if sign == 1 and num > (2**31 - 1) :
                return (2**31 - 1)
            elif sign == -1 and num > (2**31) :
                return -1*(2**31)
        
        return num*sign
