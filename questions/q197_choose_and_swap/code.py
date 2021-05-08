class Solution:
    def chooseandswap (self, A):
        
        opt = 'a'
        fir = A[0]

        arr = [0]*26
        for s in A :
            arr[ord(s)-97] += 1
        
        i = 0
        while i < len(A) :
            if opt > 'z' :
                break

            while opt < fir :
                if opt in A :
                    ans = ""
                    for s in A :
                        if s == opt :
                            ans += fir
                        elif s == fir :
                            ans += opt
                        else :
                            ans += s
                    return ans
                
                opt = chr(ord(opt) + 1)
            opt = chr(ord(opt) + 1)
            
            while i < len(A) and A[i] <= fir :
                i += 1
            if i < len(A) :
                fir = A[i]
        
        return A


if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)
