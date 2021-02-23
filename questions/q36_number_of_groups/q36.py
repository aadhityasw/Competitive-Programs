# Coding ninjas

# Number of groups

# Write your code here


def compatible(s1, s2) :
    count = 0
    if len(s1) != len(s2) :
        return False
    for i in range(len(s1)) :
        if s1[i] != s2[i] :
            count += 1
    if count % 2 == 0 :
        return True
    else :
        return False


def getlargest(words, arr, i, lar) :
    if i == len(words) :
        return(len(arr))
    else :
        for j in range(i, len(words)) :
            flag = True
            for k in arr :
                if not compatible(k, words[j]) :
                    flag = False
                    break
            if flag :
                arr.append(words[j])
                l = getlargest(words, arr, j+1, lar)
                if l > lar :
                    lar = l
                    print(arr, words[j], lar)
                arr = arr[:-1]
    return(lar)

    
n = int(input())
words = []
for i in range(n) :
    words.append(input().strip())
print(getlargest(words, [], 0, 0))