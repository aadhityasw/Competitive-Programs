def read_input(s) :
    rows = s[1:-1].split(']')
    matrix = []
    for r in rows :
        if len(r) == 0 :
            continue
        if r[0] == ',' :
            r_str = r[3:]
        else :
            r_str = r[1:]
        row = list(map(int, r_str.split(', ')))
        matrix.append(row)
    return matrix

num_matrices = int(input())
s = int(input())
filter = read_input(input())
f = len(filter)
m = int(input())


for tes in range(num_matrices) :
    matrix = read_input(input())
    
    r = 0
    c = 0
    result = []
    for i in range(0, m-f+1, s) :
        result.append([])
        for j in range(0, m-f+1, s) :
            
            # Start the convolution
            summ = 0
            for k in range(f) :
                for l in range(f) :
                    summ += (filter[k][l] * matrix[i+k][j+l])
            result[-1].append(summ)
    
    print(result)
