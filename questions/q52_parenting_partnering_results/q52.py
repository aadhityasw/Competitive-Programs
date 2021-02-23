#  Parenting Partnering Returns - Codejam Qualification Round 2020

T = int(input())
for test in range(1, T+1) :
    N = int(input())
    arr = []
    pos = []
    a = 0
    b = 0
    ans = [''] * N
    imp = False
    for i in range(N) :
        arr.append(list(map(int, input().strip().split(' '))))
        pos.append(i)
    for i in range(N):
        for j in range(0, N-i-1):
            if arr[j][0] > arr[j+1][0] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                pos[j], pos[j+1] = pos[j+1], pos[j]
    #print(arr)
    for i in range(N) :
        if arr[i][0] >= a :
            ans[pos[i]] =  "C"
            a = arr[i][1]
        elif arr[i][0] >= b :
            ans[pos[i]] =  'J'
            b = arr[i][1]
        else :
            imp = True
            break
    if imp :
        print('Case #' + str(test) + ': IMPOSSIBLE')
    else :
        print('Case #' + str(test) + ': ' + ''.join(ans))