def traverse(heights, cur, green, red, noRed=False) :
    
    n = len(heights) - 1

    while cur < n :
        if heights[cur] > heights[cur + 1] :
            # If the current height is more, then we cut it once
            red.append(heights[cur] - heights[cur + 1])
            heights[cur] = heights[cur+1]
            cur += 1
        elif heights[cur] == heights[cur + 1] :
            # If the next height is equal, then we make a move
            cur += 1
        else :
            # If the current height is less, then we have options to add any number of green bricks, or add a red and then any number of green bricks
            if green > 0 :
                # We add a green brick if we have any left
                heights[cur] += 1
                # If we have just added a red brick in the place where this function was called, then we cannot add any more red bricks in this current tower
                choice = traverse(heights, cur, green-1, red, noRed=noRed)
                heights[cur] -= 1
                if choice :
                    return True
            if len(red) > 0 and noRed == False:
                # We add a red brick if we have any left, and if we have not yet added any red brick in the current tower
                heights[cur] += red[-1]
                # We add a red brick, and send a parameter so that we cannot add any more red bricks on this tower
                ans = traverse(heights, cur, green, red[:-1], noRed=True)
                heights[cur] -= red[-1]
                if ans :
                    return True
            return False
        
        # If we have already added a red brick, then we cannot add another again, we can add only green bricks,
        # But if we move on to the next tower, then we can add a new red brick there if needed
        noRed = False
    
    if cur >= n-1 :
        return True
    return False





n, m = map(int, input().strip().split())
heights = list(map(int, input().strip().split()))
ans = traverse(heights, 0, m, [])
if ans :
    print("YES")
else :
    print("NO")
