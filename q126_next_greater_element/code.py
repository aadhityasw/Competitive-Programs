'''
Function Arguments : 
		@param  : arr(given array), n(size of array)
		@return : An array of length n denoting the next greater elements 
		          for all the array elements
'''
def nextLargerElement(arr,n):
    stack = [arr[-1]]
    res = [0] * n
    
    res[-1] = -1
    for i in range(n-2, -1, -1) :
        if len(stack) > 0 :
            while (len(stack) > 0) and (arr[i] > stack[-1]) :
                stack.pop()
            if len(stack) == 0 :
                res[i] = -1
            else :
                res[i] = stack[-1]
        stack.append(arr[i])
    
    return res
