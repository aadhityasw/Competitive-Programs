class Solution:

    def recurse(self, n, stack, cur_open) :
        if n == 0 :
            self.ans.append(stack+')'*cur_open)
            return
        
        for i in range(cur_open+1) :
            self.recurse(n-1, stack+(')'*i)+'(', cur_open-i+1)



	# @param A : integer
	# @return a list of strings
    def generateParenthesis(self, A):

        if A <= 0 :
            return []
        
        self.ans = []
        self.recurse(A, "", 0)
        
        return self.ans
