class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        
        table = [0] *  n
        table[0] = a[0]
        num_ele = 1

        for i in range(1, n) :
            if a[i] < table[0] :
                # If there is a new smallest number, we replace the first set
                table[0] = a[i]
            elif a[i] > table[num_ele - 1] :
                # If there is a new greatest number, we extend this table
                table[num_ele] = a[i]
                num_ele += 1
            else :
                # If there is a middle number, we need to replace it at its appropriate position
                
                # Do Binary Search to find the appropriate position
                l = 0
                r = num_ele - 1
                while r > l :
                    m = (l + r) // 2
                    if table[m] >= a[i] :
                        r = m
                    else :
                        l = m + 1
                
                # Change that occurance
                table[r] = a[i]
        
        # Return the length
        return num_ele


       



if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
