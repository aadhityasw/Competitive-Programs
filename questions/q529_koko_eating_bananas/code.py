class Solution:

    def getTimeToEat(self, piles: List[int], curSpeed: int) -> int:
        time = 0
        for ban in piles :
            time += (ban//curSpeed) + (0 if (ban%curSpeed == 0) else 1)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r :
            m = l + (r-l)//2

            curTime = self.getTimeToEat(piles, m)
            if curTime <= h :
                r = m
            else :
                l = m+1
        
        return l
