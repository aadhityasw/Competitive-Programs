class Solution:
    def setSetBit(self, x, y, l, r):
        n1 = (x // (2 ** (l-1))) % (2 ** (r-l+1))
        n2 = (y // (2 ** (l-1))) % (2 ** (r-l+1))
        n3 = n1 | n2
        n3 = n3 * (2 ** (l-1))
        x = x | n3
        return x




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        x = int(arr[0])
        y = int(arr[1])
        l = int(arr[2])
        r = int(arr[3])
        
        ob = Solution()
        print(ob.setSetBit(x, y, l, r))
