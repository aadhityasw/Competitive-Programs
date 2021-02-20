def findSpiral(root):
    
    if root is None :
        return []
    
    cur_level = [root]
    next_level = []
    arr = []
    level = 0
    
    while len(cur_level) > 0 :
        
        for i in range(len(cur_level)) :
            ptr = cur_level[i]
            if ptr.left :
                next_level.append(ptr.left)
            if ptr.right :
                next_level.append(ptr.right)
        
        if level % 2 == 0 :
            for i in range(len(cur_level)-1, -1, -1) :
                arr.append(cur_level[i].data)
        else :
            for i in range(len(cur_level)) :
                arr.append(cur_level[i].data)
        
        cur_level = next_level
        next_level = []
        level += 1
    
    return arr
