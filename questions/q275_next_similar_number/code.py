class Solution:

    def findPos2(self, A, num) :
        """
        Given a string of digits and another digit as a character, finds the position of the digit equal or greater than itself.
        """

        n = len(A)

        i = n-1
        while i >= 0 :
            if A[i] > num :
                return i
            i -= 1
        
        return -1
    

    def appendProperly(self, string, ele) :
        """
        Given a string of digits in sorted order, appends another digit at its appropriate position, and returns the string.
        """

        n = len(string)

        i = 0
        while i < n :
            if string[i] > ele :
                answer = string[:i] + ele + string[i:]
                return answer
            i += 1
        
        return string + ele
        


    # @param A : string
    # @return a strings
    def solve(self, A):

        n = len(A)

        i = n-1
        ma = None
        while i >= 0 :
            if ma is None :
                ma = A[i]
            else :
                new_ma = max(ma, A[i])
                if A[i] < ma :
                    pos1 = i
                    pos2 = self.findPos2(A, A[pos1])
                    right = (A[pos1+1:pos2] + A[pos2+1:])[::-1]
                    right_final = self.appendProperly(right, A[pos1])
                    answer = A[:pos1] + A[pos2] + right_final
                    return answer
                ma = new_ma
            i -= 1
        
        return "-1"


A = "740948824551711527614232216857618927954312"
#A = "903885770893074783710083450145620356667677191627276513995926532"
#A = "892795"
#A = "551"
ob = Solution()
print(ob.solve(A))
