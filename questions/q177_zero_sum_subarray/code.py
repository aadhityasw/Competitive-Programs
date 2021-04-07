class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        #return: count of sub-arrays having their sum equal to 0

        store = {0:1}
        runningSum = 0
        count = 0

        for i in arr :
            runningSum += i
            if runningSum in store :
                count += store[runningSum]
                store[runningSum] += 1
            else :
                store[runningSum] = 1
        
        return count


if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
