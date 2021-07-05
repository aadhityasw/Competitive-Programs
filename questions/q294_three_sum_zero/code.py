class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, nums):
        lookup = dict()
        for num in nums:
            if not num in lookup:
                lookup[num] = 0
            lookup[num] += 1
        
        #Check 0, 0, 0 condition
        if 0 in lookup and lookup[0] > 2:
            res = [[0,0,0]]
        else:
            res = []
        
        #We will iterate by positive and then negative
        pos = [p for p in lookup if p > 0]
        neg = [n for n in lookup if n < 0]
        
        # check whether the missing value is in dictionary
        for p in pos:
            for n in neg:
                i = -p-n
                if i not in lookup:
                    continue
                # We now found possible correspondence in dictionary, but still little to compare
                # 1. the missing value is 0
                if i == 0 and lookup[i] > 0:
                    res.append([n, 0, p])
                # 2. the missing value is same as positive value, so the occurrences should be greater than 1
                elif i == p and lookup[i] > 1:
                    res.append([n, p, p])
                # 3. Same above
                elif i == n and lookup[i] > 1:
                    res.append([n, n, p])
                # 4. Deciding position in the answer
                elif i > p:
                    res.append([n, p, i])
                elif i < n:
                    res.append([i, n, p])
                    
        return res
