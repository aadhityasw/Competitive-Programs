# Google FooBar Challenge

# Doomsday Fuel

""" Solutions 3 and 4 works perfectly for all test cases """

"""
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
Output:
    [7, 6, 8, 21]

Input:
solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
Output:
    [0, 3, 2, 9, 14]

"""


"""---------------------------------------------- Solution 1 ----------------------------------------------"""
""" Using Brute Force with custom Fraction Model """



def multiply_fraction(num1, num2) :
    """
    Multiplies two fractional numbers.
    >>> num1 = (numerator1, denominator1)
    """
    res = [0, 0]
    res[0] = num1[0] * num2[0]
    res[1] = num1[1] * num2[1]
    #print('Multiplication : ', num1, num2, simplify_fraction(res))
    return simplify_fraction(res)


def addition_fraction(num1, num2) :
    """
    Adds two fractional numbers.
    >>> num1 = (numerator1, denominator1)
    """
    if num2[0] == 0 or num2[1] == 0 :
        res =  simplify_fraction(num1)
    elif num1[0] == 0 or num1[1] == 0 :
        res =  simplify_fraction(num2)
    else :
        res = [0, 0]
        res[0] = (num1[0] * num2[1]) + (num2[0] * num1[1])
        res[1] = (num1[1] * num2[1])
        res = simplify_fraction(res)
    #print('Addition', num1, num2, res)
    return res


def geometric_progression(a, r) :
    """ 
    Finds the sum of an infinite Geometric Progression series. 
    (Given a and r as tuples whose elements are the numerator and denominator respectively).
    >>> a = (a_numerator, a_denominator)
    """
    res = [0, 0]
    res[0] = a[0] * r[1]
    res[1] = a[1] * (r[1] - r[0])
    #print('Infinite GP ', a, r, res)
    return simplify_fraction(res)


def find_hcf(a, b) :
    """ Finds the Highest Common Factor among two numbers """
    #print('HCF : ', a, b)
    if b == 0 :
        return a
    return find_hcf(b, a%b)


def find_lcm(a, b) :
    """ Finds the Least Common Multiple of two numbers. """
    #print('LCM : ', a, b)
    if a == 0 :
        return b
    elif b == 0 :
        return a
    else :
        return (a*b)//find_hcf(a, b)


