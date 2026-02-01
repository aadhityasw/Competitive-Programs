class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        store = []

        for i in range(len(temperatures)-1, -1, -1) :
            while len(store)>0 and temperatures[store[-1]] <= temperatures[i] :
                store.pop()
            
            if len(store) > 0 :
                ans[i] = store[-1] - i
            
            store.append(i)
        
        return ans
