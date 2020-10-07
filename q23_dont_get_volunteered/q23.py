# Google Foobar Challenge

"""
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------


Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(0, 1)
Output:
    3

Input:
solution.solution(19, 36)
Output:
    1

"""

def possible_actions(state) :
    actions = []
    # Top Left
    if (state % 8) > 0 and (state // 8) > 1 :
        actions.append((((state // 8) - 2) * 8) + (state % 8) - 1)
    # Top Right
    if (state % 8) < 7 and (state // 8) > 1 :
        actions.append((((state // 8) - 2) * 8) + (state % 8) + 1)
    # Bottom Left
    if (state % 8) > 0 and (state // 8) < 6 :
        actions.append((((state // 8) + 2) * 8) + (state % 8) - 1)
    # Bottom Right
    if (state % 8) < 7 and (state // 8) < 6 :
        actions.append((((state // 8) + 2) * 8) + (state % 8) + 1)
    # Left Top
    if (state % 8) > 1 and (state // 8) > 0 :
        actions.append((((state // 8) - 1) * 8) + (state % 8) - 2)
    # Left Bottom
    if (state % 8) > 1 and (state // 8) < 7 :
        actions.append((((state // 8) + 1) * 8) + (state % 8) - 2)
    # Right Top
    if (state % 8) < 6 and (state // 8) > 0 :
        actions.append((((state // 8) - 1) * 8) + (state % 8) + 2)
    # Right Bottom
    if (state % 8) < 6 and (state // 8) < 7 :
        actions.append((((state // 8) + 1) * 8) + (state % 8) + 2)
    # Removing invalid values
    for action in list(actions) :
        if action < 0 or action > 63 :
            actions.remove(action)
    return actions


def solution(src, dest) :
    if src == dest :
        return 0
    frontier = [(src, 0)]
    visited = []
    while len(frontier) > 0 :
        step = frontier[0]
        frontier = frontier[1:]
        visited.append(step[0])
        actions = possible_actions(step[0])
        if dest in actions :
            return (step[1] + 1)
        for action in possible_actions(step[0]) :
            if action not in visited :
                frontier.append((action, step[1]+1))


print(solution(0, 63))