T = int(input())
for tes in range(T) :
    s = input()
    flag = False
    while not flag :
        flag = True
        i = 0
        res = ""
        while i < len(s) :
            if i < len(s)-1 and s[i] == s[i+1] :
                flag = False
                ch = s[i]
                while i < len(s) and s[i] == ch :
                    i += 1
            else :
                res += s[i]
                i += 1
        s = res
    print(res)
