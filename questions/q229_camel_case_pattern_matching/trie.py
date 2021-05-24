"""
A Trie data structure based implementation of this question's solution.
@Author : aadhityasw
"""



class Node :
    """
    This is a Trie Node, and can be used to form a trie.
    """

    def __init__(self, numUniqueSyllables = 26):
        """
        Used to define the Trie Node.

        Parameters
        ----------
        numUniqueSyllables - Number of unique syllables of the language being used, defaults to 26 of the english language.
        """
        self.is_leaf = False
        self.children = [None] * numUniqueSyllables
        self.words = []
        self.num_unique_syllables = numUniqueSyllables



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

        # Insert all the capital characters as nodes of the trie
        for ch in word :
            if 65 <= ord(ch) <= 90 :
                if cur_node.children[ord(ch) - 65] is None :
                    cur_node.children[ord(ch) - 65] = Node()
                cur_node = cur_node.children[ord(ch) - 65]
        
        # Mark the end node as a leaf, and append the word to this leaf node's word list
        cur_node.is_leaf = True
        cur_node.words.append(word)


    def searchPattern(self, pattern) :
        """
        A customized function, such that given a pattern, searches for it, and returns the node where a match happens.
        
        Parameters
        ----------
        pattern - the pattern that needs to be searched in the trie
        """

        # Initialze a pointer to point to the root node
        cur_node = self.root

        # Search by navigating the trie by the pattern
        for ch in pattern :
            if cur_node.children[ord(ch) - 65] is None :
                # If pattern is not found, return NULL
                return None
            else :
                cur_node = cur_node.children[ord(ch) - 65]
        
        # Return the node where a match is found
        return cur_node


    def extractWords(self, node) :
        """
        After finding the pattern, we extract the words with this pattern as its subset of capital letters from beginning
        
        Parameters
        ----------
        node - the node in the trie where the pattern was completely matched
        """

        # Initialize a temporary variable for traversal
        cur_node = node

        # Initialize an array to store all the words
        arr = []

        # If the current node is a leaf, then we start the word extraction from here
        if cur_node.is_leaf :
            arr.extend(cur_node.words)

        # Perform a DFS Traversal from this node
        for i in range(cur_node.num_unique_syllables) :
            if cur_node.children[i] is not None :
                arr.extend(self.extractWords(cur_node.children[i]))
        
        # Return the list of all words
        return arr



class Solution:
    def CamelCase(self,N,Dictionary,Pattern):

        # Initialize a trie structure
        trie = Trie()

        # Insert all the words of the dictionary into the trie
        for word in Dictionary :
            trie.insertWord(word)
        
        # Find the node in the trie where the pattern is matched successfully
        matched_node = trie.searchPattern(Pattern)

        # If the pattern was not matched, return an empty array
        if matched_node is None :
            return []
        
        # Extract all the words that match this pattern
        matched_words = trie.extractWords(matched_node)

        # Return the list of matched words
        return matched_words






if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        for i in ans:
            print(i,end=" ")
        print()
