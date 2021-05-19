from collections import Counter

class Solution:
    
    #Function to find most frequent word in an array of strings.
    def mostFrequentWord(self,arr,n) :

        # Find the frequency of each word, and find its frequency
        freq = Counter(arr)
        max_freq = max(freq.values())

        visited = {word : False for word in freq.keys()}

        for i, word in enumerate(arr) :
            if freq[word] == max_freq :
                if not visited[word] :
                    required_word = word
                    visited[word] = True
        
        return required_word
