class Solution:
	# @param A : integer
	# @return a strings
    def intToRoman(self, A):
        
        integers = [1000, 500, 100, 50, 10, 5, 1]
        romans = ["M", "D", "C", "L", "X", "V", "I"]

        num = A
        s = ""
        i = 0
        while i < 7 and num > 0 :
            
            digit = num // integers[i]
            if 0 < digit < 4 :
                s += romans[i]*digit
            elif digit == 4 :
                s += romans[i] + romans[i-1]
            elif digit == 5 :
                s += romans[i-1]
            elif 5 < digit < 9 :
                s += romans[i-1] + romans[i]*(digit - 5)
            elif digit == 9 :
                s += romans[i] + romans[i-2]
            
            num = num % integers[i]
            i += 2
        
        return s

