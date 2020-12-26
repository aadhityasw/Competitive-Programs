"""
In this, we use the point that time in a single day spans for only 24 hours, and thus by the problem, 
we can have values from 0 till 2360.

We use this point to traverse through the arrival and departure as in the previous code `code2.py` and 
follow a similar increment and decrement operations.
"""


def minimumPlatform(n,arr,dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''
    
    plat = [0] * 2361

    for i in range(n) :
        plat[int(arr[i])] += 1
        # Because only after the departure, the next minute can another train arrive.
        plat[int(dep[i]) + 1] -= 1

    count = 0
    ma = 0
    for i in range(2361) :
        count += plat[i]
        ma = max(ma, count)
    
    return ma



import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(str,input().strip().split()))
        departure = list(map(str,input().strip().split()))
        print(minimumPlatform(n,arrival,departure))
