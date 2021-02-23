T = int(input())
for tes in range(T) :
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    summ = 0
    start = 0
    end = 0
    flag = False
    while True :
        if summ < s and end < n :
            summ += arr[end]
            end += 1
        elif summ > s and start <= end :
            summ -= arr[start]
            start += 1
        elif summ == s :
            flag = True
            break
        else :
            break
    if flag :
        print(start+1, end)
    else :
        print(-1)
