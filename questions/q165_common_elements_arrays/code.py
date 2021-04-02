import collections
import sys

class Solution:
    def common_element(self,v1,v2):
        
        if len(v2) == 0 :
            return sorted(v1)
        
        f1 = collections.Counter(v1);
        f2 = collections.Counter(v2);
        
        sorted_keys = sorted(f1.keys())
        
        arr = []
        
        for key in sorted_keys :
            if key in f1 and key in f2 :
                arr += [key] * min(f1[key], f2[key])
        
        return arr

if __name__=='__main__' :
    t = int(input())
    for _ in range(t) :
        n = int(input())
        v1 = list(map(int, input().strip().split()))
        try :
            m = int(input())
            v2 = list(map(int, input().strip().split()))
            ob = Solution()
            ans = ob.common_element(v1, v2)
            print(*ans)
        except EOFError :
            print(*list(sorted(v1)))
    sys.exit(1)
