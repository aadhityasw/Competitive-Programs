class Solution:
    def isValid(self, mat):
        numbers_row = [{nu : False for nu in range(1, 10)} for _ in range(9)]
        numbers_col = [{nu : False for nu in range(1, 10)} for _ in range(9)]
        
        # Check for each row and column
        for i in range(9) :
            for j in range(9) :
                # Check for each row
                if mat[i][j] != 0 and numbers_row[i][mat[i][j]] :
                    return 0
                else :
                    numbers_row[i][mat[i][j]] = True
                # Check for each column
                if mat[j][i] != 0 and numbers_col[i][mat[j][i]] :
                    return 0
                else :
                    numbers_col[i][mat[j][i]] = True
                
        # Check for all mini grids
        numbers = [{nu : False for nu in range(1, 10)} for _ in range(9)]
        ptr = 0
        for i in range(0, 9, 3) :
            for j in range(0, 9, 3) :
                for k in range(9) :
                    r = i + k // 3
                    c = j + k % 3
                    if mat[r][c] != 0 and numbers[ptr][mat[r][c]] :
                        return 0
                    else :
                        numbers[ptr][mat[r][c]] = True
                ptr += 1
        
        return 1
                    
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        mat = [[0]*9 for x in range(9)]
        for i in range(81):
            mat[i//9][i%9] = int(arr[i])
        
        ob = Solution()
        print(ob.isValid(mat))
# } Driver Code Ends
