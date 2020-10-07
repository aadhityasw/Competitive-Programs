# Codechef

# CHFNSWPS
# https://www.codechef.com/problems/CHFNSWPS
# Chefina and Swaps

"""
Chefina has two sequences A1,A2,…,AN and B1,B2,…,BN. She views two sequences with length N as identical if, after they are sorted in non-decreasing order, the i-th element of one sequence is equal to the i-th element of the other sequence for each i (1≤i≤N).

To impress Chefina, Chef wants to make the sequences identical. He may perform the following operation zero or more times: choose two integers i and j (1≤i,j≤N) and swap Ai with Bj. The cost of each such operation is min(Ai,Bj).

You have to find the minimum total cost with which Chef can make the two sequences identical.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers A1,A2,…,AN.
The third line contains N space-separated integers B1,B2,…,BN.
Output
For each test case, print a single line containing one integer ― the minimum cost, or −1 if no valid sequence of operations exists.

Constraints
1≤T≤2,000
1≤N≤2⋅105
1≤Ai,Bi≤109 for each valid i
the sum of N over all test cases does not exceed 2⋅106
Subtasks
Subtask #1 (15 points):

T≤20
N≤20
Subtask #2 (85 points): original constraints

Example Input
3
1
1
2
2
1 2
2 1
2
1 1
2 2
Example Output
-1
0
1
Explanation
Example case 1: There is no way to make the sequences identical, so the answer is −1.

Example case 2: The sequence are identical initially, so the answer is 0.

Example case 3: We can swap A1 with B2, which makes the two sequences identical, so the answer is 1.
"""

#%%

"""test = int(input())
for tes in range(test) :
    n = int(input())
    aarr = list(map(int, input().strip().split()))
    barr = list(map(int, input().strip().split()))
    aetc = {}
    betc = {}
    for i in range(n) :
        if aarr[i] in betc :
            if betc[aarr[i]] > 1 :
                betc[aarr[i]] -= 1
            else :
                del betc[aarr[i]]
        else :
            if aarr[i] in aetc :
                aetc[aarr[i]] += 1
            else :
                aetc[aarr[i]] = 1
        
        if barr[i] in aetc :
            if aetc[barr[i]] > 1 :
                aetc[barr[i]] -= 1
            else :
                del aetc[barr[i]]
        else :
            if barr[i] in betc :
                betc[barr[i]] += 1
            else :
                betc[barr[i]] = 1
    if (any(d%2==1 for d in list(aetc.values())) or any(d%2==1 for d in list(betc.values()))) :
        print(-1)
    else :
        arem = []
        for d in aetc :
            arem += [d]*(int(aetc[d]//2))
        brem = []
        for d in betc :
            brem += [d]*(int(betc[d]//2))
        if len(arem) != len(brem) :
            print(-1)
        else :
            arem = sorted(arem)
            brem = sorted(brem, reverse=True)
            tot = 0
            for i in range(len(arem)) :
                tot += min(arem[i], brem[i])
            print(tot)"""



#%%

