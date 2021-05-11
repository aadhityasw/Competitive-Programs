operation_map = {}

class Solution:
    def minOperation(self, n):
        global operation_map
        
        if n not in operation_map :
            if n == 0 :
                operation_map[n] = 0
            elif n % 2 == 0 :
                operation_map[n] = 1 + self.minOperation(n // 2)
            else :
                operation_map[n] = 1 + self.minOperation(n - 1)
                
        return operation_map[n]


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
