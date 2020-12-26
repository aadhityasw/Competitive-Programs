"""
We sort all the trains based on their arrival times and then parse through the list once keeping
in mind the longest departure and its arrival and finding the clashed on the way.
"""


def sortArrays(n, arr, dep) :
    """
    Given the arrival and the departure times, we sort these arrays simultaneously in place.
    """
    for i in range(n-1) :
        for j in range(n-i-1) :
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                dep[j], dep[j+1] = dep[j+1], dep[j]


def minimumPlatform(n,arr,dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''

    sortArrays(n, arr, dep)

    i = 0
    j = 1
    ma = 0

    while j < n :
        if dep[j] <= dep[i] :
            j += 1
        else :
            if arr[j] <= dep[i] :
                j += 1
            else :
                if ma < (j-i) :
                    ma = j-i
                i = j
                j += 1
    
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
