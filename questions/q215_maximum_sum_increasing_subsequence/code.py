class Solution:
    def maxSumIS(self, Arr, n):
        summ_arr = [0] * n

        for i in range(n) :
            s = 0
            for j in range(i) :
                if Arr[j] < Arr[i] :
                    s = max(s, summ_arr[j])
            summ_arr[i] = s + Arr[i]

        return max(summ_arr)



if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.maxSumIS(Arr,n)
        print(ans)
