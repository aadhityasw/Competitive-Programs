class Solution:
    def getCount(self, N):
        
        if N < 3 :
            return 0
        elif N == 3 :
            return 1
        
        cur_sum = 3
        start = 1
        end = 2
        count = 0
        
        while end < N//2 + 2 :
            if end-start < 1 :
                cur_sum += end+1
                end += 1
            elif cur_sum < N :
                cur_sum += end+1
                end += 1
            else :
                cur_sum -= start
                start += 1
            
            if cur_sum == N :
                count += 1
        
        return count


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.getCount(N))
