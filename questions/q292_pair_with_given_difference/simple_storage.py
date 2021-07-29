class Solution:

    def findPair(self, arr, L,N):
        
        store = set()
        for num in arr :
            if num in store :
                return True
            store.add(num - N)
            store.add(num + N)
        
        return False


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        L,N = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        if(solObj.findPair(arr,L, N)):
            print(1)
        else:
            print(-1)
