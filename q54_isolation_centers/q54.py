# Codechef - CORUS

test = int(input())
for tes in range(test) :
    (n, q) = map(int, input().strip().split(' '))
    sentence = input()
    letters = {}
    for ch in sentence :
        if ch in letters :
            letters[ch] += 1
        else :
            letters[ch] = 1
    for qu in range(q) :
        qi = int(input())
        count = 0
        for (l, c) in letters.items() :
            if c > qi :
                count += c-qi
        print(count)