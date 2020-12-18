def romanToDecimal(s):
    num = 0
    i = 0
    translation = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    
    while i < len(s) :
        if i<len(s)-1 and roman.index(s[i]) <= roman.index(s[i+1]) :
            temp_sum = translation[s[i]]
            temp_num = s[i]
            i += 1
            while i < len(s) and s[i] == temp_num :
                temp_sum += translation[s[i]]
                i += 1
            while i < len(s) and roman.index(s[i]) > roman.index(temp_num) :
                temp_sum = translation[s[i]] - temp_sum
                temp_num = s[i]
                i += 1
            num += temp_sum
        else :
            num += translation[s[i]]
            i += 1
    
    return num


if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        print(romanToDecimal(str(input())))
