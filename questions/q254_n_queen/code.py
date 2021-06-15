class Solution:

    def __init__(self):
        self.validPositions = []


    def validatePosition(self, board, n, position) :
        """
        Given a board and the position for the queen to be placed, returns if we can make this move or not
        """

        # Primary Diagonal
        x, y = len(board)-1, position-1
        while x >= 0 and y >= 0 :
            if board[x] == y :
                return False
            x -= 1
            y -= 1
        
        # Row
        x, y = len(board)-1, position
        while x >= 0 :
            if board[x] == y :
                return False
            x -= 1
        
        # Secondary Diagonal
        x, y = len(board)-1, position+1
        #print(board, position, x, y)
        while x >= 0 and y <= n:
            if board[x] == y :
                #print("false")
                return False
            x -= 1
            y += 1
        
        return True



    def nQueen(self, n, board=[]):
        if len(board) == n :
            self.validPositions.append(board)
            return

        for i in range(1, n+1) :
            if self.validatePosition(board, n, i) :
                self.nQueen(n, board + [i])

        return self.validPositions






if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
