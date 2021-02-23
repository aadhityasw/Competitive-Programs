# Codechef : COVIDLQ
# COVID Pandemic and Long Queue 
# https://www.codechef.com/problems/COVIDLQ

test_cases = int(input())
for tes in range(test_cases) :
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    cost = 0
    ncount = 0
    flag = True
    for i in range(n) :
        if(arr[i] == 1) :
            if ncount == 0 :
                ncount += 1
                cost = 0
            elif cost >= 6 :
                cost = 0
                ncount += 1
            else :
                flag = False
                break
        cost += 1
    if flag :
        print("YES")
    else :
        print("NO")
