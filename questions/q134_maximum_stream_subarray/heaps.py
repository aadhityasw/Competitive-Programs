import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        store = []
        ans = []

        for i in range(k) :
            heapq.heappush(store, (-1*nums[i], i))
        ans.append(-1 * store[0][0])

        for i in range(k, len(nums)) :
            heapq.heappush(store, (-1*nums[i], i))
            while store[0][1] <= i-k :
                heapq.heappop(store)
            
            ans.append(-1 * store[0][0])
        
        return ans
