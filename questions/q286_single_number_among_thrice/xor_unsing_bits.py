class Solution:

    def xorBaseThree(self, a, b) :
        """
        Given two numbers returns their xor base 3
        """

        ans = 0
        power = 0
        while a > 0 or b > 0 :
            ans += ((3**power) * (((a%3) + (b%3)) % 3))
            power += 1
            a = a // 3
            b = b // 3
        
        #print("XOR", a, b, ans)
        return ans
        

    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):

        res = None
        for num in A :
            if res is None :
                res = num
            else :
                res = self.xorBaseThree(res, num)
            #print(res)
        
        return res
        