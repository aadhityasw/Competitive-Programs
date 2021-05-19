"""
This code causes a time limit exceeded error, so Not sure if this works

"""


from collections import Counter


class Trie :
    def __init__(self):
        self.is_leaf = False
        self.children = []
    
    def insert(self, word) :

        # If the word is of zero length, then return the word if it is not a leaf, else return None
        if len(word) == 0 :
            if self.is_leaf :
                return None
            else :
                self.is_leaf = True
                return ""

        # If the word[0] character is present in its children, then proceed further into that node
        for (ch, child) in self.children :
            if ch == word[0] :
                res = child.insert(word[1:])
                # If the result is a word, we append this character to the front to form the word
                if res is not None :
                    res = ch + res
                return res
            
        # If the word[0] character is not present, create a new entry and proceed.
        self.children.append((word[0], Trie()))
        res = self.children[-1][1].insert(word[1:])
        # If the result is a word, we append this character to the front to form the word
        if res is not None :
            res = ch + res
        return res


class Solution:
    
    #Function to find most frequent word in an array of strings.
    def mostFrequentWord(self,arr,n) :

        # Find the frequency of each word, and find its frequency
        freq = Counter(arr)
        max_freq = max(freq.values())

        # Initialize the trie
        trie = Trie()
        
        # Insert all the words with maximum frequency into the trie
        for i in range(n) :
            if freq[arr[i]] == max_freq :
                # Find the last word that was entered into the trie
                # If the trie returns a word, it means that it was inserted, else it is already present in trie
                val = trie.insert(arr[i])
                if val is not None :
                    required_word = val

        return required_word
