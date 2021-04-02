# This is a N^3 approach with hash tables

def fourSum(arr, k):
    arr.sort()
    n = len(arr)
    
    ans = [[] for _ in range(22)]
    for i in range(n-3) :
        if i > 0 and arr[i] == arr[i-1] :
            continue
        
        for j in range(i+1, n-2) :
            if j > i+1 and arr[j] == arr[j-1] :
                continue
        
            l = j+1
            r = n-1
            
            while l < r :
                summ = arr[i] + arr[j] + arr[l] + arr[r]
                tup = (arr[i], arr[j], arr[l], arr[r])
                if summ == k :
                    if tup not in ans[arr[i]//10] :
                        ans[arr[i]//10].append(tup)
                    l += 1
                    r -= 1
                elif summ < k :
                    l += 1
                else :
                    r -= 1
    
    answer = []
    for i in range(11, 22) :
        for a in ans[i] :
            answer.append(a)
    for i in range(11) :
        for a in ans[i] :
            answer.append(a)
    return answer
