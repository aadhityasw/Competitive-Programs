class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        front = 0
        rear = 0
        curSum = 0
        pZero = 0
        count = 0

        while (rear < len(nums)) :
            curSum += nums[rear]

            while (curSum > goal and front < rear) :
                curSum -= nums[front]
                front += 1
                pZero = 0
            
            while curSum == goal and front < rear and nums[front] == 0 :
                pZero += 1
                front += 1
            
            if curSum == goal :
                count += (1 + pZero)

            rear += 1
        
        return count
