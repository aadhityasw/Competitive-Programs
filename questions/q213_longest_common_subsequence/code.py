class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        """
        We follow the Rule :
        table[i][j] = maximum of {
            table[i-1][j]   # The top cell
            table[i-1][j] + (1 if the character in position (i-1) of s1 and (j-1) of s2 are equal else 0)
            table[i][j-1]   # The cell to the left
        }
        We also add an extra column and row of zeros to the front and top of the table to simplify calculations, and hence the (i-1) in s1[i-1] instead of s1[i] in the comparison and also the loop goes from 1 to (length + 1)
        """
        
        table = [[0 for _ in range(y+1)] for _ in range(x+1)]

        for i in range(1, x+1) :
            for j in range(1, y+1) :
                if s1[i-1] == s2[j-1] :
                    table[i][j] = max((table[i-1][j]), (1 + table[i-1][j-1]), (table[i][j-1]))
                else :
                    table[i][j] = max((table[i-1][j]), (table[i-1][j-1]), (table[i][j-1]))
       
            
        return table[-1][-1]



import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
