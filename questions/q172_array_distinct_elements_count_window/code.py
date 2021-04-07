import collections

class Solution:
    def countDistinct(self, A, N, K):
        freq = collections.Counter(A[:K])
        count = len(freq.keys())
        
        arr = [count]
        
        for i in range(K, N) :
            
            freq[A[i-K]] -= 1
            if freq[A[i-K]] == 0 :
                count -= 1
                
            if A[i] in freq :
                if freq[A[i]] == 0 :
                    count += 1
                freq[A[i]] += 1
            else :
                freq[A[i]] = 1
                count += 1
            
            arr.append(count)
    
        return arr


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
