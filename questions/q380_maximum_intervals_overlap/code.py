class Solution:

    def findMaxGuests(self, Entry, Exit, N):
        
        Entry.sort()
        Exit.sort()
        
        current_strength = 0
        max_strength = 0
        time_max_strength = -1
        
        start = 0
        end = 0
        
        while start < N :
            if Entry[start] <= Exit[end] :
                current_strength += 1
                start += 1
            elif Entry[start] > Exit[end] :
                current_strength -= 1
                end += 1
            
            if current_strength > max_strength :
                time_max_strength = Entry[start-1]
                max_strength =  current_strength
        
        return max_strength, time_max_strength
        
        


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        
        N = int(input())

        entry = [int(x) for x in input().split()]
        exit =  [int(x) for x in input().split()]

        solObj = Solution()
        ans = solObj.findMaxGuests(entry, exit, N) 
        print(ans[0],ans[1])
