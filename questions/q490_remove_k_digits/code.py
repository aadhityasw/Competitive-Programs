class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        store = [''] * len(num)
        curLen = 0
        
        for ch in num :
            while curLen > 0 and k > 0 and ch < store[curLen-1] :
                curLen -= 1
                k -= 1
            
            store[curLen] = ch
            curLen += 1
        
        start = 0
        while start < curLen-k and store[start] == '0' :
            start += 1
        
        ans = ''.join(store[start:curLen-k])
        if ans == "" :
            ans = "0"
        return ans
