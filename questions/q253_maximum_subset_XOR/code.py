class Solution:
    def maxSubarrayXOR(self, arr, N):

        # Initialize Maximum number of bits
        bits = 32

        front = 0
        for i in range(bits-1, -1, -1) :

            # Initialize temp variables for storing the position and value of maximum number with the i'th bit set
            max_ele = 0
            max_pos = front - 1
            
            # Loop through the unchecked elements for comparing them to find the largest number with i'th bit set
            for j in range(front, N) :
                if ((arr[j] & (1 << i)) != 0) and arr[j] > max_ele :
                    max_ele = arr[j]
                    max_pos = j
            
            # If there are no new numbers with i'th bit set
            if max_pos < front :
                continue

            # Copy the maximum number with i'th bit set to the frontier and expand it
            arr[front], arr[max_pos] = arr[max_pos], arr[front]
            front += 1

            # Do XOR with all numbers with i'th bit set so as to nullify its effect in further iterations
            for j in range(N) :
                if (j != front-1) and ((arr[j] & (1 << i)) != 0) :
                    arr[j] = arr[j] ^ max_ele

        # Final sum is the XOR of all these processed elements of the array
        ans = 0
        for i in range(N) :
            ans = ans ^ arr[i]
        
        return ans



if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        set=list(map(int,input().split()))
        obj = Solution()
        print(obj.maxSubarrayXOR(set,n))
