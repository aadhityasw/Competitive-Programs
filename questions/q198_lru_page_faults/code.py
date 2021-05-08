class Solution:
    def pageFaults(self, N, C, pages):
        cache_size = 0
        page_faults = 0
        cache = {i : 0 for i in range(1001)}
        end = 0
        start = 0

        while end < N :
            ele = pages[end]
            if cache[ele] > 0 :
                cache[ele] += 1
            else :
                cache[ele] = 1
                cache_size += 1
                page_faults += 1
            
            while cache_size > C :
                cache[pages[start]] -= 1
                if cache[pages[start]] == 0 :
                    cache_size -= 1
                start += 1
            
            end += 1
        
        return page_faults



if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        pages = input().split()
        for itr in range(N):
            pages[itr] = int(pages[itr])
        C = int(input())

        ob = Solution()
        print(ob.pageFaults(N, C, pages))
