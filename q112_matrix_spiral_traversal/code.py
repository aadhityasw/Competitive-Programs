def spirallyTraverse(matrix, r, c): 
    round = 0
    arr = []

    while True :

        if round >= c-round :
            break
        for i in range(round, c-round) :
            arr.append(matrix[round][i])
        
        if round+1 >= r-round :
            break
        for i in range(round+1, r-round) :
            arr.append(matrix[i][c-round-1])
        
        if c-round-2 <= round-1 :
            break
        for i in range(c-round-2, round-1, -1) :
            arr.append(matrix[r-round-1][i])
        
        if r-round-2 <= round :
            break
        for i in range(r-round-2, round, -1) :
            arr.append(matrix[i][round])
        
        round += 1
    
    return arr
