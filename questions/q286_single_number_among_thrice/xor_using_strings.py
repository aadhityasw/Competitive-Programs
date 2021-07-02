class Solution:

    def __init__(self) :
        self.store_base3 = {}


    def convertToBaseThree(self, n) :
        """
        Given a number returns its base 3 format
        """
        if n in self.store_base3 :
            return self.store_base3[n]

        s = ""
        num = n

        while num > 0 :
            a = num % 3
            s = str(a) + s
            num = num // 3

        self.store_base3[n] = s
        
        #print("base conversion", n, s)
        return s
    

    def xorBaseThree(self, a, b) :
        """
        Given two base 3 strings, returns its XOR to base 3
        """

        s = ""

        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 :
            if i >= 0 and j >= 0 :
                temp = (int(a[i]) + int(b[j])) % 3
            elif i >= 0 :
                temp = int(a[i])
            else :
                temp = int(b[j])
            s = str(temp) + s
            i -= 1
            j -= 1
        
        #print("XOR", a, b, s)
        return s


    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):

        res = ""
        for num in A :
            if res == "" :
                res = self.convertToBaseThree(num)
            else :
                res = self.xorBaseThree(res, self.convertToBaseThree(num))
        
        res = int(res, 3)
        return res
        
