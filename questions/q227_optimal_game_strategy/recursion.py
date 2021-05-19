def recursivePlay(arr, n, front, end) :
    if front == end :
        return arr[front]
    elif front == end - 1 :
        return max(arr[front], arr[end])
    else :
        return max(
            arr[front] + min(                           # We choose from front
                recursivePlay(arr, n, front+2, end),        # Opponent chooses from next front
                recursivePlay(arr, n, front+1, end-1)       # Opponent chooses from end
            ),
            arr[end] + min(                             # We choose from end
                recursivePlay(arr, n, front, end-2),        # Opponent chooses from next front
                recursivePlay(arr, n, front+1, end-1)       # Opponent chooses from end
            ),
        )


def optimalStrategyOfGame(arr, n):

    return recursivePlay(arr, n, 0, n-1)
