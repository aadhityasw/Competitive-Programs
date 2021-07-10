class Solution:

    def recurse(self, A, stack) :

        if A == "" :
            self.ans.append(stack)
        
        temp_str = ""
        n = len(A)
        for i, ch in enumerate(A) :
            temp_str += ch
            if self.isPalindrome(temp_str) :
                self.recurse(A[i+1:], stack+[temp_str])


    def isPalindrome(self, string) :
        if string == string[::-1] :
            return True
        return False




    # @param A : string
    # @return a list of list of strings
    def partition(self, A):

        n = len(A)
        if n <= 1 :
            return [A]

        self.ans = []
        self.recurse(A, [])

        self.ans.sort()
        return self.ans
