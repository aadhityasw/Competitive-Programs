#  CHPINTU
# https://www.codechef.com/problems/CHPINTU

test = int(input())
for tes in range(test) :
    (m, n) = list(map(int, input().strip().split()))
    f = list(map(int, input().strip().split()))
    p = list(map(int, input().strip().split()))
    dict = {}
    for i in range(len(f)) :
        if f[i] not in dict :
            dict[f[i]] = 0
        dict[f[i]] += p[i]
    print(min(dict.values()))
