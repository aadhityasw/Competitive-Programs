class Solution:
    def shortest_distance(self, matrix):

        V = len(matrix)

        for k in range(V) :
            for i in range(V) :
                for j in range(V) :
                    if (i != j) and (matrix[i][k] >= 0) and (matrix[k][j] >= 0) :
                        matrix[i][j] = min(matrix[i][j], (matrix[i][k] + matrix[k][j]))
        
        return matrix


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        obj = Solution()
        obj.shortest_distance(matrix)
        for _ in range(n):
            for __ in range(n):
                print(matrix[_][__], end = " ")
            print()
