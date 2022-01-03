import sys
s=input()
s=s.strip()
if s=='12:00:00 midnight' :
    print('08:00:00 midnight')
elif s=='12:00:00 noon' :
    print('04:00:00 B.M')
elif s=='08:00:00 A.M' :
    print('00:00:00 midmorning')
elif s=='04:00:00 P.M' :
    print('08:00:00 midevening')
else :
    mer=s[len(s)-3:]
    tim=s[:len(s)-3]
    time=tim.split(':')
    ti=[]
    for i in time :
        ti.append(int(i))
    if mer=='P.M' :
        ti[0]=ti[0]+12
    if ti[0]<8 and ti[1]<60 and ti[2]<60 :
        time=[]
        for i in ti :
            if i<10 :
                c='0'+str(i)
            else :
                c=str(i)
            time.append(c)
        ab=':'.join(time)
        print(ab,'A.M')
    elif ti[0]<16 and ti[1]<60 and ti[2]<60 :
        ti[0]=ti[0]-8
        time=[]
        for i in ti :
            if i<10 :
                c='0'+str(i)
            else :
                c=str(i)
            time.append(c)
        ab=':'.join(time)
        print(ab,'B.M')
    elif ti[0]<24 and ti[1]<60 and ti[2]<60:
        ti[0]=ti[0]-16
        time=[]
        for i in ti :
            if i<10 :
                c='0'+str(i)
            else :
                c=str(i)
            time.append(c)
        ab=':'.join(time)
        print(ab,'C.M')