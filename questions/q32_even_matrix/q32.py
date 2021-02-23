# Codechef June2020

# EVENM
# Even Matrix
# https://www.codechef.com/problems/EVENM

"""
Chef has an integer N and he wants to generate a matrix M with N rows (numbered 1 through N) and N columns (numbered 1 through N). He thinks that M would be delicious if:

Each element of this matrix is an integer between 1 and N2 inclusive.
All the elements of the matrix are pairwise distinct.
For each square submatrix containing cells in rows r through r+a and in columns c through c+a (inclusive) for some valid integers r, c and a≥0:
Mr,c+Mr+a,c+a is even
Mr,c+a+Mr+a,c is even
Can you help Chef generate a delicious matrix? It can be proved that a solution always exists. If there are multiple solutions, you may find any one.
"""

test = int(input())
for t in range(test) :
    n = int(input())
    p = 1
    c = 1
    r = 0
    while (p <= (n*n)) :
        if r%2 == 0 :
            print(p, end=" ")
        else :
            print(((r+1)*n)-c, end=" ")
        if p%n == 0 :
            print()
            r += 1
            c = 0
        else :
            c += 1
        p += 1
