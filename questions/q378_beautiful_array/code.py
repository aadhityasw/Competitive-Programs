class Solution:
    
    def findCombination(self, N):
        
        if N not in self.store:
            odds = self.findCombination((N+1)//2)
            evens = self.findCombination(N//2)
            self.store[N] = [2*x-1 for x in odds] + [2*x for x in evens]
        
        return self.store[N]
    
    
    def beautifulArray(self, n: int) :
        self.store = {1: [1]}
    
        self.findCombination(n)
        
        return self.store[n]
