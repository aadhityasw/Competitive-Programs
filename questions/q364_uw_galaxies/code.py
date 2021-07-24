


"""
def calculateCapacitance(G) :
    capacitance = []
    for i in range(1, len(G)) :
        capacitance.append(G[i] * G[i-1])
    
    return capacitance


def calculatePotential(G) :
    potential = []
    for i in range(1, len(G)) :
        potential.append(G[i] - G[i-1])
    
    return potential


def calculateInductance(G) :
    inductance = []
    for i in range(1, len(G)) :
        inductance.append(G[i] + G[i-1])

    return inductance


def calculateUWValue(G) :
    capacitance = calculateCapacitance(G)
    potential = calculatePotential(G)
    inductance = calculateInductance(G)
    
    v1 = [i*i for i in capacitance]
    v2 = [i - j for (i, j) in zip(v1, inductance)]
    v3 = [i*j for (i, j) in zip(potential, v2)]
    uw_value = abs(sum(v3))
    
    return uw_value

"""





def calculateCost(v1, v2) :
    return abs(v1**3 - v2**3)



n = int(input())
alien = []
human = []
gravities = []
for i in range(n) :
    inp = input().strip().split()
    gravity = int(inp[0])
    species = inp[1]
    gravities.append(gravity)
    if species == 'a' :
        alien.append(i)
    else :
        human.append(i)

graph = {}
num_edges = int(input())
for _ in range(num_edges) :
    u, v = map(int, input().strip().split())
    if u-1 in graph :
        graph[u-1].add(v-1)
    else :
        graph[u-1] = {v-1}
    if v-1 in graph :
        graph[v-1].add(u-1)
    else :
        graph[v-1] = {u-1}
    
human.sort(key=lambda x : gravities[x])
alien.sort(key=lambda x : gravities[x])

# For each human visit all aliens
min_cost = float("inf")

while len(human) > 0 and len(alien) > 0 :

    i = human[-1]
    j = alien[-1]
    val1 = gravities[i]
    val2 = gravities[j]

    cur_cost = calculateCost(val1, val2)

    if j in graph[i] :
        if val1 > val2 :
            cur_cost = min(cur_cost, calculateCost(val1-1, val2+1))
            for v in graph[j] :
                if v == i :
                    continue
                if v in graph[i] :
                    cur_cost = min(cur_cost, calculateCost(val1, val2+1))
                    break

        else :
            cur_cost = min(cur_cost, calculateCost(val1+1, val2-1))
            for v in graph[i] :
                if v == j :
                    continue
                if v in graph[j] :
                    cur_cost = min(cur_cost, calculateCost(val1+1, val2))
                    break
    
    else :
        if val1 > val2 :
            cur_cost = min(cur_cost, calculateCost(val1-1, val2))
        else :
            cur_cost = min(cur_cost, calculateCost(val1, val2-1))
    
    min_cost = min(min_cost, cur_cost)

    if val2 > val1 :
        alien.pop()
    else :
        human.pop()


print(min_cost)
