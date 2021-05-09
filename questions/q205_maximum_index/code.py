class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,arr, n): 
        
        positions = []
        cur_max_pos = None
        for i in range(n-1, -1, -1) :
            if i == n-1 :
                cur_max_pos = n-1
                positions.append(n-1)
            else :
                if arr[i] > arr[cur_max_pos] :
                    positions.append(i)
                    cur_max_pos = i
        
        max_diff = 0
        for i in range(n) :
            j = 0
            while j < len(positions) and arr[positions[j]] < arr[i] and i < positions[j] :
                j += 1
            max_diff = max(max_diff, (positions[j] - i))
        
        return max_diff





import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
