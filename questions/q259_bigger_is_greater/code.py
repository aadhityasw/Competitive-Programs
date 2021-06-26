#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    n = len(w)
    
    found = None
    for i in range(n-1, -1, -1) :
        limit = -1 if found is None else found[0]
        for j in range(i-1, limit, -1) :
            if w[i] > w[j] :
                found = (j, i)
                break
    if found is None :
        w = "no answer"
    else :
        remaining = "".join(sorted(w[found[0]+1:found[1]] + w[found[0]] + w[found[1]+1:]))
        w = w[:found[0]] + str(w[found[1]]) + remaining
    
    return w

    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
