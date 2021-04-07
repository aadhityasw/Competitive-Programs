# Time Limit Exceeded

import collections

class Solution:
    def countDistinct(self, A, N, K):
        freq = collections.Counter(A[:K])
        arr = [len(freq.keys())]
        
        for i in range(K, N) :
            
            freq[A[i-K]] -= 1
            if freq[A[i-K]] == 0 :
                del freq[A[i-K]]
                
            if A[i] in freq :
                freq[A[i]] += 1
            else :
                freq[A[i]] = 1
            
            arr.append(len(freq.keys()))
    
        return arr
