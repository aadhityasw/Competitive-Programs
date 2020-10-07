# Codechef

# PTMSSNG
# Missing a Point 
# https://www.codechef.com/problems/PTMSSNG

"""
Chef has N axis-parallel rectangles in a 2D Cartesian coordinate system. These rectangles may intersect, but it is guaranteed that all their 4N vertices are pairwise distinct.

Unfortunately, Chef lost one vertex, and up until now, none of his fixes have worked (although putting an image of a point on a milk carton might not have been the greatest idea after all…). Therefore, he gave you the task of finding it! You are given the remaining 4N−1 points and you should find the missing one.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
Then, 4N−1 lines follow. Each of these lines contains two space-separated integers x and y denoting a vertex (x,y) of some rectangle.
Output
For each test case, print a single line containing two space-separated integers X and Y ― the coordinates of the missing point. It can be proved that the missing point can be determined uniquely.

Constraints
T≤100
1≤N≤2⋅105
|x|,|y|≤109
the sum of N over all test cases does not exceed 2⋅105
Subtasks
Subtask #1 (20 points):

T=5
N≤20
Subtask #2 (30 points): |x|,|y|≤105
Subtask #3 (50 points): original constraints

Example Input
1
2
1 1
1 2
4 6
2 1
9 6
9 3
4 3
Example Output
2 2
Explanation
The original set of points are:
Upon adding the missing point (2,2), N=2 rectangles can be formed:
"""

#%%

test = int(input())
for tes in range(test) :
    n = int(input())
    points = []
    for i in range(4*n-1) :
        points.append(tuple(map(int, input().strip().split())))
    # Row Check
    row = None
    for p1 in points :
        count = 1
        for p2 in points :
            if p1 != p2 :
                if p1[0] == p2[0] :
                    count += 1
        if count % 2 != 0 :
            row = p1[0]
            break
    # Column Check
    col = None
    for p1 in points :
        count = 1
        for p2 in points :
            if p1 != p2 :
                if p1[1] == p2[1] :
                    count += 1
        if count % 2 != 0 :
            col = p1[1]
            break
    print(row, col)


#%%


test = int(input())
for tes in range(test) :
    n = int(input())
    points = []
    for i in range(4*n-1) :
        points.append(tuple(map(int, input().strip().split())))
    row = None
    col = None
    for p1 in points :
        row_count = 1
        col_count = 1
        for p2 in points :
            if p1 != p2 :
                if p1[0] == p2[0] :
                    row_count += 1
                elif p1[1] == p2[1] :
                    col_count += 1
        if row_count % 2 != 0 :
            row = p1[0]
        if col_count %2 != 0 :
            col = p1[1]
        if col != None and row != None :
            break
    print(row, col)



#%%

test = int(input())
for tes in range(test) :
    n = int(input())
    rows = []
    cols = []
    for i in range(4*n-1) :
        r, c = map(int, input().strip().split())
        if r in rows :
            rows.remove(r)
        else :
            rows.append(r)
        if c in cols :
            cols.remove(c)
        else :
            cols.append(c)
    print(rows[0], cols[0])



#%%

test = int(input())
for tes in range(test) :
    n = int(input())
    rows = []
    cols = []
    for i in range(4*n-1) :
        r, c = map(int, input().strip().split())
        try :
            rows.remove(r)
        except :
            rows.append(r)
        try :
            cols.remove(c)
        except :
            cols.append(c)
    print(rows[0], cols[0])


#%%

test = int(input())
for tes in range(test) :
    n = int(input())
    rows = [[] for _ in range(10000)]
    cols = [[] for _ in range(10000)]
    for i in range(4*n-1) :
        r, c = map(int, input().strip().split())
        try :
            rows[r%10000].remove(r)
        except :
            rows[r%10000].append(r)
        try :
            cols[c%10000].remove(c)
        except :
            cols[c%10000].append(c)
    r = None
    c = None
    for i in range(10000) :
        if len(rows[i]) > 0 :
            r = rows[i][0]
        if len(cols[i]) > 0 :
            c = cols[i][0]
        if c!=None and r!=None :
            break
    print(r, c)
    