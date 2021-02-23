# Codechef

# DRCHEF
# https://www.codechef.com/problems/DRCHEF
# Doctor Chef

"""
Chef is multi-talented. He has developed a cure for coronavirus called COVAC-19. Now that everyone in the world is infected, it is time to distribute it throughout the world efficiently to wipe out coronavirus from the Earth. Chef just cooks the cure, you are his distribution manager.

In the world, there are N countries (numbered 1 through N) with populations a1,a2,…,aN. Each cure can be used to cure one infected person once. Due to lockdown rules, you may only deliver cures to one country per day, but you may choose that country arbitrarily and independently on each day. Days are numbered by positive integers. On day 1, Chef has x cures ready. On each subsequent day, Chef can supply twice the number of cures that were delivered (i.e. people that were cured) on the previous day. Chef cannot supply leftovers from the previous or any earlier day, as the cures expire in a day. The number of cures delivered to some country on some day cannot exceed the number of infected people it currently has, either.

However, coronavirus is not giving up so easily. It can infect a cured person that comes in contact with an infected person again ― formally, it means that the number of infected people in a country doubles at the end of each day, i.e. after the cures for this day are used (obviously up to the population of that country).

Find the minimum number of days needed to make the world corona-free.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and x.
The second line contains N space-separated integers a1,a2,…,aN.
Output
For each test case, print a single line containing one integer ― the minimum number of days.

Constraints
1≤T≤103
1≤N≤105
1≤ai≤109 for each valid i
1≤x≤109
the sum of N over all test cases does not exceed 106
Subtasks
Subtask #1 (20 points): a1=a2=…=aN
Subtask #2 (80 points): original constraints

Example Input
3
5 5
1 2 3 4 5
5 1
40 30 20 10 50
3 10
20 1 110
Example Output
5
9
6
"""


#%%

"""test = int(input())
for tes in range(test) :
    n, x = map(int, input().strip().split())
    population = list(map(int, input().strip().split()))
    arr = list(population)
    days = 0
    count = n
    while(count > 0) :
        if x >= max(arr) :
            days += count
            break
        ma = float("inf")
        mapos = -1
        for i in range(n) :
            if arr[i] == x :
                mapos = i
                break
            elif arr[i] > x :
                if arr[i]-x < ma :
                    ma = arr[i]-x
                    mapos = i
        if mapos == -1 :
            ma = 0
            for i in range(n) :
                if arr[i] >= ma :
                    ma = arr[i]
                    mapos = i
        if arr[mapos] == x :
            arr[mapos] = 0
            x *= 2
            count -= 1
        elif arr[mapos] > x :
            arr[mapos] -= x
            x *= 2
        else :
            x = arr[mapos] * 2
            arr[mapos] = 0
            count -= 1
        print("Before", arr)
        for i in range(n) :
            if arr[i] * 2 < population[i] :
                arr[i] *= 2
            else :
                arr[i] = population[i]
        days += 1
        print("After", arr)
        print()
    print(days)"""


#%%

"""test = int(input())
for tes in range(test) :
    n, x = map(int, input().strip().split())
    population = list(map(int, input().strip().split()))
    arr = list(population)
    days = 0
    count = n
    while(count > 0) :
        if x >= max(arr) :
            days += count
            break
        mapos = -1
        ma = 0
        maxpos = 0
        for i in range(n) :
            if arr[i] == x :
                mapos = i
                break
            elif arr[i] < x and arr[i] >= ma :
                ma = arr[i]
                mapos = i
            if arr[i] > arr[maxpos] :
                maxpos = i
        if mapos == -1 :
            mapos = maxpos
        if arr[mapos] == x :
            arr[mapos] = 0
            x *= 2
            count -= 1
        elif arr[mapos] > x :
            arr[mapos] -= x
            x *= 2
        else :
            x = arr[mapos] * 2
            arr[mapos] = 0
            count -= 1
        print("Before", arr)
        for i in range(n) :
            if arr[i] * 2 < population[i] :
                arr[i] *= 2
            else :
                arr[i] = population[i]
        days += 1
        print("After", arr)
        print()
    print(days)"""



#%%

