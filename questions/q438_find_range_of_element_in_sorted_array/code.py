class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=-1
        end=-1
        l=0
        r=len(nums)-1

        # Find start
        while l <= r :
            m = l + (r-l)//2
            if nums[m] == target :
                if m == 0 or nums[m-1] < target :
                    start = m
                    if m == len(nums)-1 or nums[m+1] > target :
                        end = m
                    break
                else :
                    r = m-1
            elif nums[m] < target :
                l = m+1
            else :
                r = m-1
        
        if start > -1 and end > -1 :
            return [start, end]
        elif start == -1 :
            return [-1, -1]
        else :
            l = start
            r = len(nums)-1

            # Find end
            while l <= r :
                m = l + (r-l)//2

                if nums[m] == target :
                    if m == len(nums)-1 or nums[m+1] > target :
                        end = m
                        break
                    else :
                        l = m+1
                elif nums[m] < target :
                    l = m+1
                else :
                    r = m-1
            
        return [start, end]
