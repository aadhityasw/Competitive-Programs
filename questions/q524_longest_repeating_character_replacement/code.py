class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = [0]*26
        front = -1
        rear = 0
        maxSize = 0

        while rear < len(s) :
            store[ord(s[rear])-65] += 1
            numToReplace = (rear - front) - max(store)

            while numToReplace > k and front <= rear:
                front += 1
                store[ord(s[front])-65] -= 1
                numToReplace = (rear - front) - max(store)
            
            maxSize = max(maxSize, (rear - front))
            rear += 1
        
        return maxSize
