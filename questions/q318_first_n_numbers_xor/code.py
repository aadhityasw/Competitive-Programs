def computeXOR(n) :
 
    # if n is multiple of 4
    if n % 4 == 0 :
        return n
 
    # If n % 4 gives remainder 1
    if n % 4 == 1 :
        return 1
 
    # If n%4 gives remainder 2
    if n % 4 == 2 :
        return n + 1
 
    # If n%4 gives remainder 3
    return 0
 


n = int(input())
print(computeXOR(n))
