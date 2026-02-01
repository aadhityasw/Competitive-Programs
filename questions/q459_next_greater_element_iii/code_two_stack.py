class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = n
        s1 = []
        dig = -1

        while num > 0 and (num % 10) >= dig :
            dig = num % 10
            s1.append(dig)
            num = num // 10
        
        if num == 0 :
            return -1
        
        dig = num % 10
        num = num // 10

        s2 = []
        while len(s1)>0 and s1[-1] > dig :
            s2.append(s1[-1])
            s1.pop()
        s1.append(dig)
        
        num = (num*10) + s2[-1]
        s2.pop()

        while len(s1)>0 :
            s2.append(s1[-1])
            s1.pop()
        
        while len(s2)>0 :
            num = (num*10) + s2[-1]
            s2.pop()
        
        if num > (2**31 - 1) :
            return -1
        return num
        