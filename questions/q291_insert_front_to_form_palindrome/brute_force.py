class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        s = '$'
        for ch in A :
            s = s + ch + '$'
        
        n = len(s)
        pos = n // 2

        while pos > 0 :
            i = 0
            while i < pos :
                if s[i] == s[(pos-i)+pos] :
                    i += 1
                    continue
                else :
                    break
            if i == pos :
                #print(pos)
                return (n - (2*pos))//2
            pos -= 1
