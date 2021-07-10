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

        for i, num in enumerate(A) :
            pos = self.hashFunc(num)
            if num in table[pos] :
                table[pos][num].append(i)
            else :
                table[pos][num] = [i]

        ans = set()
        for i in range(n) :
            for j in range(i+1, n) :
                for k in range(j+1, n) :
                    rem = B - (A[i] + A[j] + A[k])
                    pos = self.hashFunc(rem)
                    if rem in table[pos] :
                        index = list(set(table[pos][rem]) - {i, j, k})
                        for l in index :
                            res = [A[i], A[j], A[k], A[l]]
                            res.sort()
                            res = tuple(res)
                            ans.add(res)

        ans = list(ans)
        ans.sort()       
        return ans
