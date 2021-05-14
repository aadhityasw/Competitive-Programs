class Solution:
    def minJumps(self, arr, n):
        jumps = [-1] * n
        jumps[0] = 0
        
        front = 0
        rear = 0
        while rear < n :
            remaining_jumps = arr[rear] - (front - rear)

            while remaining_jumps > 0 and front < n-1:
                front += 1
                j = jumps[rear]
                jumps[front] = j + 1
                remaining_jumps -= 1
            
            rear += 1
            if rear > front :
                break
        
        
        return jumps[n-1]



        

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)
