def merge(arr1,arr2,n,m) :
    """ This is a O((n+m)log(n+m)) solution """
    gap = n + m

    while gap > 1 :

        gap = (gap // 2)  + (gap % 2)
        
        i = 0
        while (i + gap) <= (n+m-1) :
            if i < n  and (i+gap) < n :
                if arr1[i] > arr1[i+gap] :
                    arr1[i], arr1[i+gap] = arr1[i+gap], arr1[i]
            elif i < n and (i + gap) >= n :
                if arr1[i] > arr2[i+gap-n] :
                    arr1[i], arr2[i+gap-n] = arr2[i+gap-n], arr1[i]
            elif i >= n :
                if arr2[i-n] > arr2[i+gap-n] :
                    arr2[i-n], arr2[i+gap-n] = arr2[i+gap-n], arr2[i-n]
            i += 1
