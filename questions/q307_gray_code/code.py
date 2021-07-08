class Solution:

    def __init__(self) :
        self.store = []
    

    def recursiveTraverse(self, s, pos) :
        """
        Given a character array and a pos, changes bit in that position
        """

        if pos >= len(s) :
            return

        self.recursiveTraverse(s, pos+1)

        if s[pos] == '0' :
            s[pos] = '1'
        else :
            s[pos] = '0'
        
        self.store.append(int("".join(s),2))
        self.recursiveTraverse(s, pos+1)


    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):

        s = ['0']*A
        self.store.append(int("".join(s),2))
        self.recursiveTraverse(s, 0)

        return self.store
