from collections import deque


def max_of_subarrays(arr,n,k):
    '''
    you can use collections module here.
    :param a: given array
    :param n: size of array
    :param k: value of k
    :return: A list of required values 
    '''

    queue = deque()
    res = []

    # To enter the initial k elements
    for i in range(k) :
        while queue and arr[queue[-1]] <= arr[i] :
            queue.pop()
        queue.append(i)
    
    for i in range(k, n) :
        res.append(arr[queue[0]])

        # Remove elements out of range
        while queue and queue[0] < (i-k) :
            queue.popleft()
        
        # Remove all elements smaller than arr[i]
        while queue and arr[queue[-1]] <= arr[i] :
            queue.pop()
        
        queue.append(i)
    
    res.append(arr[queue[0]])

    return res
