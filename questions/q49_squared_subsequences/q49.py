# Codechef      SQRDSUB

"""import math
testcase = int(input())
prodarr = set()
for tes in range(testcase) :
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    count = 0
    for i in range(n) :
        prod = 1
        for j in range(i, n) :
            prod *= arr[j]
            absprod = abs(prod)
            if absprod in prodarr :
                count += 1
            else :
                for k in range(math.sqrt(absprod)+1) :
                    dif = prod + math.pow(k, 2)
                    if dif<0 :
                        continue
                    dif = math.sqrt(dif)
                    if dif%1 == 0.0 :
                        count += 1
                        prodarr.add(absprod)
                        break
    print(count)"""