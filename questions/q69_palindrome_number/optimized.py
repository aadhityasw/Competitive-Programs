class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0) :
            return False

        num = x
        reversed = 0
        while num > 0 :
            reversed = reversed*10 + num%10
            num = num // 10
        
        if reversed == x :
            return True
        else :
            return False