"""test = int(input())
for tes in range(test) :
    n = int(input())
    aarr = list(map(int, input().strip().split()))
    barr = list(map(int, input().strip().split()))
    adict = {}
    bdict = {}
    for i in range(10000) :
        adict[i] = {}
        bdict[i] = {}
    for i in range(n) :
        if aarr[i] in adict[aarr[i]%10000] :
            adict[aarr[i]%10000][aarr[i]] += 1
        else :
            adict[aarr[i]%10000][aarr[i]] = 1
        if barr[i] in bdict[barr[i]%10000] :
            bdict[barr[i]%10000][barr[i]] += 1
        else :
            bdict[barr[i]%10000][barr[i]] = 1
    arem = []
    brem = []
    flag = True
    for i in range(10000) :
        akeys = list(adict[i].keys())
        bkeys = list(bdict[i].keys())
        for j in range(len(akeys)) :
            if akeys[j] in bkeys :
                if adict[i][akeys[j]] == bdict[i][akeys[j]] :
                    continue
                else :
                    diff = adict[i][akeys[j]] - bdict[i][akeys[j]]
                    if diff % 2 != 0 :
                        flag = False
                        break
                    else :
                        if diff > 0 :
                            arem += [akeys[j] for _ in range(int(diff//2))]
                        else :
                            brem += [akeys[j] for _ in range(int(diff//2))]
            else :
                diff = adict[i][akeys[j]]
                if diff % 2 != 0 :
                    flag = False
                    break
                else :
                    arem += [akeys[j] for _ in range(int(diff//2))]
        for num in list(set(bkeys) - set(akeys)) :
            diff = bdict[i][num]
            if diff % 2 != 0 :
                flag = False
                break
            else :
                brem += [num for _ in range(int(diff//2))]
        if flag == False :
            break
    if len(arem) != len(brem) :
        flag = False
    if flag :
        cost = 0
        for i in range(len(arem)) :
            cost += min(arem[i], brem[len(brem)-i-1])
        print(cost)
    else :
        print(-1)"""



#%%

"""test = int(input())
for tes in range(test) :
    n = int(input())
    aarr = list(map(int, input().strip().split()))
    barr = list(map(int, input().strip().split()))
    cost = 0
    arem = []
    for i in range(n) :
        try :
            barr.remove(aarr[i])
        except :
            arem.append(aarr[i])
    if len(arem) != len(barr) :
        print(-1)
    else :
        arem.sort()
        barr.sort(reverse=True)
        num = len(arem)
        flag = True
        if num%2 == 1 :
            flag = False
        else :
            for i in range(0, num-1, 2) :
                if (arem[i] != arem[i+1]) or (barr[i] != barr[i+1]) :
                    flag = False
                    break
                cost += min(arem[i], barr[i])
        if flag :
            print(cost)
        else :
            print(-1)"""



#%%


"""test = int(input())
for tes in range(test) :
    n = int(input())
    aarr = list(map(int, input().strip().split()))
    barr = list(map(int, input().strip().split()))
    board = [0 for _ in range(1000000000)]
    for i in range(n) :
        board[aarr[i]-1] += 1
        board[barr[i]-1] -= 1
    numswaps = 0
    flag = True
    for i in range(1000000000) :
        if abs(board[i]) % 2 != 0 :
            flag = False
            break
        if board[i] != 0 :
            numswaps += abs(board[i]) / 2
    if numswaps % 2 != 0 :
        flag = False
    if flag :
        numswaps = numswaps / 2
        i = 0
        cost = 0
        while (numswaps > 0) :
            if board[i] != 0 :
                cost += (i+1) * abs(board[i])
                numswaps -= abs(board[i])
            i += 1
        print(cost)
    else :
        print(-1)"""



#%%

"""test = int(input())
for tes in range(test) :
    n = int(input())
    aarr = list(map(int, input().strip().split()))
    barr = list(map(int, input().strip().split()))
    board = {}
    flag = True
    for i in range(n) :
        try :
            board[aarr[i]] += 1
            if board[aarr[i]] == 0 :
                del board[aarr[i]]
        except :
            board[aarr[i]] = 1
        try :
            board[barr[i]] -= 1
            if board[barr[i]] == 0 :
                del board[barr[i]]
        except :
            board[barr[i]] = -1
    keys = list(board.keys())
    if len(keys) % 2 != 0 :
        flag = False
    if flag :
        numswaps = 0
        for k in keys :
            if board[k] % 2 != 0 :
                flag = False
                break
            numswaps += abs(board[k]) // 2
        if flag :
            numswaps /= 2
            keys = sorted(keys)
            k = 0
            cost = 0
            while numswaps > 0 :
                if abs(board[keys[k]]) > numswaps :
                    cost += numswaps*keys[k]
                else :
                    cost += abs(board[keys[k]])*keys[k]
                numswaps -= abs(board[keys[k]])
                k += 1
    if flag :
        print(int(cost))
    else :
        print(-1)"""



