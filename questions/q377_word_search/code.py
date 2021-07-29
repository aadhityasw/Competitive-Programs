class Solution:

    def getCandidate(self, position, visited) :
        """
        Returns all the possible moves from a position.

        Parameters
        ----------
        - position - the current position in the board
        - visited - the visited marker matrix

        Return
        ------
        - candidates - a list of all candidates for next move
        """

        # Decode the dimensions of the board
        # The visited matrix has same dimensions as the board
        m, n = len(visited), len(visited[0])

        # Decode the current position
        r, c = position

        # List out all the possible moves
        possible_moves = [
            (r+1, c), (r-1, c),
            (r, c+1), (r, c-1)
        ]

        # Scrutinize the moves based on the conditions
        candidates = []
        for (i, j) in possible_moves :
            if 0 <= i < m and 0 <= j < n and not visited[i][j] :
                candidates.append((i, j))
        
        # Return the list of candidates
        return candidates


    def DFS(self, position, word, board, visited) :
        """
        Performs a DFS search for the word in the board

        """

        # If the word is empty, then we have found it
        if len(word) == 0 :
            return True

        # Decode the current position
        r, c = position

        # Mark the current cell as visited
        visited[r][c] = True

        # If the next letter is matching any candidate position, then we apply DFS in that direction
        for next_position in self.getCandidate(position, visited) :
            if board[next_position[0]][next_position[1]] == word[0] :
                if self.DFS(next_position, word[1:], board, visited) :
                    return True
        
        # Mark the cell as not visited, as we are backtracking from this path
        visited[r][c] = False
        
        # If no path is found
        return False


    def isWordExist(self, board, word):

        # If the board is empty, we cannot find the word
        if len(board) == 0 :
            return False

        # Decode the dimensions of the board
        m, n = len(board), len(board[0])
        
        # Create a visited array to keep track of the current path followed
        visited = [[False for _ in range(n)] for _ in range(m)]

        # If the first letter of the word is found, start a DFS search from this position
        for i in range(m) :
            for j in range(n) :
                if word[0] == board[i][j] :
                    if self.DFS((i, j), word[1:], board, visited) :
                        return True
        
        return False




if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n, m = map(int, input().split())
        board = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            board.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(board, word)
        if(ans):
            print("1")
        else:
            print("0")
