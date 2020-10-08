#      Vestigium      Google -  Qualification Round 2020 - Code Jam 2020


T = int(input())
for test in range(1, T+1) :
    N = int(input())
    arr = []
    for i in range(N) :
        arr.append(list(map(int, input().strip().split(' '))))
    row = [[] for _ in range(N)]
    col = [[] for _ in range(N)]
    r=0
    c=0
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] in row[i] :
                r += 1
                break
            else :
                row[i].append(arr[i][j])
    for i in range(N) :
        for j in range(N) :
            if arr[j][i] in col[i] :
                c += 1
                break
            else :
                col[i].append(arr[j][i])
    tr=0
    for i in range(N) :
        tr += arr[i][i]
    print('Case #' + str(test) + ': ' + str(tr) + ' ' + str(r) + ' ' + str(c))