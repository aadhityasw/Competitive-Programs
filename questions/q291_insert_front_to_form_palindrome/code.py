class Solution:
    # @param A : string
    # @return an integer
    def solve(self, s):
        n = len(s)
        lps = [0]*n
        i,l = 1,0
        while i < n:
            if s[i]==s[l]:
                lps[i] = l+1
                l+=1
                i+=1
            elif l > 0:
                l = lps[l-1]
            else:
                i+=1
        ans = n
        for i in range(n):
            x = i-lps[i]
            if lps[i]>=x:
                ans = n-i-1
        return ans
