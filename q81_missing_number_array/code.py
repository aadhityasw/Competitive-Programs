def MissingNumber(array,n) :
    return (n * (n+1) // 2) - sum(array)


def MissingNumber2(array, n) :
    """ In case we get a very large integer in the summation process """
    summ = 0
    for i in range(n-1) :
        summ += array[i] - (i+1)
    return n - summ


def MissingNumber3(array, n) :
    """ In case we can use an XOR operation """

    x1 = array[0]
    x2 = 1

    for i in range(1, n-1) :
        x1 = x1 ^ array[i]

    for i in range(2, n+1) :
        x2 = x2 ^ i
    
    return x1 ^ x2
