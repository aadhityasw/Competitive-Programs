# Time Limit Exceeded

import math


class Solution:
    def countDistinct(self, A, N, K):
        table = [{} for _ in range(6)]
        count = [0 for _ in range(6)]

        for i in range(K) :
            p = int(math.log(A[i], 10))
            if A[i] in table[p] :
                if table[p][A[i]] == 0 :
                    count[p] += 1
                table[p][A[i]] += 1
            else :
                count[p] += 1
                table[p][A[i]] = 1
        
        arr = [sum(count)]

        for i in range(K, N) :
            p = int(math.log(A[i-K], 10))
            table[p][A[i-K]] -= 1
            if table[p][A[i-K]] == 0 :
                count[p] -= 1
            
            p = int(math.log(A[i], 10))
            if A[i] in table[p] :
                if table[p][A[i]] == 0 :
                    count[p] += 1
                table[p][A[i]] += 1
            else :
                count[p] += 1
                table[p][A[i]] = 1
            
            arr.append(sum(count))
        
        return arr

