def findElement( arr, n):
    front = []
    rear = []

    for a in arr :
        if len(front) == 0 :
            front.append(a)
        else :
            front.append(max(a, front[-1]))
    
    for a in reversed(arr) :
        if len(rear) == 0 :
            rear.append(a)
        else :
            rear.append(min(a, rear[-1]))
    rear.reverse()
    
    for i in range(1, n-1) :
        if arr[i] == front[i] == rear[i] :
            return arr[i]
    
    return -1
