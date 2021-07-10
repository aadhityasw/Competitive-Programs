class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
    def anagrams(self, A):

        table = {}

        for i, word in enumerate(A) :
            freq = [0]*26
            for ch in word :
                freq[ord(ch)-97] += 1
            
            freq = tuple(freq)
            if freq in table :
                table[freq].append(i+1)
            else :
                table[freq] = [i+1]
        
        return list(table.values())
