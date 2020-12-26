class Solution:
    def removeDups(self, S):
        arr = []
        st = ""
        for ch in S :
            if ch not in arr :
                arr.append(ch)
                st += ch
        return st



if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s = input()
        
        ob = Solution()    
        answer = ob.removeDups(s)
        
        print(answer)
