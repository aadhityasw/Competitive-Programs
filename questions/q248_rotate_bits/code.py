
class Solution:
    def rotate(self, N, D):
        D = D%16
        val1 = ((N << D) % (2 ** 16)) ^ int(N // (2 ** (16 - D)))
        #val1 = (N << D) | (N >> (16 - D))
        val2 = (N >> D) ^ int((2 ** (16 - D)) * (N % (2 ** D)))
        
        return [val1, val2]




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
