def numberOf2s(num, d):
    
    current_digit = (num // int(10 ** d)) % 10
    round_down = num - num % int(10 ** (d + 1))
    
    if current_digit < 2 :
        return round_down // 10
    
    if current_digit == 2 :
        right_portion = num % int(10 ** d)
        return round_down // 10 + right_portion + 1
    
    round_up = round_down + int(10 ** (d+1))
    return round_up // 10
    
    
def numberOf2sinRange(num):
    
    count = 0
    n = len(str(num))
    
    for i in range(n) :
        count += numberOf2s(num, i)
    
    return count





if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        print(numberOf2sinRange(n))
