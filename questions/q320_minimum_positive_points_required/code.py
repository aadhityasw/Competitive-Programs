# You are using Python


def getCandidatePositions(dimensions, pos) :
    m, n = dimensions
    r, c = pos
    
    candidate = []
    if r+1 < m :
        candidate.append((r+1, c))
    if c+1 < n :
        candidate.append((r, c+1))
    return candidate



def findMinInitialPoints(matrix, dimensions, current_position, required_initial_points, current_positive) :
    
    # Decode dimensions and current position
    m, n = dimensions
    r, c = current_position
    
    #print(r, c, required_initial_points, current_positive)
    
    # If we have reached the end, save the value if necessary
    if r == m-1 and c == n-1 :
        if matrix[r][c] < 0 :
            diff = matrix[r][c] + current_positive
            if diff < 0 :
                required_initial_points += -1*diff
        #print("final", required_initial_points)
        return required_initial_points +1
    
    if matrix[r][c] > 0 :
        current_positive += matrix[r][c]
    else :
        diff = matrix[r][c] + current_positive
        if diff < 0 :
            current_positive = 0
            required_initial_points += -1*diff
        else :
            current_positive = diff
    
    answer = float("inf")
    for (i, j) in getCandidatePositions(dimensions, current_position) :
        answer = min(
            answer, 
            findMinInitialPoints(matrix, dimensions, (i, j), required_initial_points, current_positive)
        )
    
    return answer





input_array = list(map(int, input().strip().split()))
m, n = input_array[0], input_array[1]
matrix = [[0 for _ in range(n)] for _ in range(m)]
for i, num in enumerate(input_array[2:]) :
    matrix[i//n][i%n] = num

ans = findMinInitialPoints(matrix, (m, n), (0, 0),0, 0)
print(ans)
