class Solution:
    # @param numerator : integer
    # @param denominator : integer
    # @return a string
    def fractionToDecimal(self, n, d):

        # If result is a whole number
        if n % d == 0 :
            return str(n // d)
        
        # Initialize variable to store result
        ans = ''

        # Prepare the sign
        if (abs(n)/n) * (abs(d)/d) < 0 :
            ans += '-'
            n = abs(n)
            d = abs(d)
        
        # Add the integer part (left part to the decimal point)
        ans += str(n // d) + '.'
        n = n % d

        # Now n < d, and we find the fractional value

        # Check for cycles (recurring decimals) using fast and slow pointers
        slow = n
        fast = n
        while fast != 0 :
            slow = (slow * 10) % d
            fast = (fast * 10) % d
            if fast != 0 :
                fast = (fast * 10) % d
            if fast == slow :
                break
        
        if fast == 0 :
            # No cycle in the list
            slow = n
            while slow != 0 :
                ans += str((slow * 10) // d)
                slow = (slow * 10) % d
        else :
            # If a cycle is present

            # Save the pre-cycle elements
            slow = n
            while slow != fast :
                ans += str((slow * 10) // d)
                slow = (slow * 10) % d
                fast = (fast * 10) % d
            
            # Now add the recurring portion
            ans += '('
            while True :
                ans += str((slow * 10) // d)
                slow = (slow * 10) % d
                if slow == fast :
                    break
            ans += ')'
        
        return ans



ob = Solution()
A = -1
B = -2147483648
print(ob.fractionToDecimal(A, B))
