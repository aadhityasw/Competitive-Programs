"""
@aadhityasw

Uses sum of numbers and sub of squares to solve a system of linear equations to derrive the answers.

y -> Missing number
x -> Repeated number

S + x = sum of `arr`
S + y = sum of first `n` natural numbers  =  `n*(n+1)/2`
Get `x - y` from this -- (1)

S^2 + x^2 = sum of square of elements of `arr`
S^2 + y^2 = sum of squares of first `n` natural numbers = `n*(n+1)*(2*n+1)/6`
Get `x^2 - y^2` from this -- (2)

Divide (2) by (1) to get `x + y` -- (3)

Use equations (1) and (3) to get `x` and `y`
"""

class Solution:
    def findTwoElement( self,arr, n): 
        
        x_minus_y = sum(arr) - (n*(n+1)/2)

        x_2_minus_y_2 = int(sum([i**2 for i in arr]) - (n*(n+1)*(2*n+1)/6))

        x_plus_y = int(x_2_minus_y_2 / x_minus_y)

        x = int((x_plus_y + x_minus_y) / 2)
        y = x_plus_y - x

        return [x, y]


if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
