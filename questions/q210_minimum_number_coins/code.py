class Solution:
    def minPartition(self, N):
        notes = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        
        i = 9
        ans = []
        while N > 0 :
            if N // notes[i] > 0 :
                ans.extend([notes[i]] * ( N // notes[i]))
                N = N % notes[i]
            i -= 1
        
        return ans




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
