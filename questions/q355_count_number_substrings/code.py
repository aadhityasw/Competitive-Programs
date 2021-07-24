class Solution:
    
    def atMostK(self, s, k) :
        
        freq = [0]*26
        n = len(s)
        front = 0
        count = 0
        
        for rear in range(n) :
            if not freq[ord(s[rear])-97] :
                k -= 1
            freq[ord(s[rear])-97] += 1
            
            while k < 0 :
                freq[ord(s[front])-97] -= 1
                if not freq[ord(s[front])-97] :
                    k += 1
                front += 1
            count += rear - front + 1
        
        return count
        
    
    
    def substrCount (self,s, k):
        
        return self.atMostK(s, k) - self.atMostK(s, k-1)





t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
