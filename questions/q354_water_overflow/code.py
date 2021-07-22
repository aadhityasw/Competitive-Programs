class Solution:
    def waterOverflow(self, K, R, C):
        
        if R <= 0 or C <= 0 or C > R :
            return 0
        
        table = [[K]]
        i = 0
        while True :
            table.append([0]*(i+2))
            flag = True
            for j in range(i+1) :
                if table[i][j] > 1 :
                    val = (table[i][j] - 1) / 2
                    table[i][j] = 1
                    table[i+1][j] += val
                    table[i+1][j+1] += val
                    flag = False
            if flag or i > (R-1) :
                break
            i += 1
        
        if table[R-1][C-1] == int(table[R-1][C-1]) :
            return int(table[R-1][C-1])
        return round(table[R-1][C-1], 6)
        
        

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        K,R,C=map(int,input().split())
        
        ob = Solution()
        print(ob.waterOverflow(K,R,C))
