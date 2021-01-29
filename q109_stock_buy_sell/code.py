class Solution:
    def stockBuySell(self, A, n):
        arr = []

        i = 0
        while i < n :
            while i < n-1 and A[i+1] <= A[i] :
                i += 1
            buy = i
            while i < n-1 and A[i+1] >= A[i] :
                i += 1
            sell = i
            i += 1
            if A[sell] > A[buy] :
                arr.append([buy, sell])
    
        return arr
