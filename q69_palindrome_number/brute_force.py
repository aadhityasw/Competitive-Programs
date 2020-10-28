class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 :
            return False
        
        arr = []
        while x > 0 :
            arr.append(x % 10)
            x = x // 10
        
        right_side_start = (len(arr) // 2) + (0 if len(arr)%2==0 else 1)
        left = (len(arr) // 2) - 1

        for i in range(right_side_start, len(arr)) :
            if left < 0 or arr[left] != arr[i] :
                return False
            left -= 1
            
        return True
