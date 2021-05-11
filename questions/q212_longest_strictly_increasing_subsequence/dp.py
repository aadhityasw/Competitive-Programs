"""
Uses a Dynamic Programming Approach
"""



class Solution:

    def findPath(self, i) :
        if self.path_length[i] == 0 :
            leng = 0
            for j in range(i+1, self.n) :
                if self.a[j] > self.a[i] :
                    leng = max(leng, self.findPath(j))
            self.path_length[i] = 1 + leng
        
        return self.path_length[i]

    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):

        self.path_length = [0] * n
        self.n = n
        self.a = a

        max_len = 0
        i = 0
        while i < n :
            max_len = max(max_len, self.findPath(i))
            i += 1
        
        return max_len
