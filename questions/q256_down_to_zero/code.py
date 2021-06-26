#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
total = 1000001
store = [-1] * total
store[0] = 0
for i in range(1, total) :
    if (store[i] == -1) or (store[i] > store[i-1]+1) :
        store[i] = store[i-1] + 1
    j = 1
    while (j <= i) and (i*j < total) :
        if (store[i*j] == -1) or (store[i*j] > store[i]+1) :
            store[i*j] = store[i] + 1
        j += 1


def downToZero(n):
    global store
    return store[n]

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
