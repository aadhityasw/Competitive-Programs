# This is for the leetcode version of the problem


from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        store = deque()
        ans = []

        for i in range(len(nums)) :
            while len(store) > 0 and nums[store[-1]] <= nums[i] :
                store.pop()
            while len(store) > 0 and store[0] <= i-k :
                store.popleft()
            store.append(i)

            if i >= k-1 :
                ans.append(nums[store[0]])

        return ans
