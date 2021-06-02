def find_num_decrease(i, arr, n) :
    count = 1
    for j in range(i+1, n) :
        if arr[j] <= arr[j-1] :
            count += 1
        else :
            break
    return count


def func(n, arr) :
    ans = [0 for _ in range(n)]

    if n == 1 :
        return 1
    
    i = 0
    while i < n :
        if i < n-1 and arr[i+1] <= arr[i] :
            d = find_num_decrease(i, arr, n)
            if i > 0 and arr[i-1] < arr[i] :
                ans[i] = max(ans[i-1] + 1, d)
                d -= 1
                i += 1
            while d > 0 and i < n :
                ans[i] = d
                d -= 1
                i += 1
        
        if i >= n :
            break
        
        if i > 0 :
            if arr[i-1] < arr[i] :
                ans[i] = ans[i-1] + 1
            else :
                ans[i] = 1
        else :
            ans[i] = 1
        i += 1
        

    #print(ans)
    return sum(ans)



n = int(input())
arr = []
for _ in range(n) :
    arr.append(int(input()))
print(func(n, arr))