"""test = int(input())
for tes in range(test) :
    n, x = map(int, input().strip().split())
    population = list(map(int, input().strip().split()))
    arr = list(population)
    days = 0
    count = n
    while(count > 0) :
        if x >= max(arr) :
            days += count
            break
        # To get the largest number less than x
        downpos = -1
        downele = 0
        # To get the smallest number greater than x
        uppos = -1
        upele = 0
        for i in range(n) :
            if arr[i] == x :
                downpos = i
                uppos = i
                break
            elif arr[i] < x :
                if downpos == -1 :
                    downpos = i
                    downele = x - arr[i]
                else :
                    if arr[i] > arr[downpos] :
                        downpos = i
                        downele = x - arr[i]
            else :
                if uppos == -1 :
                    uppos = i
                    upele = arr[i] - x
                else :
                    if arr[i] < arr[uppos] :
                        uppos = i
                        upele = arr[i] - x
        if downpos == uppos :
            mapos = downpos
        elif downpos == -1 :
            mapos = uppos
        elif uppos == -1 :
            mapos = downpos
        elif upele < downele :
            mapos = uppos
        else :
            mapos = downpos
        print("x=", x, "upele=", upele, "uppos=", uppos, "downele=", downele, "downpos=", downpos, "mapos=", mapos)
        if arr[mapos] == x :
            arr[mapos] = 0
            x *= 2
            count -= 1
        elif arr[mapos] > x :
            arr[mapos] -= x
            x *= 2
        else :
            x = arr[mapos] * 2
            arr[mapos] = 0
            count -= 1
        print("Before", arr)
        for i in range(n) :
            if arr[i] * 2 < population[i] :
                arr[i] *= 2
            else :
                arr[i] = population[i]
        days += 1
        print("After", arr)
        print()
    print(days)"""


#%%

"""import math

test = int(input())
for tes in range(test) :
    n, x = map(int, input().strip().split())
    population = list(map(int, input().strip().split()))
    maxi = max(population)
    maxi = maxi / x
    maxi = math.ceil(math.log2(maxi))
    maxi += n
    print(maxi)"""



#%%

test = int(input())
for tes in range(test) :
    n, x = map(int, input().strip().split())
    population = list(map(int, input().strip().split()))
    arr = list(population)
    count = n
    days = 0
    while(count > 0) :
        maxi = -1
        downpos = -1
        mapos = -1
        for i in range(n) :
            if arr[i] == 0 :
                continue
            elif arr[i] == x :
                mapos = i
                break
            elif arr[i] < x and (2 * arr[i]) > x :
                if downpos == -1 :
                    downpos = i
                elif arr[downpos] < arr[i] :
                    downpos = i
            if maxi == -1 :
                maxi = i
            elif arr[maxi] < arr[i] :
                maxi = i
        if i==n-1 and  x >= arr[maxi] :
            days += count
            break
        if mapos == -1 :
            if downpos != -1 :
                mapos = downpos
            else :
                mapos = maxi
        if arr[mapos] == x :
            arr[mapos] = 0
            x *= 2
            count -= 1
        elif arr[mapos] > x :
            arr[mapos] -= x
            x *= 2
        else :
            x = arr[mapos] * 2
            arr[mapos] = 0
            count -= 1
        print("Before", arr)
        for i in range(n) :
            if arr[i] * 2 < population[i] :
                arr[i] *= 2
            else :
                arr[i] = population[i]
        days += 1
        print("x=", x, "maxi=", maxi, "downpos=", downpos, "mapos=", mapos)
        print("After", arr)
        print()
    print(days)




#%%

import math

test = int(input())
for tes in range(test) :
    n, x = map(int, input().strip().split())
    population = list(map(int, input().strip().split()))
    maxinum = max(population)
    count = n
    shelf_count = math.floor(math.log2(maxinum))
    count_arr = [0] * (shelf_count+1)
    board = [[] for _ in range(shelf_count+1)]
    for i in range(n) :
        key = math.floor(math.log2(population[i]))
        board[key].append(population[i])
        count_arr[key] += 1
    days = 0
    while count > 0 :
        if x >= maxinum :
            days += count
            break
        key = math.floor(math.log2(x))
        if x in board[key] :
            board[key].remove(x)
            count -= 1
            x *= 2
            days += 1
            continue
        flag = False
        num = 0
        numpos = -1
        for i in board[key] :
            if i < x and (i*2) > x :
                if flag == False :
                    num = i
                    numpos = key
                    flag = True
                else :
                    if i > num :
                        num = i
                        numpos = key
        if flag == False :
            if key > 0 and len(board[key-1]) > 0 and (max(board[key-1])*2) > x :
                num = max(board[key-1])
                numpos = key-1
                flag = True
        if flag :
            board[numpos].remove(num)
            x = num*2
            count -= 1
        else :
            x *= 2
        days += 1
    print(days)
