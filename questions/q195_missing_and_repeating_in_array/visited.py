"""
Uses the numbers as index and mark them to be visited, if any is already marked, then it is repeated, and if any is left unmarked aftertraversal, it is absent
"""

class Solution:
    def findTwoElement(self, arr, n): 

        for i in arr :
            if arr[abs(i)-1] < 0 :
                repeated = abs(i)
            else :
                arr[abs(i)-1] = -1 * arr[abs(i)-1]
        
        for i in range(n) :
            if arr[i] > 0 :
                absent = i+1
        
        return [repeated, absent]


if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
