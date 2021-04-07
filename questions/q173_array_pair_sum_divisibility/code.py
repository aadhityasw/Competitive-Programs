class Solution :

    def canPair(self, nums, k) :

        n = len(nums)
        if n % 2 != 0 :
            return False

        # Initialization of dictionary
        count = [0] * k

        # Filling the map
        for i in range(n) :
            count[nums[i]%k] += 1
        
        #print(count)
        
        if (count[0] % 2 != 0) or ((k%2 == 0) and (count[k // 2] % 2 != 0)) :
            return False
        
        limit = k // 2
        limit += 1 if k%2==1 else 0
        for i in range(1, limit) :
            if (count[i] != count[k-i]) :
                return False
        
        return True



if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, k = input().split()
        n = int(n)
        k = int(k)
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.canPair(nums, k)
        if(ans):
            print("True")
        else:
            print("False")
