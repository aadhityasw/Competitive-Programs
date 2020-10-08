# Codechef  :  CARSELL
# https://www.codechef.com/problems/CARSELL
# Sell All the Cars

test = int(input())
for tes in range(test) :
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    arr.sort()
    j=n-1
    summ = 0
    for i in range(n) :
        numm = arr[i] - j
        if numm > 0 :
            summ = ((numm + summ)%1000000007)
        j-=1
    print(summ)
