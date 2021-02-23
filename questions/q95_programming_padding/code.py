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


input_matrix = read_input(input())
padding_locations = input()
padding_layers = int(input())
filter = read_input(input())
s = int(input())

if padding_locations == 'A' :
    height = len(input_matrix) + (2 * padding_layers)
    width = len(input_matrix) + (2 * padding_layers)
else :
    height = len(input_matrix) + (padding_layers if 'T' in padding_locations else 0) + (padding_layers if 'B' in padding_locations else 0)
    width = len(input_matrix) + (padding_layers if 'L' in padding_locations else 0) + (padding_layers if 'R' in padding_locations else 0)
    
    

matrix = []
if 'T' in padding_locations or 'A' in padding_locations :
    for i in range(padding_layers) :
        matrix.append([0 for _ in range(width)])
for i in range(len(input_matrix)) :
    matrix.append([0 for _ in range(padding_layers if ('L' in padding_locations) or ('A' in padding_locations) else 0)] + input_matrix[i] + [0 for _ in range(padding_layers if ('R' in padding_locations) or ('A' in padding_locations) else 0)])
if 'T' in padding_locations or 'A' in padding_locations :
    for i in range(padding_layers) :
        matrix.append([0 for _ in range(width)])
    
    
f = len(filter)


result = []
for i in range(0, height-f+1, s) :
    result.append([])
    for j in range(0, width-f+1, s) :

        # Start the convolution
        summ = 0
        for k in range(f) :
            for l in range(f) :
                summ += (filter[k][l] * matrix[i+k][j+l])
        result[-1].append(summ)

if len(result) == 1 :
    result = result[0]
print(result)
