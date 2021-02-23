# TCS Codevita

# Digit Pairs



#%%

n = int(input())
arr = list(map(int, input().strip().split()))
odd = {}
even = {}
for i in range(1, n+1) :
    num = arr[i-1]
    lar = max(int(num//100), int((num//10)%10), int(num%10))
    sma = min(int(num//100), int((num//10)%10), int(num%10))
    score = 11*lar + 7*sma
    bit = int((score%100)//10)
    if i % 2 == 0 :
        if bit in even :
            even[bit] += 1
        else :
            even[bit] = 1
    else :
        if bit in odd :
            odd[bit] += 1
        else :
            odd[bit] = 1
count = 0
for num in list(odd.keys()) :
    if odd[num] > 2 :
        count += 2
    elif odd[num] == 2 :
        count += 1
for num in list(even.keys()) :
    if even[num] > 2 :
        count += 2
    elif even[num] == 2 :
        count += 1
print(count)