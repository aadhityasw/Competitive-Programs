def permut(arr, i, n, s) :
    s += arr[i]
    if len(s) == n :
        if s not in words :
            print(s, end=" ")
            words.append(s)
        return
    for j in range(n) :
        if arr[j] not in s :
            permut(arr, j, n, s)


T = int(input())
for tes in range(T) :
    s = input()
    
    arr = []
    for ch in s :
        arr.append(ord(ch))
    
    arr.sort()
    for i in range(len(arr)) :
        arr[i] = chr(arr[i])
        
    words = []
    for i in range(len(arr)) :
        permut(arr, i, len(arr), "")
    print()
