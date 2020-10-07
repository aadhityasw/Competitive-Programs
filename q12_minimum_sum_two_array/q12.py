test = int(input())
for tes in range(test) :
    n = int(input())
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    a.sort()
    b.sort()
    summ = 0
    for i in range(n) :
        summ = summ + min(a[i], b[i])
    print(summ)