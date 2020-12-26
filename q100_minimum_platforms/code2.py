"""
In this we sort the arrival and the departure seperately, and then traverse through them simultaneously.
During the traversal, if the arrival is smaller or equal, we increment the number of platform and proceed,
otherwise, we decement the number of platforms and proceed.
During this at any point the maximum number of platforms obtained is our desired result.
"""


def minimumPlatform(n,arr,dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''

    arr.sort()
    dep.sort()

    i = 0
    j = 0

    count = 0
    res = 0
    while i < n and j < n :
        if arr[i] <= dep[j] :
            count += 1
            i += 1
        else :
            count -= 1
            j += 1
        res = max(res, count)
    
    return res



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
