class Solution:

    def hashFunc(self, num) :
        return num % 1000


	# @param A : list of integers
	# @param B : integer
	# @return a list of list of integers
    def fourSum(self, A, B):

        A.sort()
        n = len(A)
        table = [{} for i in range(1001)]

        ans = set()
        for i in range(n) :
            for j in range(i+1, n) :
                cur_sum = A[i] + A[j]
                rem = B - cur_sum
                pos = self.hashFunc(rem)
                if rem in table[pos] :
                    for k, l in table[pos][rem] :
                        if l < i :
                            ans.add((A[k], A[l], A[i], A[j]))
                
                pos = self.hashFunc(cur_sum)
                if cur_sum in table[pos] :
                    table[pos][cur_sum].append((i, j))
                else :
                    table[pos][cur_sum] = [(i, j)]

        ans = list(ans)
        ans.sort()       
        return ans
