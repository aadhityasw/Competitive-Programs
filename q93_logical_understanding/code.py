def split(n) :
    n1 = n // 2
    n2 = n // 3
    n3 = n // 4
    
    if n1 > 10 :
        n1 = split(n1)
    if n2 > 10 :
        n2 = split(n2)
    if n3 > 10 :
        n3 = split(n3)
    
    return n1+n2+n3


n = int(input())

print(split(n))
