"""
For each train, we check all the other trains to check how many collide, and we choose the case
where there is maximum collision.
"""


def minimumPlatform(n,arr,dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''
    ma = 0
    for i in range(n) :
        clash = 1
        for j in range(n) :
            if i != j :
                if (arr[i] <= arr[j] <= dep[i]) or (arr[i] <= dep[j] <= dep[i]) or ((arr[i] >= arr[j]) and (dep[i] <= dep[j])) :
                    clash += 1
        if clash > ma :
            ma = clash
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
