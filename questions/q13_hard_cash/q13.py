"""https://www.codechef.com/FEB20B/problems/CASH"""

"""test = int(input())
for tes in range(test) :
    (n, k) = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    minCost = 999999
    cost = 0
    sets = 0
    for c in range(0, n) :
        cost += arr[c] % k
        sets += arr[c] // k
        i = c+1
        pcost = cost
        pset = sets
        f = True
        while i<n and f :
            if arr[i] % k != 0 :
                if (k-arr[i]%k) > pcost :
                    if pset == 0 :
                        f = False
                        break
                    else :
                        pset -= 1
                        pcost = pcost + (arr[i]%k)
                else :
                    pcost -= (k-arr[i]%k)
            pset += pcost // k
            pcost = pcost % k
            i += 1
        if pcost < minCost and f :
            minCost = pcost
    print(minCost)"""


test = int(input())
for tes in range(test) :
    (n, k) = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    brr = []
    backsum = 0
    for i in arr :
        a = k-(i%k)
        brr.append(a)
        backsum += a
    minCost = 99999
    fsum = 0
    for i in range(n) :
        fsum += arr[i]
        backsum -= brr[i]
        if backsum > fsum :
            continue
        else :
            a = fsum - backsum
            a = a%k
            if minCost > a :
                minCost = a
    print(minCost)
