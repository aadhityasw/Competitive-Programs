
from collections import Counter
import heapq
import sys

class Solution :
    def rearrangeString(self, S):

        freq = Counter(S)

        heap = [(-1*v, k) for (k, v) in freq.items()]
        heapq.heapify(heap)

        result = ""
        flag = True
        ch = ''
        while (len(heap) > 0) and flag :
            #print(heap)
            if (ch == heap[0][1]) :
                if (len(heap) == 1):
                    flag = False
                    break
                else :
                    (v, k) = heap[1]
                    result += k
                    ch = k
                    
                    if v != -1 :
                        heap[1] = (v+1, k)
                    else :
                        heap.pop(1)
                    heapq.heapify(heap)
            else :
                (v, k) = heap[0]
                result += k
                ch = k

                heapq.heappop(heap)
                if v != -1 :
                    heapq.heappush(heap, (v+1, k))
        
        if flag :
            return result
        else :
            return "-1"
            
            

        
        
        

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        str = input()

        solObj = Solution()
        str1 = solObj.rearrangeString(str)
        
        flag=1
        c=[0]*26
        for i in range(len(str)):
            c[ord(str[i])-97]+=1
        f = 0
        x = (len(str)+1)//2
        for i in range(26):
            if c[i]>x:
                f = 1
        if f:
            if str1=="-1":
                print(0)
            else:
                print(1)
        else:
            a=[0]*26 
            b=[0]*26
            for i in range(len(str)):
                a[ord(str[i])-97]+=1
            for i in range(len(str1)):
                b[ord(str1[i])-97]+=1
                
            for i in range(26):
                if a[i]!=b[i]:
                    flag = 0
            
            for i in range(len(str1)):
                if i>0:
                    if str1[i-1]==str1[i]:
                        flag=0
            if flag==1:
                print(1)
            else:
                print(0)
