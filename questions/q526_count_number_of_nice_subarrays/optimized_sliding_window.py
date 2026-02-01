class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        front = 0
        rear = 0
        pEven = 0
        curOdd = 0
        count = 0

        while rear < len(nums) :
            if nums[rear] % 2 == 1 :
                curOdd += 1
            
            while curOdd > k and front < rear :
                pEven = 0
                if nums[front] % 2 == 1 :
                    curOdd -= 1
                front += 1
            
            while front < rear and curOdd == k and (nums[front]%2 == 0) :
                pEven += 1
                front += 1
            
            if curOdd == k :
                count += (1 + pEven)

            rear += 1
            
        return count
