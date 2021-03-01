def balanceHeaps():
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    Balance the two heaps size , such that difference is not more than one.
    '''
    global min_heap, max_heap
    
    while len(min_heap) - len(max_heap) > 1 :
        ele = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-1 * ele))
    
    while len(max_heap) - len(min_heap) > 1 :
        ele = -1 * heapq.heappop(max_heap)
        heapq.heappush(min_heap, ele)
    
    
def getMedian():
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    :return: return the median of the data received till now.
    '''
    global min_heap, max_heap
    
    if len(min_heap) == len(max_heap) :
        median = (min_heap[0] + (-1 * max_heap[0])) / 2
    elif len(min_heap) > len(max_heap) :
        median = min_heap[0]
    else :
        median = -1 * max_heap[0]

    #print(max_heap, min_heap)
    return int(median)
    
    
def insertHeaps(x):
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    :param x: value to be inserted
    :return: None
    '''
    global min_heap, max_heap

    if len(max_heap) > 0 and (-1 * max_heap[0]) > x :
        ele = -1 * heapq.heappushpop(max_heap, (-1 * x))
        heapq.heappush(min_heap, ele)
    else :
        heapq.heappush(min_heap, x)
    


import atexit
import io
import sys
import heapq
from collections import  defaultdict

min_heap = [] # our min heap to be used for upper half of data.
max_heap = [] # our max heap to be used for lower half of data.

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        for i in range(n):
            insertHeaps(int(input()))
            # call this function to balance the two heaps, such that
            # their size does not differ by more than 1.
            balanceHeaps()
            # prints the median
            print(getMedian())
