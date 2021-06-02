#import sys
#sys.setrecursionlimit(50000)


class Node :
    """
    This is a Trie Node, and can be used to form a trie.
    """

    def __init__(self, numUniqueSyllables = 256):
        """
        Used to define the Trie Node.

        Parameters
        ----------
        numUniqueSyllables - Number of unique syllables of the language being used, defaults to 26 of the english language.
        """
        self.is_leaf = False
        self.children = [None] * numUniqueSyllables
        self.num_unique_syllables = numUniqueSyllables
        self.word_count = 0
        self.added = False
    

    def checkPresence(self, character) :
        """
        Given a character returns if the character is present in this node's children or not

        Parameter
        ---------
        character - the character which needs to be checked
        """

        encoded_character = ord(character)
        return (self.children[encoded_character] is not None)
    

    def getChildNode(self, character) :
        """
        Given a character returns the child with this value.

        Parameter
        ---------
        character - the character whose node needs to be returned
        """

        encoded_character = ord(character)
        return self.children[encoded_character]



class Trie :

    def __init__(self):
        self.root = Node()
    

    def insertWord(self, word) :
        """
        A customized function designed to enter only the capital letters of the words as nodes.
        
        Parameters
        ----------
        word - the word to be inserted into the trie
        """

        # Initialze a pointer to point to the root node
        cur_node = self.root

        for ch in word :
            if cur_node.children[ord(ch)] is None :
                cur_node.children[ord(ch)] = Node()
            cur_node = cur_node.children[ord(ch)]
        
        # Mark the end node as a leaf
        cur_node.is_leaf = True
        cur_node.word_count += 1



class Solution:

    def getCandidatePositions(self, r, c, board) :
        """
        Given the current position and the board, determines the candidate positions for the next step

        Parameters
        ----------
        r - the row position
        c - the column position
        board - the board
        """

        # Find the dimensions of the board
        l, w = len(board), len(board[0])
        
        # List out the possible positions
        possible_positions = [
            (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1),
            (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)
        ]

        # Among these possible positions, find the candidates
        candidate_positions = []
        for position in possible_positions :
            (i, j) = position
            if (0 <= i < l) and (0 <= j < w) and (not self.visited[i][j]) :
                candidate_positions.append(position)
        
        # Return the list of candidate positions
        return candidate_positions



    def search(self, position, board, node, s) :
        """
        Searches if the character in the current position is present in the child's node or not, if so then recurses to find the remaining part of the word.

        Parameters
        ----------
        position - the (row, column) positions of the current location in the board
        board - the board
        node - the current node in the trie
        s - the currently formed string
        """

        # Extract the positions
        r, c = position

        # If the current board position has been marked as visited then return
        if self.visited[r][c] :
            return

        # Check if word can be formed using this character
        if node.checkPresence(board[r][c]) :

            # Get the child node
            child = node.getChildNode(board[r][c])

            # If the child node is a leaf node, then add the currently forned string as a found word
            if (child.is_leaf) and (not child.added) :
                # Add how many ever instances of the word is present in the dictionary
                for _ in range(child.word_count) :
                    self.found_words.append(s+board[r][c])
                child.added = True
            
            # Mark the current character in board as visited
            self.visited[r][c] = True
            
            for next_position in self.getCandidatePositions(r, c, board) :
                self.search(next_position, board, child, s+board[r][c])
            
            # Mark the current character in board as not visited again, as we are backtracking and persuing another path
            self.visited[r][c] = False


    def wordBoggle(self,board,dictionary):

        if len(board) == 0 or len(dictionary) == 0 :
            return []

        # Create a Trie structure and insert all the words into this
        trie = Trie()
        for word in dictionary :
            trie.insertWord(word)

        # Create an array to store the found words
        self.found_words = []

        # Fetch the co-ordinates of the board
        r, c = len(board), len(board[0])

        # Create a visited array
        self.visited = [[False for _ in range(c)] for _ in range(r)]

        # Perform the search
        for i in range(r) :
            for j in range(c) :
                self.search((i, j), board, trie.root, "")

        # Returns the found words
        return list(self.found_words)


if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        N=int(input())
        dictionary=[x for x in input().strip().split()]
        line=input().strip().split()
        R=int(line[0])
        C=int(line[1])
        board=[]
        for _ in range(R):
            board.append( [x for x in input().strip().split()] )
        obj = Solution()
        found = obj.wordBoggle(board,dictionary)
        if len(found) is 0:
            print(-1)
            continue
        found.sort()
        for i in found:
            print(i,end=' ')
        print()
