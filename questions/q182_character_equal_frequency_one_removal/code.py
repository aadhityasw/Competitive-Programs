import collections

class Solution:
    
    def getCount(self, n, freq) :
        # Find the number of characters with freq=1
        count = 0
        
        for _, v in freq.items() :
            if v == n :
                count += 1
                
        return count
    
    
    def sameFreq(self, s):
        freq = collections.Counter(s)
        
        if len(list(freq.keys())) <= 1 :
            return 1
        
        dis = list(set(freq.values()))
      
        # If we have many frequencies, removing one won't fix it
        if len(dis) > 2 :
            return 0
        
        # If all letters already have same frequency, no need to remove
        if len(dis) == 1 :
            return 1
        
        # If either a character has frequency as 1, or if there is just one letter with freq=1
        if ((abs(dis[0] - dis[1]) == 1) and (self.getCount(max(dis[0], dis[1]), freq) == 1)) or ((1 in dis) and (self.getCount(1, freq) == 1)) :
            return 1
        else :
            return 0





if __name__ == "__main__":
    T=int(input())

    for _ in range(T):
        s = input()
        ob = Solution()
        answer = ob.sameFreq(s)
        if answer:
            print(1)
        else:
            print(0)
