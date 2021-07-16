def Anagrams(words,n):

    store = {}
    order = []

    for word in words :
        arr = [0]*26
        for ch in word :
            arr[ord(ch)-97] += 1
        arr = tuple(arr)
        if arr in store :
            store[arr].append(word)
        else :
            store[arr] = [word]
            order.append(arr)
    
    ans = []
    for arr in order :
        ans.append(store[arr])
    
    return ans


if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ans=Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()
