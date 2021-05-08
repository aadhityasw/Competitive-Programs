import heapq


class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        heap = []

        for i in range(n) :
            heapq.heappush(heap, (end[i], start[i]))
        
        pos = 0
        count = 0
        while len(heap) > 0 :
            e, s = heapq.heappop(heap)
            if pos < s :
                count += 1
                pos = e
        
        return count


import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
