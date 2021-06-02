from collections import Counter

n, k = map(int, input().strip().split())
candy_colors_index = list(map(int, input().strip().split()))
candy_preferences = list(map(int, input().strip().split()))
happiness_scores = list(map(int, input().strip().split()))

colors_available = Counter(candy_colors_index)
total_happiness = 0

for i, color in enumerate(candy_preferences) :
    # We can use k candies if more is available, else use the number of preferred candies available
    use = min(k, colors_available[color])
    if use > 0 :
        total_happiness += happiness_scores[use-1]
    colors_available[color] -= use

print(total_happiness)
