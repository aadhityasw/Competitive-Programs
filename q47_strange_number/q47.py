# Codechef : STRNO

"""testcase = int(input())
for tes in range(testcase) :
    x, k = map(int, input().strip().split(' '))
    p=1
    mainflag = False
    while True :
        xarr = []
        karr = []
        for i in range(1, p+1) :
            flag = True
            if p%i == 0 :
                for j in xarr :
                    if (i%j == 0 and j!=1) :
                        flag = False
                        break
                if flag == True and len(xarr) > 0:
                    karr.append(i)
                xarr.append(i)
        if len(xarr) == x and len(karr) == k :
            mainflag = True
            break
        p += 1
    if mainflag :
        print(1)
    else :
        print(0)"""

import math
testcase = int(input())
for tes in range(testcase) :
    x, k = map(int, input().split(' '))
    count = 0
    flag = False
    while x % 2 == 0: 
        x = x / 2
        count += 1
        if count >= k :
            flag = True
            break
    if flag == False :
        for i in range(3,int(math.sqrt(x))+1,2): 
            while x % i== 0: 
                x = x / i 
                count += 1
            if count >= k :
                flag = True
                break
    if x > 2 :
        count += 1
    if count >= k :
        print(1)
    else :
        print(0)