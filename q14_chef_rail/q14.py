# Code Chef   CHEFRAIL

test = int(input())
for tes in range(test) :
    (m, n) = map(int, input().strip().split())
    x = list(map(int, input().strip().split()))
    y = list(map(int, input().strip().split()))
    xpos=[]
    xneg = []
    ypos = []
    yneg = []
    ys = {}
    xs = {}
    p = 0
    for i in x :
        if i>0 :
            xpos.append(i)
            p=i
        elif i<0 :
            xneg.append(i)
            p=-1*i
        else :
            xpos.append(i)
            xneg.append(i)
            p = i

        if p in xs :
            xs[p] += 1
        else :
            xs[p] = 1

    for i in y :
        if i>0 :
            ypos.append(i)
            p = i
        elif i<0 :
            yneg.append(i)
            p=-1*i
        else :
            ypos.append(i)
            yneg.append(i)
            p = i
        if p in ys :
            ys[p] += 1
        else :
            ys[p] = 1
    count = 0
    
    for i in xpos :
        for j in xneg :
            s = (i*j*-1)**(1/2)
            if (s == int(s)) and (int(s) in ys) :
                count += ys[int(s)]
    
    for i in ypos :
        for j in yneg :
            s = (i*j*-1)**(1/2)
            if (s == int(s)) and (int(s) in xs) :
                count += xs[int(s)]
    
    print(count)