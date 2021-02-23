class Solution:
    def reverse(self, x: int) -> int:
        if x > 0 :
            sign = 1
        else :
            sign = -1
            x = x * -1
        
        rev = 0
        while (x > 0) :
            a = x % 10
            x = x // 10
            rev = rev*10 + a
        
        rev = rev * sign
        if ((-2)**31) <= rev < (2**31) :
            return rev
        else :
            return 0
