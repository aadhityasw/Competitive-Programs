class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        board = {}
        count = 0
        
        for i in A :
            if i in board :
                if board[i] == 0 :
                    count += 1
                board[i] += 1
            else :
                count += 1
                board[i] = 1
        
        #print(count, board)
        
        for i in B :
            if i in board :
                if board[i] == 0 :
                    return False
                board[i] -= 1
                if board[i] == 0 :
                    count -= 1
            else :
                return False
        
        #print(count, board)
        
        if count != 0 :
            return False
        
        return True






if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
