"""
In the previous solution, we can notice that to get the value for i'th position, only its previous 3 values are used.
So this question can be solved by just an array of 3 elements, and thus of constant space complexity (O(1))
"""

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        arr = [1, 1, 2]
        
        for i in range(3, n+1) :
            arr[i % 3] = (arr[(i-1)%3] + arr[(i-2)%3] + arr[(i-3)%3]) % 1000000007
        
        return arr[n % 3]


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
