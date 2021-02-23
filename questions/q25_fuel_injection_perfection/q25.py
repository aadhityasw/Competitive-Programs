# Google Foobar Challenge

"""
Fuel Injection Perfection
=========================

Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly. 

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

The fuel control mechanisms have three operations: 

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution('15')
Output:
    5

Input:
solution.solution('4')
Output:
    2

"""


import math
store = {}
store[1] = 0


def recursive_solution(num, steps) :
    if num in store :
        return steps + store[num]
    elif (math.log(num)/math.log(2)% 1) == 0 :
        val = steps + int(math.log(num)/math.log(2))
        store[num] = int(math.log(num)/math.log(2))
    elif num%2 == 0 :
        val = recursive_solution(num//2, steps+1)
        store[num] = val - steps
    else :
        val = min(
            recursive_solution(num-1, steps+1),
            recursive_solution(num+1, steps+1),
        )
        store[num] = val - steps
    return val


def possible_actions(num, steps) :
    if num in store :
        return [(1, steps + store[num])]
    elif (math.log(num)/math.log(2)% 1) == 0 :
        val = steps + int(math.log(num)/math.log(2))
        store[num] = int(math.log(num)/math.log(2))
        return [(1, val)]
    elif num%2 == 0 :
        return [(num//2, steps+1)]
    else :
        return [(num-1, steps+1), (num+1, steps+1)]


def solution(s) :
    num = int(s)
    #return recursive_solution(num, 0)
    """frontier = [(num, 0)]
    while len(frontier) > 0 :
        step = frontier[0]
        frontier = frontier[1:]
        if step[0] == 1 :
            return step[1]
        actions = possible_actions(step[0], step[1])
        for action in actions :
            if action[0] == 1 :
                return(action[1])
            else :
                frontier.append(action)"""
    step = 0
    while num > 1 :
        if (num & 1) == 0 :
            num = num >> 1
        else :
            a = num+1
            b = num-1
            ac = 0
            bc = 0
            while (a & 1) == 0 :
                a = a >> 1
                ac += 1
            while (b & 1) == 0 :
                b = b >> 1
                bc += 1
            if ac > bc and num != 3 :
                num = num + 1
            else :
                num = num - 1
        step += 1
    return step


#print(solution('768'))


print(solution('54533113435565767878343355321435454545331134355657678786573756123242342343355321435454545331134355657678786573756123242342343355321435454545331134355657678786573756343355321435454545331134355657678786573756123242342343355321435454545331134355657678786573756123242342343355321435454545331134355657678786573756'))

