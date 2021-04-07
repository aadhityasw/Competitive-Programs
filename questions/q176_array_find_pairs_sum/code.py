import math
import heapq


class Solution:

    def getPos(self, num) :
        if num == 0 :
            return 0
        elif num < 0 :
            return 13 - int(math.log(-1*num, 10))
        else :
            return int(math.log(num, 10))


    def allPairs(self, A, B, N, M, X):
        tableA = [[] for _ in range(14)]
        tableB = [[] for _ in range(14)]

        for i in A :
            heapq.heappush(tableA[self.getPos(i)], i)
        for i in B :
            tableB[self.getPos(i)].append(i)
        
        ans = []
        
        for i in range(7, 14) :
            while len(tableA[i]) > 0 :
                a = heapq.heappop(tableA[i])
                if (X - a) in tableB[self.getPos(X - a)] :
                    ans.append((a, X-a))
        for i in range(7) :
            while len(tableA[i]) > 0 :
                a = heapq.heappop(tableA[i])
                if (X - a) in tableB[self.getPos(X - a)] :
                    ans.append((a, X-a))
        
        return ans
        


        
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        N, M, X = sz[0], sz[1], sz[2]
        A = [int(x) for x in input().strip().split()]
        B = [int(x) for x in input().strip().split()]
        ob=Solution()
        answer = ob.allPairs(A, B, N, M, X)
        sz = len(answer)
        
        if sz==0 :
            print(-1) 
        
        else: 
            
            for i in range(sz):
                if i==sz-1:
                    print(*answer[i])
                else:
                    print(*answer[i], end=', ')
        

        T -= 1


if __name__ == "__main__":
    main()
