# Codechef June2020

# XYSTR
# https://www.codechef.com/problems/XYSTR
# Chef and String

"""

There are N students standing in a row and numbered 1 through N from left to right. You are given a string S with length N, where for each valid i, the i-th character of S is 'x' if the i-th student is a girl or 'y' if this student is a boy. Students standing next to each other in the row are friends.

The students are asked to form pairs for a dance competition. Each pair must consist of a boy and a girl. Two students can only form a pair if they are friends. Each student can only be part of at most one pair. What is the maximum number of pairs that can be formed?

"""

test = int(input())
for t in range(test) :
    s = input().strip()
    i=0
    pairs = 0
    while((i+1)<len(s)) :
        if ((s[i] =='x' and s[i+1] == 'y') or (s[i] =='y' and s[i+1] == 'x')) :
            i += 1
            pairs += 1
        i += 1
    print(pairs)
