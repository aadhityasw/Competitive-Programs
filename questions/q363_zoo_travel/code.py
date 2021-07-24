n = int(input())
costs = list(map(int, input().strip().split()))

# Sort the costs
costs.sort()

total_cost = 0

i = n-1
while i > 2 :
    total_cost += min(
        costs[i] + costs[0] + costs[i-1] + costs[0],
        costs[1] + costs[0] + costs[i] + costs[1]
    )
    i -= 2

if i == 2 :
    # Person 0 goes with Person 1 with the latter's charge, Person 0 comes back and goes with Person 2 with latter's charge
    total_cost += costs[1] + costs[0] + costs[2]
elif i == 1 :
    # first person has more cost than person 0
    total_cost += max(costs[0], costs[1])
else :
    # The only person rides alone
    total_cost += costs[0]

print(total_cost)
