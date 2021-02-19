def max_of_subarrays(arr,n,k):
    '''
    you can use collections module here.
    :param a: given array
    :param n: size of array
    :param k: value of k
    :return: A list of required values 
    '''
    temp = arr[:k]
    ma = 0
    
    res = [max(temp)]
    
    for i in range(k, n) :
        temp = temp[1:] + [arr[i]]
        res.append(max(temp))
    
    return res
