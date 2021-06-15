class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):

        # Increment the number by 1
        n += 1

        # The RHS bit with have 1 half the number of times
        count = n // 2

        power = 2
        while power <= n :
            # Get the number of full groups in that current position from right
            current_index_pairs = n // power
            # For each full group, half of them will have 1 in the current position from right, so we add this
            count += (current_index_pairs // 2) * power

            # If there are any leftovers in a group, then it means there will be leftovers from each group, so we add all these
            if current_index_pairs % 2 == 1 :
                count += (n % power)
            
            # Increment the power to check for the next index in binary
            power *= 2
        
        return count
        
if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
