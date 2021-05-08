class Solution:
    def getMinDiff(self, arr, n, k):

        arr.sort()

        for i in range(n) :
            arr[i] += k
        
        mini = arr[0]
        maxi = arr[-1]
        ans = maxi - mini

        for i in range(n-1, -1, -1) :
            arr[i] -= (2 * k)
            if arr[i] < 0 :
                break

            if i > 0 :
                maxi = max(arr[-1], arr[i-1])
            else :
                maxi = arr[n-1]
            mini = min(arr[0], arr[i])
            ans = min(ans, (maxi - mini))

        return ans
