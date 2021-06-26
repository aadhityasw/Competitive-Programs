#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def isSorted(arr) :
    n = len(arr)
    for i in range(n-1) :
        if arr[i] > arr[i+1] :
            return False
    return True

def almostSorted(arr):
    
    if isSorted(arr) :
        print("yes")
        return
    
    n = len(arr)
    for i in range(n-1) :
        if arr[i] > arr[i+1] :
            prob = i
            break
    
    # Check for swap operation
    swap = False
    pt = n-1
    for j in range(prob+1, n) :
        if arr[j] >= arr[prob] :
            pt = j-1
            break
    temparr = arr[:]
    temparr[prob], temparr[pt] = temparr[pt], temparr[prob]
    if isSorted(temparr) :
        swap = True
        swap_coord = (prob+1, pt+1)
    
    if swap :
        print("yes")
        print("swap", swap_coord[0], swap_coord[1])
        return
    
    # Check for reverse operation
    reverse = False
    pt = n-1
    for j in range(prob, n-1) :
        if arr[j] < arr[j+1] :
            pt = j
            break
    temparr = arr[:]
    temparr[prob:pt+1] = temparr[prob:pt+1][::-1]
    #print(temparr[prob:pt+1][::-1])
    if isSorted(temparr) :
        reverse = True
        reverse_coord = (prob+1, pt+1)
    
    if reverse :
        print("yes")
        print("reverse", reverse_coord[0], reverse_coord[1])
        return
    
    print("no")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
