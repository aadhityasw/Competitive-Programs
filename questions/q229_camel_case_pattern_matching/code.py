class Solution:
    def CamelCase(self,N,Dictionary,Pattern):

        # Extract and store only the capital letters of each word
        arr = []
        for i, word in enumerate(Dictionary) :
            arr.append("")
            for ch in word :
                if 65 <= ord(ch) <= 90 :
                    arr[i] = arr[i] + ch
        
        # Find and store the words that match
        ans = []
        for i, short in enumerate(arr) :
            if short.startswith(Pattern) :
                ans.append((arr[i], Dictionary[i]))

        # Sort this by their Capital letters short hand notation, and return the words in the same sorted order
        ans.sort(key= lambda w : w[0])
        return [w[1] for w in ans]




if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        for i in ans:
            print(i,end=" ")
        print()
