def fourSum(arr, num):
    arr.sort()
    n = len(arr)
    
    ans = []
    for i in range(n) :
        for j in range(i+1, n) :
            for k in range(j+1, n) :
                for l in range(k+1, n) :
                    if (arr[i] + arr[j] + arr[k] + arr[l]) == num :
                        cur = (arr[i], arr[j], arr[k], arr[l])
                        if cur not in ans :
                            ans.append(cur)
    
    return ans
