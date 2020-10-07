# Codechef - TRPLSRT
# https://www.codechef.com/problems/TRPLSRT

def findnextpos(arr, pos) :
    # Finds the next number that is out of order from position pos and to its right.
    """print(arr, pos)"""
    for i in range(pos, len(arr)) :
        if arr[i] != (i+1) :
            return i
    return len(arr)

"""def findele(arr, ele, pos) :
    # Finds the position of pos element in the array.
    for i in range(pos, len(arr)) :
        if arr[i] == ele :
            return i
    return len(arr)"""

testcase = int(input())
for tes in range(testcase) :
    (n, k) = map(int, input().strip().split(' '))
    parr = list(map(int, input().strip().split(' ')))
    parr_orig = parr.copy()
    pos = 0
    kcount = 0
    result = []
    finding_pos = 0
    while (kcount <= k) and (pos < n) :
        if pos >= finding_pos :
            finding_pos = pos+1
        if parr[pos] == (pos+1) :
            pos += 1
            continue
        else :
            # element is { indexToArrange : (value, position) }
            marr = {}

            b1 = -1
            b2 = -1
            marr[1] = (parr[pos], pos)
            marr[2] = (parr[marr[1][0]-1], marr[1][0]-1)
            if (marr[2][0]) == (marr[1][1] + 1) :
                b0 = finding_pos
                b1 = findnextpos(parr, finding_pos)
                if b1 == marr[2][1] :
                    b2 = findnextpos(parr, marr[2][1]+1)
                    b = b2
                else :
                    b = b1
                if b >= n :
                    kcount = k+3
                    break
            else :
                b = marr[2][0]-1
            marr[3] = (parr[b], b)


            """marr[2] = (parr[pos], pos)
            b = findele(parr, pos+1, pos+1)
            if b >= n :
                kcount = k+2
                break
            marr[1] = (parr[b], b)
            if parr[pos] == b+1 :
                b2 = findnextpos(parr, pos+1)
                if b2 == b :
                    b2 = findnextpos(parr, b+1)
            else :
                b2 = findele(parr, b+1, pos)
            if b2 >= n :
                kcount = k+2
                break
            marr[3] = (parr[b2], b2)"""


            """b = findnextpos(parr, pos+1)
            if parr[b] == (pos+1) :
                marr[1] = (parr[b], b)
                b = findnextpos(parr, b+1)
                if b >= n :
                    # If we have only two numbers which are not in their respective places, then we exit the program.
                    kcount = k+2
                    break
                else :
                    marr[3] = (parr[b], b)
            else :
                marr[3] = (parr[b], b)
                b = findele(parr, pos+1)
                marr[1] = (parr[b], b)"""
            # We now have the i1, i2, i3, now we perform the interchange.
            v1 = parr[marr[1][1]]
            v2 = parr[marr[2][1]]
            v3 = parr[marr[3][1]]
            parr[marr[2][1]] = v1
            parr[marr[3][1]] = v2
            parr[marr[1][1]] = v3
            # We have performed an interchange.
            kcount += 1
            #pos += 1
            result.append((marr[1][1]+1, marr[2][1]+1, marr[3][1]+1))
            """print('Result : ', result[-1])"""
            # If after all changes we reach the initial array, then it is a loop and thus we cannot win.
            if (b1 != -1) and (parr[b0] == (b0+1)) :
                finding_pos = b1
                if (parr[b1] == (b1+1)) and (b2 != -1) :
                    finding_pos = b2
            if parr[pos] == (pos+1) :
                pos = finding_pos
            """if parr == parr_orig :
                kcount = k+2
                break"""
    if kcount > k :
        print(-1)
    else :
        print(kcount)
        for i in range(kcount) :
            print(result[i][0], result[i][1], result[i][2])
