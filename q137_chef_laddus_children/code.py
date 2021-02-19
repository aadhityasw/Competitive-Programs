#%%

T = int(input())
for tes in range(T) :
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    arr.sort()

    min_diff = 9999999999
    for i in range(n-k+1) :
        diff = max(arr[i:i+k]) - min(arr[i:i+k])
        if diff < min_diff :
            min_diff = diff

    print(min_diff)


#%%


T = int(input())
for tes in range(T) :
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    arr.sort()

    temp_max = max(arr[:k])
    temp_min = min((arr[:k]))
    min_diff = temp_max - temp_min
    for i in range(n-k) :
        
        if arr[i+k] >= temp_max :
            temp_max = arr[i+k]
        elif temp_max == arr[i] :
            temp_max = max(arr[i+1:i+k+1])
        
        if arr[i+k] <= temp_min :
            temp_min = arr[i+k]
        elif temp_min == arr[i] :
            temp_min = min(arr[i+1:i+k+1])
        
        diff = temp_max - temp_min
        if diff < min_diff :
            min_diff = diff
    
    print(min_diff)




#%%


T = int(input())
for tes in range(T) :
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    arr.sort()

    min_diff = 9999999999
    for i in range(n-k+1) :
        diff = arr[i+k-1] - arr[i]
        if diff < min_diff :
            min_diff = diff

    print(min_diff)
