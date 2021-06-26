#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def hashNum(n) :
    return n % 10000

def queensAttack(n, k, r_q, c_q, obstracles):
    #board = [[True for _ in range(n)] for _ in range(n)]
    #for x, y in obstacles :
    #    board[x-1][y-1] = False
    
    table = [[] for _ in range(10000 + 2)]
    for r, c in obstracles :
        table[int(hashNum(r))].append((r, c))
    
    count = 0
    
    # Left
    i = c_q-2
    while i >= 0 and ((r_q, i+1) not in table[int(hashNum(r_q))]) :
        count += 1
        i -= 1
    
    # Right
    i = c_q
    while i < n and (r_q, i+1) not in table[int(hashNum(r_q))]  :
        count += 1
        i += 1
    
    # Top
    i = r_q-2
    while i >= 0 and (i+1, c_q) not in table[int(hashNum(i+1))] :
        count += 1
        i -= 1
    
    # Bottom
    i = r_q
    while i < n and (i+1, c_q) not in table[int(hashNum(i+1))]  :
        count += 1
        i += 1
    
    # Top Left Diagonal
    i = r_q-2
    j = c_q-2
    while i >= 0 and j >= 0 and (i+1, j+1) not in table[int(hashNum(i+1))] :
        count += 1
        i -= 1
        j -= 1
    
    # Top Right Diagonal
    i = r_q-2
    j = c_q
    while i >= 0 and j < n and (i+1, j+1) not in table[int(hashNum(i+1))] :
        count += 1
        i -= 1
        j += 1
    
    # Bottom Left Diagonal
    i = r_q
    j = c_q-2
    while i < n and j >= 0 and (i+1, j+1) not in table[int(hashNum(i+1))] :
        count += 1
        i += 1
        j -= 1
    
    # Bottom Right Diagonal
    i = r_q
    j = c_q
    while i < n and j < n and (i+1, j+1) not in table[int(hashNum(i+1))] :
        count += 1
        i += 1
        j += 1
    
    # Return the count
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(tuple(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
