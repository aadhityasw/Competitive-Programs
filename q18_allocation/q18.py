# Allocation
# Kickstart 2020 A

test = int(input())
for tes in range(test) :
    (n, avacost) = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))
    c = 0
    i=0
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if avacost >= arr[n-i-1] :
            c += 1
            avacost -= arr[n-i-1]
        else :
            break
    
    stri = 'Case #' + str(tes+1) + ": " + str(c)
    print(stri)