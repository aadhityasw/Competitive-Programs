class Solution:
    def findLargest(self, N, S):
        if S > 9 :
            num9 = S // 9
            modu = S % 9
            remaining = N - num9 - (1 if modu > 0 else 0)
            if remaining < 0 :
                return -1
            else :
                return "9"*num9 + (str(modu) if modu>0 or remaining>0 else "") + "0"*(remaining if modu>0 else remaining-1)
        elif S > 0 :
            return str(S) + "0"*(N-1)
        else :
            if N == 1 :
                return 0
        return -1
        




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
