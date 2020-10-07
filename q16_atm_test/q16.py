#HS08TEST
# https://www.codechef.com/problems/HS08TEST

withd, bal = map(float, input().strip().split())
if withd%5 != 0 :
    print(bal)
elif (withd+0.5) > bal :
    print(bal)
else :
    print(bal - 0.5 - withd)
