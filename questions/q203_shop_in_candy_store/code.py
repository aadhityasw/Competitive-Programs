class Solution:

    def candyStore(self, candies,N,K):
        candies.sort()
        
        min_cost = 0
        front = 0
        rear = N-1
        while front <= rear :
            min_cost += candies[front]
            front += 1
            rear -= K
        
        front = 0
        rear = N-1
        max_cost = 0
        while front <= rear :
            max_cost += candies[rear]
            front += K
            rear -= 1
        
        return min_cost, max_cost




if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        N,K = [int(x) for x in input().split()]
        candies = [int(x) for x in input().split()]

        solObj = Solution()

        print(*solObj.candyStore(candies,N,K))
