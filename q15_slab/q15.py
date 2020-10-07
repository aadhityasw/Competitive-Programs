#  SLAB

test = int(input())
for tes in range(test) :
    tot = int(input())
    totalinc = tot
    tr = 0
    tax = 0
    while(tot>0) :
        if(tr > 25) :
            tax += tr*tot/100
            tot = 0
        else :
            if(tot < 250000) :
                tax += tot*tr/100
                tot = 0
            else :
                tax += 250000*tr/100
                tot -= 250000
                tr += 5
    inc = int(totalinc - tax)
    print(inc)