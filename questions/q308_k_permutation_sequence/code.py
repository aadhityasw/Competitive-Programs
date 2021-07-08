class Solution:

    def recurse(self, available_digits, k) :
        if k == 0 :
            return "".join([str(i) for i in available_digits])
        n = len(available_digits)
        pos = (k // self.factorial[n-1])
        ans = str(available_digits.pop(pos))

        ans += self.recurse(available_digits, k%self.factorial[n-1])
        return ans


	# @param A : integer
	# @param B : integer
	# @return a strings
    def getPermutation(self, A, B):

        n = A
        k = B
        self.factorial = [1]
        prod = 1
        for i in range(1, n) :
            prod *= i
            self.factorial.append(prod)
        
        available_digits = [dig for dig in range(1, n+1)]
        ans = self.recurse(available_digits, k-1)
        return ans
