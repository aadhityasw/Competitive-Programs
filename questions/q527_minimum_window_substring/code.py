class Solution:
    def minWindow(self, s: str, t: str) -> str:
        front = 0
        rear = 0
        ans = ""
        ansSize = float('inf')
        numSuccessful = 0
        numRequired = 0

        keyStore = [0] * 128
        store = [0] * 128

        for ch in t :
            keyStore[ord(ch)] += 1
            if keyStore[ord(ch)] == 1 :
                numRequired += 1
        
        while rear < len(s) :
            store[ord(s[rear])] += 1
            if store[ord(s[rear])] == keyStore[ord(s[rear])] :
                numSuccessful += 1

            # Trim window from front
            while store[ord(s[front])] > keyStore[ord(s[front])] and front < rear :
                store[ord(s[front])] -= 1
                front += 1
            
            if numSuccessful == numRequired :
                if ansSize > (rear - front + 1) :
                    ans = s[front:rear+1]
                    ansSize = (rear - front + 1)
                
                store[ord(s[front])] -= 1
                if store[ord(s[front])] < keyStore[ord(s[front])] :
                    numSuccessful -= 1
                front += 1
            
            rear += 1
        
        return ans
