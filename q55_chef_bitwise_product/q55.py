# Codechef - CHANDF

# Incomplete

import math

testc = int(input())
for tes in range(testc) :
    (x, y, l, r) = map(int, input().strip().split(' '))
    if x==0 or y==0 or r==0 or l==r :
        print(l)
    elif r == 1 :
        print((x|y)&r)
    elif l <= (x|y) <= r :
        print(x|y)
    else :
        """maxi = 0
        v = 0
        for i in range(l, r+1) :
            res = (x&i) * (y&i)
            if res > maxi :
                maxi = res
                v = i
        print(v)"""
        if (r&max(x, y)|min(x,y)) <= r :
            print(r&max(x, y)|min(x,y))
        else :
            num1 = r&(x|y)
            num2= int(math.floor(math.log2(r)))
            num2 = ((pow(2, num2)) - 1)&(x|y)
            res1 = (x&num1) * (y&num1)
            res2 = (x&num2) * (y&num2)
            if res1 > res2 :
                print(num1)
            elif res2 > res1 :
                print(num2)
            else :
                print(min(num1, num2))