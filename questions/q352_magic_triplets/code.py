class Solution:
    def countTriplets(self, nums):
        
        n = len(nums)
        count = 0
        
        for i in range(1, n-1) :
            lcount = 0
            ptr1 = i-1
            while ptr1 >= 0 :
                if nums[ptr1] < nums[i] :
                    lcount += 1
                ptr1 -= 1
            
            rcount = 0
            ptr2 = i + 1
            while ptr2 < n :
                if nums[ptr2] > nums[i] :
                    rcount += 1
                ptr2 += 1
            
            count += (lcount * rcount)
        
        return count
