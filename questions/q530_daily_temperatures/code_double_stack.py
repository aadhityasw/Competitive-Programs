class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        store = []

        for i in range(len(temperatures)-1, -1, -1) :
            numDays = 1
            while len(store)>0 and store[-1][0] <= temperatures[i] :
                numDays += store[-1][1]
                store.pop()
            
            if len(store) > 0 :
                ans[i] = numDays
            
            store.append([temperatures[i], numDays])
        
        return ans
