def verticalOrder(root): 

    pos = []
    neg = []
    queue = [(root, 0)]
    
    while len(queue) > 0 :

        ptr, H = queue.pop(0)

        if ptr.left :
            queue.append((ptr.left, H-1))
        if ptr.right :
            queue.append((ptr.right, H+1))
        
        if H >= 0 :
            if len(pos) > H :
                pos[H].append(ptr.data)
            elif len(pos) == H :
                pos.append([ptr.data])
        else :
            H_p = (-1 * H) - 1
            if len(neg) > H_p :
                neg[H_p].append(ptr.data)
            elif len(neg) == H_p :
                neg.append([ptr.data])
        
    arr = []
    for i in range(len(neg)-1, -1, -1) :
        arr.extend(neg[i])
    for i in range(len(pos)) :
        arr.extend(pos[i])
    
    return arr