def simplify_fraction(number) :
    """
    Reduces a fraction into its simplest form as numerator and denominator
    >>> number = (numerator, denominator)
    """
    #print('Simplification  :  ', number)
    (numerator, denominator) = number
    if numerator == denominator == 0 :
        return number
    hcf = int(find_hcf(numerator, denominator))
    return (numerator//hcf, denominator//hcf)


cycles = set()
def cycle_detection(matrix, path, cost) :
    """ Detects and logs cycles that are present in a graph. """
    if len(path) == 0 :
        for i in range(len(matrix)) :
            cycle_detection(matrix, [i], (1, 1))
    else :
        for i in range(len(matrix[path[-1]])) :
            if (matrix[path[-1]][i] != 0) :
                flag = False
                for (cycle, cost) in cycles :
                    if cycle[0] == path[-1] and cycle[1] == i :
                        flag = True
                        break
                if flag :
                    continue
                if (i == path[0]) :
                    cycles.add((tuple(path), simplify_fraction((cost[0] * matrix[path[-1]][i], cost[1] * sum(matrix[path[-1]])))))
                elif i in path :
                    ind = path.index(i)
                    temp_cost = (1, 1)
                    for j in range(ind, len(path)-1) :
                        temp_cost[0] *= matrix[path[j]][path[j+1]]
                        temp_cost[1] *= sum(matrix[path[j]])
                        temp_cost = simplify_fraction(temp_cost)
                    cycles.add((path[ind:], temp_cost))
                else :
                    cycle_detection(matrix, path+[i], simplify_fraction((cost[0] * matrix[path[-1]][i], cost[1] * sum(matrix[path[-1]]))))


terminals = {}
def extract_terminals(matrix) :
    """ Extracts and logs the terminal states in the graph. """
    for i in range(len(matrix)) :
        flag = True
        for j in range(len(matrix[i])) :
            if matrix[i][j] != 0 :
                flag = False
                break
        if flag :
            terminals[i] = (0, 0)


def search(matrix, path, cost) :
    for i in range(len(matrix)) :
        if (matrix[path[-1]][i] != 0) and (i not in path) :
            if i in terminals :
                flag = True
                for cycle, cycle_cost in cycles :
                    if (path[-1] == cycle[0]) or (path[-1] == cycle[-1]) :
                        flag = False
                        #print(f'For terminal {i} from node {path[-1]} for path {path}')
                        c = geometric_progression(cost, cycle_cost)
                        c = multiply_fraction(c, (matrix[path[-1]][i], sum(matrix[path[-1]])))
                        terminals[i] = addition_fraction(c, terminals[i])
                if flag :
                    c = multiply_fraction(cost, (matrix[path[-1]][i], sum(matrix[path[-1]])))
                    terminals[i] = addition_fraction(c, terminals[i])
            else :
                search(matrix, path+[i], multiply_fraction(cost, (matrix[path[-1]][i], sum(matrix[path[-1]]))))


def normalize_terminals() :
    """
    Normalizes the terminals to have a common denominator.
    """
    lcm = 0
    for (n, d) in terminals.values() :
        if d != 0 :
            lcm = find_lcm(lcm, d)
    #print('LCM ', lcm)
    arr = []
    for key in sorted(list(terminals.keys())) :
        (n, d) = terminals[key]
        if d == 0 :
            arr.append(0)
        else :
            arr.append(n * (lcm // d))
    arr.append(lcm)
    return arr


def solution1(matrix) :
    extract_terminals(matrix)
    cycle_detection(matrix, [], (1, 1))
    search(matrix, [0], (1, 1))
    result = normalize_terminals()
    return result


"""---------------------------------------------- Test Cases (With Solutions) ----------------------------------------------"""


matrix1 = [
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

matrix2 = [
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

matrix3 = [
        [1, 2, 3, 0, 0, 0],
        [4, 5, 6, 0, 0, 0],
        [7, 8, 9, 1, 0, 0],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
# Answer = [1, 2, 3]

matrix4 = [
        [0]
    ]
#Answer = [1, 1]

matrix5 = [
        [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
        [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
        [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
        [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
# Answer = [1, 2, 3, 4, 5, 15]

matrix6 = [
        [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
        [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
        [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
# Answer = [4, 5, 5, 4, 2, 20]

matrix7 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
# Answer = [1, 1, 1, 1, 1, 5]

matrix8 = [
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
# Answer = [2, 1, 1, 1, 1, 6]

matrix9 = [
        [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
        [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
        [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
# Answer = [6, 44, 4, 11, 22, 13, 100]

matrix10 = [
        [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
        [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
        [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
        [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
# Answer = [1, 1, 1, 2, 5]


#print(solution(matrix3))




"""---------------------------------------------- Solution 2 ----------------------------------------------"""
""" Using principle of Markow Chains with custom Fraction models """

def extract_terminals_mod(matrix) :
    """ Extracts and logs the terminal states in the graph. """
    terminals = []
    for i in range(len(matrix)) :
        flag = True
        for j in range(len(matrix[i])) :
            if matrix[i][j] != 0 :
                flag = False
                break
        if flag :
            terminals.append(i)
    return terminals


def make_probability_matrix(matrix) :
    prob_matrix = []
    for i in range(len(matrix)) :
        flag = True
        for j in range(len(matrix[i])) :
            if matrix[i][j] != 0 :
                flag = False
                break
        if not flag :
            summ = sum(matrix[i])
            row = []
            for j in matrix[i] :
                if j == 0:
                    row.append((0, 0))
                else :
                    row.append((j, summ))
        else :
            # All are zeros.
            row = [(0, 0) for _ in range(len(matrix))]
            row[i] = (1, 1)
        prob_matrix.append(row)
    return prob_matrix


def normalize_terminal_vector(terminals) :
    lcm = 0
    for (n, d) in terminals :
        if d != 0 :
            lcm = find_lcm(lcm, d)
    #print('LCM ', lcm)
    arr = []
    for (n, d) in terminals :
        if d == 0 :
            arr.append(0)
        else :
            arr.append(n * (lcm // d))
    arr.append(lcm)
    return arr


def solution2(matrix) :
    if len(matrix) == 1:
        return [1, 1]
    prob_matrix = make_probability_matrix(matrix)
    vector = list(prob_matrix[0])
    print('Probability Matrix : ', prob_matrix)
    for itr in range(100) :
        vector2 = [(0, 0) for _ in range(len(matrix))]
        for col in range(len(matrix)) :
            #print('Column', col)
            for i in range(len(vector)) :
                vector2[col] = addition_fraction(vector2[col], multiply_fraction(vector[i], prob_matrix[i][col]))
                #print('Modified vector element : ', vector2[col])
        #print('Vector', vector)
        if vector2 == vector :
            break
        vector = vector2
    terminal_states = extract_terminals_mod(matrix)
    i = 0
    p = 0
    while i<len(vector) :
        if p not in terminal_states :
            vector = vector[:i] + vector[i+1:]
        else :
            i += 1
        p += 1
    return normalize_terminal_vector(vector)



"""---------------------------------------------- Solution 3 ----------------------------------------------"""
""" Using Markow Chain Principle with handling decimal numbers """

import fractions


def make_probability_matrix_decimals(matrix) :
    prob_matrix = []
    for i in range(len(matrix)) :
        flag = True
        for j in range(len(matrix[i])) :
            if matrix[i][j] != 0 :
                flag = False
                break
        if not flag :
            summ = sum(matrix[i])
            row = []
            for j in matrix[i] :
                if j == 0:
                    row.append(0)
                else :
                    row.append(j/summ)
        else :
            # All are zeros.
            row = [0] * len(matrix)
            row[i] = 1
        prob_matrix.append(row)
    return prob_matrix


def solution3(matrix) :
    if len(matrix) == 1:
        return [1, 1]
    prob_matrix = make_probability_matrix_decimals(matrix)
    vector = list(prob_matrix[0])
    #print('Probability Matrix : ', prob_matrix)
    for itr in range(100) :
        vector2 = [0] * len(matrix)
        for col in range(len(matrix)) :
            #print('Column', col)
            for i in range(len(vector)) :
                vector2[col] += (vector[i] * prob_matrix[i][col])
                #print('Modified vector element : ', vector2[col])
        #print('Vector', vector)
        if vector2 == vector :
            break
        vector = vector2
    terminal_states = extract_terminals_mod(matrix)
    i = 0
    p = 0
    while i<len(vector) :
        if p not in terminal_states :
            vector = vector[:i] + vector[i+1:]
        else :
            i += 1
        p += 1
    #print('Vector', vector)
    fractional_vectors = [fractions.Fraction(v).limit_denominator() for v in vector]
    #print('Fractional Vectors : ', fractional_vectors)

    max_d = 0
    lcm = 1
    for fac in fractional_vectors :
        if fac.denominator > max_d :
            max_d = fac.denominator
        lcm = find_lcm(lcm, fac.denominator)
    arr = []
    for fac in fractional_vectors :
        arr.append(int(fac.numerator * lcm / fac.denominator))
    div_factor = 1
    for i in range(len(arr)) :
        flag = True
        if arr[i] == 0 :
            continue
        for j in range(len(arr)) :
            if i == j :
                continue
            else :
                if arr[j] % arr[i] != 0 :
                    flag = False
                    break
        if flag :
            div_factor = arr[i]
            for j in range(len(arr)) :
                arr[j] = arr[j] // div_factor
            break
    arr.append(lcm // div_factor)
    return arr


#print(solution3(matrix1))



"""---------------------------------------------- Solution 4 ----------------------------------------------"""
""" Using Absorbing Markow Chain Principle """


from fractions import Fraction

def gcd(x, y):
    def gcd1(x, y):
        if y == 0:
            return x
        return gcd1(y, x%y)
    return gcd1(abs(x), abs(y))

def simplify(x, y):
    g = gcd(x, y)
    return Fraction(x/g, y/g)

def lcm(x, y):
    return x*y/gcd(x,y)

def transform(mat):
    sum_list = list(map(sum, mat))
    bool_indices = list(map(lambda x: x == 0, sum_list))
    indices = set([i for i, x in enumerate(bool_indices) if x])
    new_mat = []
    for i in range(len(mat)):
        new_mat.append(list(map(lambda x: Fraction(0, 1) if(sum_list[i] == 0) else simplify(x, sum_list[i]), mat[i])))
    transform_mat = []
    zeros_mat = []
    for i in range(len(new_mat)):
        if i not in indices:
            transform_mat.append(new_mat[i])
        else:
            zeros_mat.append(new_mat[i])
    transform_mat.extend(zeros_mat)
    tmat = []
    for i in range(len(transform_mat)):
        tmat.append([])
        extend_mat = []
        for j in range(len(transform_mat)):
            if j not in indices:
                tmat[i].append(transform_mat[i][j])
            else:
                extend_mat.append(transform_mat[i][j])
        tmat[i].extend(extend_mat)
    return [tmat, len(zeros_mat)]

def copy_mat(mat):
    cmat = []
    for i in range(len(mat)):
        cmat.append([])
        for j in range(len(mat[i])):
            cmat[i].append(Fraction(mat[i][j].numerator, mat[i][j].denominator))
    return cmat

def gauss_elmination(m, values):
    mat = copy_mat(m)
    for i in range(len(mat)):
        index = -1
        for j in range(i, len(mat)):
            if mat[j][i].numerator != 0:
                index = j
                break
        if index == -1:
            raise ValueError('Gauss elimination failed!')
        mat[i], mat[index] = mat[index], mat[j]
        values[i], values[index] = values[index], values[i]
        for j in range(i+1, len(mat)):
            if mat[j][i].numerator == 0:
                continue
            ratio = -mat[j][i]/mat[i][i]
            for k in range(i, len(mat)):
                mat[j][k] += ratio * mat[i][k]
            values[j] += ratio * values[i]
    res = [0 for i in range(len(mat))]
    for i in range(len(mat)):
        index = len(mat) -1 -i
        end = len(mat) - 1
        while end > index:
            values[index] -= mat[index][end] * res[end]
            end -= 1
        res[index] = values[index]/mat[index][index]
    return res

def transpose(mat):
    tmat = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == 0:
                tmat.append([])
            tmat[j].append(mat[i][j])
    return tmat

def inverse(mat):
    tmat = transpose(mat)
    mat_inv = []
    for i in range(len(tmat)):
        values = [Fraction(int(i==j), 1) for j in range(len(mat))]
        mat_inv.append(gauss_elmination(tmat, values))
    return mat_inv

def mat_mult(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            res[i].append(Fraction(0, 1))
            for k in range(len(mat1[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res

def splitQR(mat, lengthR):
    lengthQ = len(mat) - lengthR
    Q = []
    R = []
    for i in range(lengthQ):
        Q.append([int(i==j)-mat[i][j] for j in range(lengthQ)])
        R.append(mat[i][lengthQ:])
    return [Q, R]

def answer(mat):
    res = transform(mat)
    if res[1] == len(mat):
        return [1, 1]
    Q, R = splitQR(*res)
    inv = inverse(Q)
    res = mat_mult(inv, R)
    row = res[0]
    l = 1
    for item in row:
        l = lcm(l, item.denominator)
    res = list(map(lambda x: x.numerator*l/x.denominator, row))
    res.append(l)
    return res