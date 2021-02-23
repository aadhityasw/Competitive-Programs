# CodeJam - Qualification Round - Nesting Depths


T = int(input())
for test in range(1, T+1) :
    inp = input()
    out = ""
    cur = 0
    for chri in inp :
        i = int(chri)
        if i > cur :
            out = out + ('(' * (i-cur)) + chri
        elif cur > i :
            out = out + (')' * (cur-i)) + chri
        else :
            out += chri
        cur = i
    if cur > 0 :
        out = out + (')' * cur)
    print('Case #'+ str(test) + ': ' + out)