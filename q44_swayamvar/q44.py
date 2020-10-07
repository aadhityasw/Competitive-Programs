# TCS Code VITA

# Swayamvar

#%%


n = int(input())
bride = input().strip()
groom = input().strip()
rum = 0
mojito = 0
for ch in groom :
    if ch == 'r' :
        rum += 1
    elif ch == 'm' :
        mojito += 1
p = 0
ans = 0
for ch in bride :
    if ch == 'r' :
        if rum == 0 :
            ans = n - p
            break
        rum -= 1
    elif ch == 'm' :
        if mojito == 0 :
            ans = n - p
            break
        mojito -= 1
    p += 1
print(ans)