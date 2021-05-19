"""
This solution  uses O(n) space.
"""


class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        arr = [1, 1, 2]

        for i in range(3, n+1) :
            arr.append((arr[i-1] + arr[i-2] + arr[i-3]) % 1000000007)
        
        return arr[n]


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
