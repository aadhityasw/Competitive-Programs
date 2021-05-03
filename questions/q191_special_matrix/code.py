class Solution:
    def minMoves (self, N, matrix):
        st = []
        for i in range(50):
            x = (i*(i+1))/2
            st.append(int(x))
            
        ans = 1e9 
        
        for i in range(N):
            c = 0
            for j in range(N):
                high = bisect.bisect(st,matrix[i][j])
                low = 0 
                if high:
                    low = high-1
                c += min(matrix[i][j] - st[low] , st[high] - matrix[i][j]) 
            ans = min(ans , c)
        
        
        for i in range(N):
            c = 0
            for j in range(N):
                high = bisect.bisect(st,matrix[j][i])
                low = 0 
                if high:
                    low = high-1
                c += min(matrix[j][i] - st[low] , st[high] - matrix[j][i]) 
            ans = min(ans , c)
        
        return ans
