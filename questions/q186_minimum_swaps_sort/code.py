class Solution:

    def minSwaps(self, nums):

        arrpos = [*enumerate(nums)]
        arrpos.sort(key= lambda s : s[1])

        num_cycles = 0
        n = len(nums)

        visited = {d:False for d in nums}

        for i in range(n) :

            if visited[nums[i]] or arrpos[i][1] == nums[i] :
                continue

            length = 0
            j = i

            while not visited[nums[j]] :

                visited[nums[j]] = True
                j = arrpos[j][0]
                length += 1
            
            num_cycles += (length - 1)
        
        return num_cycles


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        obj = Solution()
        ans = obj.minSwaps(nums)
        print(ans)
