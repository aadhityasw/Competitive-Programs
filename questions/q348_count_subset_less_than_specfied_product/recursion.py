class Solution:
    def recurse(self, arr, ind, k, cur_prod) :
        
        if cur_prod and cur_prod > k :
            return
        
        for i in range(ind, len(arr)) :
            if cur_prod :
                next_prod = cur_prod * arr[i]
            else :
                next_prod = arr[i]
            
            if next_prod > k :
                continue
            
            self.count += 1
            self.recurse(arr, i+1, k, next_prod)
            
    
    
    def numOfSubsets(self, arr, N, K):
        self.count = 0
        
        arr.sort()
        self.recurse(arr, 0, K, None)

        return self.count
