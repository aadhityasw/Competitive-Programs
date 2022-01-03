# ============================================================================================================
# We deal with many cases in order to try and figure out the actual scenario meant in the problem statement
# ============================================================================================================


#%%

# Considering that each state in each phase can have only one seat.
t = int(input())
for test in range(t) :
    s = list(map(int, input().strip().split(' ')))
    r = s[0]
    c = s[1]
    rl = list(map(int, input().strip().split(' ')))
    cl = list(map(int, input().strip().split(' ')))
    if sum(rl) != sum(cl) :
        print('NO')
    else :
        f = True
        rl.sort(reverse = True)
        cl.sort(reverse = True)
        for i in range(r) :
            for j in range(c) :
                if cl[j]==0 and rl[i]!=0 :
                    print('NO')
                    f = False
                    break
                else :
                    rl[i] -= 1
                    cl[j] -= 1
                if i == r-1 and cl[j] !=0 :
                    print('NO')
                    f = False
                    break
            if f==False :
                break
        if f==True :
            print('YES')



#%%

# Considering that each state in each phase can have more than one seats.
t = int(input())
for test in range(t) :
    s = list(map(int, input().strip().split(' ')))
    r = s[0]
    c = s[1]
    rl = list(map(int, input().strip().split(' ')))
    cl = list(map(int, input().strip().split(' ')))
    if sum(rl) != sum(cl) :
        print('NO')
    else :
        store = []
        t = True
        for i in range(r) :
            for j in range(c) :
                if rl[i]>0 and cl[j]>0 :
                    store.append([i, j, 1])
                    rl[i] -= 1
                    cl[j] -= 1
            while rl[i]>0 :
                f = False
                for j in range(len(store)-1, -1,-1) :
                    if cl[store[j][1]>0] :
                        store[j][2] += 1
                        rl[store[j][0]] -= 1
                        cl[store[j][1]] -= 1
                        f = True
                        break
                if f==False :
                    print('NO')
                    t = False
                    break
        if t == True :
            print('YES')
            print(store)




#%%

# Considering that each state in each phase can have more than one seats.
def elect(rl, cl, x, y, store) :
    for i in range(x, len(rl)) :
        if i != x :
            a = 0
        else :
            a = y
        for j in range(a, len(cl)) :
            #print(i, j)
            if rl[i]>0 and cl[j]>0 :
                store.append([i, j, 1])
                rl[i] -= 1
                cl[j] -= 1
        print(store, rl, cl, rl[i])
        if rl[i]>0 :
            #print(store, rl, cl)
            for j in range(len(store)-1, -1,-1) :
                if cl[store[j][1]>0] and rl[store[j][0]]>0 :
                    store[j][2] += 1
                    rl[store[j][0]] -= 1
                    cl[store[j][1]] -= 1
                    store = store[:j+1]
                    #print(store, 'Call')
                    return(elect(rl, cl, store[j][0], store[j][1], store))
                else :
                    rl[store[j][0]] += 1
                    cl[store[j][1]] += 1
                if j == 0 :
                    return(False)
            return(False)
    return(True)

t = int(input())
for test in range(t) :
    s = list(map(int, input().strip().split(' ')))
    r = s[0]
    c = s[1]
    rl = list(map(int, input().strip().split(' ')))
    cl = list(map(int, input().strip().split(' ')))
    if sum(rl) != sum(cl) :
        print('NO')
    else :
        t = elect(rl, cl, 0, 0, [])
        if t :
            print('YES')
        else :
            print('NO')




#%%

# Considering that each state in each phase can have only one seat.
t = int(input())
for test in range(t) :
    s = list(map(int, input().strip().split(' ')))
    r = s[0]
    c = s[1]
    rll = list(map(int, input().strip().split(' ')))
    cll = list(map(int, input().strip().split(' ')))
    if sum(rl) != sum(cl) :
        print('NO')
    else :
        t = True
        rl = rll.copy()
        cl = cll.copy()
        rl.sort(reverse = True)
        cl.sort(reverse = True)
        for i in range(len(rl)) :
            count = 0
            for j in range(len(cl)) :
                if cl[j]>0 :
                    count += 1
                    cl[j] -= 1
            if rl[i] > count :
                t = False
                break
        if t == True :
            print('YES')
        else :
            print('NO')