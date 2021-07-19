class Solution:
    
    def recurse(self, s) :
        
        if len(s) == 0 :
            return 1
        if s[0] == '0' :
            return 0
        if s in self.store :
            return self.store[s]
        
        count = 0
        if s[0] == '1' :
            if len(s) > 1 :
                count += self.recurse(s[2:])
        elif s[0] == '2' :
            if len(s) > 1 and int(s[1]) < 7 :
                count += self.recurse(s[2:])
        count += self.recurse(s[1:])
        
        self.store[s] = count
        return count

    
    def CountWays(self, s):
        
        if (len(s) == 0) or ("00" in s) or (s[0] == '0') :
            return 0
        
        self.store = {}
        
        self.recurse(s)
        
        return self.store[s] % 1000000007






import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        str = input()
        ob = Solution()
        ans = ob.CountWays(str)
        print(ans)
