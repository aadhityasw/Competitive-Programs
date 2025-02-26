def rotate(matrix): 

    # Any arbitrary number greater than all elements of the matrix
    mod = 102

    n = len(matrix)

    # Transfer i'th row into the reversed location of i'th column

    for i in range(n) :
        k = n-1
        for j in range(n) :
            # Value to be placed
            val = matrix[i][j]
            if val > mod :
                val = val // mod

            # We place it at matrix[k][i]
            matrix[k][i] = (matrix[k][i] * mod) + val
            k -= 1
    
    # Decode all the elements of the matrix
    for i in range(n) :
        for j in range(n) :
            matrix[i][j] = matrix[i][j] % mod




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N=int(input())
        arr=[int(x) for x in input().split()]
        matrix=[]

        for i in range(0,N*N,N):
            matrix.append(arr[i:i+N])

        rotate(matrix)
        for i in range(N): 
            for j in range(N): 
                print(matrix[i][j], end =' ') 
            print() 
