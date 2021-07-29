class Solution:
    def isProduct(self, arr, n, x):
        
        store = set()
        for num in arr :
            
            if num == 0 :
                if x == 0 :
                    return True
                continue
            
            if num in store :
                return True
                
            if x % num != 0 :
                continue
            
            store.add(x / num)
        
        return False






if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.isProduct(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1