#%%

"""import math

test = int(input())
for tes in range(test) :
    n = int(input())
    aarr = list(map(int, input().strip().split()))
    barr = list(map(int, input().strip().split()))
    row = math.ceil(math.log(max(aarr + barr), 10)) + 1
    # col = pow(10, row_num)
    board = [[0 for _ in range(pow(10, i))] for i in range(row)]
    # Count of extra pairs per shelf
    acount = [0 for _ in range(row)]
    bcount = [0 for _ in range(row)]
    # Count of odd numbered elements per shelf
    aodd = [0 for _ in range(row)]
    bodd = [0 for _ in range(row)]
    for i in range(n) :
        if aarr[i] == barr[i] :
            continue

        # For aarr[i] element
        rkey = math.ceil(math.log(aarr[i], 10))
        if rkey > 0 :
            ckey = aarr[i] - pow(10, rkey-1)
        else :
            ckey = 0
        if board[rkey][ckey] >= 0 :
            if board[rkey][ckey] % 2 == 0 :
                aodd[rkey] += 1
            else :
                aodd[rkey] -= 1
                acount[rkey] += 1
        else :
            if board[rkey][ckey] % 2 == 0 :
                bodd[rkey] += 1
                bcount[rkey] -= 1
            else :
                bodd[rkey] -= 1
        board[rkey][ckey] += 1

        # For barr[i] element
        rkey = math.ceil(math.log(barr[i], 10))
        if rkey > 0 :
            ckey = barr[i] - pow(10, rkey-1)
        else :
            ckey = 0
        if board[rkey][ckey] <= 0 :
            if board[rkey][ckey] % 2 == 0 :
                bodd[rkey] += 1
            else :
                bodd[rkey] -= 1
                bcount[rkey] += 1
        else :
            if board[rkey][ckey] % 2 == 0 :
                acount[rkey] -= 1
                aodd[rkey] += 1
            else :
                aodd[rkey] -= 1
        board[rkey][ckey] -= 1
    #print(board)
    #print(acount)
    #print(bcount)
    if any(aodd) > 0 or any(bodd) > 0 :
        print(-1)
        continue
    else :
        a_total = sum(acount)
        b_total = sum(bcount)
        if a_total == b_total :
            count = a_total
            summ = 0
            for i in range(row) :
                if acount[i] > 0 or bcount[i] > 0 :
                    for j in range(int(pow(10, i))) :
                        if board[i][j] != 0 :
                            ele = abs(board[i][j])
                            if ele >= count :
                                summ += (count * (pow(10, i) + j))
                                count = 0
                                break
                            else :
                                summ += (ele * (pow(10, i) + j))
                                count -= ele
                            if count == 0 :
                                break
                    if count <= 0 :
                        break
            print(summ)
        else :
            print(-1)"""





#%%

test = int(input())
for tes in range(test) :
    n = int(input())
    aarr = list(map(int, input().strip().split()))
    barr = list(map(int, input().strip().split()))
    board = {}
    mini = 0
    for i in range(n) :
        if aarr[i] in board :
            board[aarr[i]] += 1
        else :
            board[aarr[i]] = 1
        if barr[i] in board :
            board[barr[i]] -= 1
        else :
            board[barr[i]] = -1
        mini = min(mini, aarr[i], barr[i])
    flag = True
    arem = []
    brem = []
    for key, val in board.items() :
        if abs(val) % 2 != 0 :
            flag = False
            break
        else :
            if val > 0 :
                arem = arem + [key]*(val // 2)
            elif val < 0 :
                brem = brem + [key]*(abs(val) // 2)
    if flag :
        brem = list(reversed(brem))
        cost = 0
        for i in range(len(arem)) :
            cost += min(2*mini, min(arem[i], brem[i]))
        print(cost)
    else :
        print(-1)
