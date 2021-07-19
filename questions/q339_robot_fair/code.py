# You are using Python


def shiftLeft(direction) :
    left_shift = {
        'N' : 'W',
        'E' : 'N',
        'S' : 'E',
        'W' : 'S'
    }
    return left_shift[direction]


def shiftRight(direction) :
    right_shift = {
        'N' : 'E',
        'E' : 'S',
        'S' : 'W',
        'W' : 'N'
    }
    return right_shift[direction]
    

def makeMove(position, direction) :
    if direction == 'N' :
        return (position[0]-1, position[1])
    elif direction == 'E' :
        return (position[0], position[1]+1)
    elif direction == 'W' :
        return (position[0], position[1]-1)
    elif direction == 'S' :
        return (position[0]+1, position[1])


def validateMove(position, matrix) :
    
    r, c = len(matrix), len(matrix[0])
    if (0 <= position[0] < r) and (0 <= position[1] < c) and (matrix[position[0]][position[1]] is None) : 
        return True
    
    return False


def findPath(matrix, position, direction, path, final_positions) :
    if len(path) == 0 :
        final_positions.add(tuple(position))
        #print("end", position)
        return
    #print(position, path, direction)
    
    matrix[position[0]][position[1]] = 'Y'
    
    cur_option = path[0]
    if cur_option == 'L' :
        findPath(matrix, position, shiftLeft(direction), path[1:], final_positions)
    elif cur_option == 'R' :
        findPath(matrix, position, shiftRight(direction), path[1:], final_positions)
    elif cur_option == 'F' :
        new_position = makeMove(position, direction)
        if validateMove(new_position, matrix) :
            findPath(matrix, new_position, direction, path[1:], final_positions)
    
    matrix[position[0]][position[1]] = None



row, col = map(int, input().strip().split())
matrix = []
for i in range(row) :
    cur_row = [None if ch == '.' else ch for ch in list(input().strip().split())]
    matrix.append(cur_row)

initial_position = list(map(int, input().strip().split()))

num_path = int(input())
path = input().strip()

final_positions = set()

available_directions = ['N', 'S', 'E', 'W']

for dire in available_directions :
    findPath(matrix, initial_position, dire, path, final_positions)

final_positions = list(final_positions)
final_positions.sort()
for x, y in final_positions :
    print(x, y)
