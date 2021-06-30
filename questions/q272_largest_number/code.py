import functools

class Solution:

    def compareFunc(self, a, b) :
        if int(str(a) + str(b)) < int(str(b) + str(a)) :
            return 1
        elif int(str(a) + str(b)) == int(str(b) + str(a)) :
            return 0
        else :
            return -1

    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):

        answer = "".join([str(i) for i in sorted(A, key=functools.cmp_to_key(self.compareFunc))])
        while len(answer) > 1 and answer[0] == '0' :
            answer = answer[1:]
        
        return answer
