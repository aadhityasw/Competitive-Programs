def dist(n, pos) :
    i, j = pos
    return ((i-n)**2 + (j-n)**2)

n = int(input())
matrix = [[' ' for _ in range(2*n + 1)] for _ in range(2*n + 1)]

for i in range(2*n+1) :
    for j in range(2*n+1) :
        if dist(n, (i, j)) <= n**2 + 1 :
            matrix[i][j] = '.'

for row in matrix :
    print(" ".join(row))
