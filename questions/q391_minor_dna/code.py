def poss(d,m,b) :
    global l
    global k
    c=d
    e=b
    for i in range(len(d)) :
        if m==1 :
            for j in range(len(d)) :
                l.append(e+c[j])
            return()
        e=e+c[i]
        c=c[i+1:]
        if len(e)==k :
            l.append(e)
            return()
        poss(c,m-1,e)
        c=d
        e=b
d=input().strip()
k=int(input())
l=[]
poss(d,k,'')
l.sort()
print(l)