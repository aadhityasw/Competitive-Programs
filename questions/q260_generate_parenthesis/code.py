
class Solution:
    def __init__(self) :
        self.store = {
            0 : [],
            1 : ["()"]
        }
    
    def AllParenthesis(self,n):
        if n in self.store :
            return self.store[n]
        
        ans = set()
        for i in range(n) :
            if i == 0 :
                for comb in self.AllParenthesis(n-1) :
                    ans.add('(' + comb + ')')
            else :
                for comb1 in self.AllParenthesis(i) :
                    for comb2 in self.AllParenthesis(n-i) :
                        ans.add(comb1 + comb2)
                        ans.add(comb2 + comb1)
        ans = list(ans)
        ans.sort()
        self.store[n] = ans
        
        return ans




        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        
