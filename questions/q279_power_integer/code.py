class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x == 0 or d < 2 :
            return 0
        
        if n == 0 :
            return 1
        
        if x < 0 :
            x += d
        x = x % d
        power = n
        ans = 1
        for ch in bin(power)[2:] :
            ans = ans**2 % d
            if ch == '1' :
                ans = ans*x % d
        
        return ans
        
            