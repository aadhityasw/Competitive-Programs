class Solution:

    def findPair(self, arr, L,N):
        
        # Sort the array
        arr.sort()
        
        front = 0
        rear = 1
        
        while front < L and rear < L :
            
            # If the current window is empty, we extend it
            if front == rear :
                rear += 1
                continue
            
            # If there are two numbers with the required difference
            if arr[rear] - arr[front] == N :
                return True
            # If the difference is not enough, we increase the rear pointer to get larger number
            elif arr[rear] - arr[front] < N :
                rear += 1
            # If the difference is larger than required, we reduce the boundary
            else :
                front += 1
        
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
