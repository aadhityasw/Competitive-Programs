def merge(arr1,arr2,n,m):
    """ This is a O(n*m) solution """
    j = m - 1
    while j >= 0 :
        if arr2[j] < arr1[-1] :
            num = arr2[j]
            arr2[j] = arr1[-1]
            i = n - 2
            while arr1[i] > num and i >= 0 :
                arr1[i+1] = arr1[i]
                i -= 1
            arr1[i+1] = num
        j -= 1
