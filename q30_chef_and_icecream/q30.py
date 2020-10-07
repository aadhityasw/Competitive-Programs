# Codechef June2020

# Chef and Icecream
# https://www.codechef.com/problems/CHFICRM
# CHFICRM

"""

Chef owns an icecream shop in Chefland named scoORZ. There are only three types of coins in Chefland: Rs. 5, Rs. 10 and Rs. 15. An icecream costs Rs. 5.

There are N people (numbered 1 through N) standing in a queue to buy icecream from scoORZ. Each person wants to buy exactly one icecream. For each valid i, the i-th person has one coin with value ai. It is only possible for someone to buy an icecream when Chef can give them back their change exactly ― for example, if someone pays with a Rs. 10 coin, Chef needs to have a Rs. 5 coin that he gives to this person as change.

Initially, Chef has no money. He wants to know if he can sell icecream to everyone in the queue, in the given order. Since he is busy eating his own icecream, can you tell him if he can serve all these people?

"""

test = int(input())
for t in range(test) :
    a = int(input())
    parr = list(map(int, input().strip().split()))
    avalible = [0, 0, 0]
    flag = True
    for p in parr :
        if p == 5 :
            avalible[0] += 1
        elif p == 10 :
            if avalible[0] > 0 :
                avalible[0] -= 1
                avalible[1] += 1
            else :
                flag = False
                break
        elif p == 15 :
            if avalible[1] > 0 :
                avalible[1] -= 1
                avalible[2] += 1
            elif avalible[0] > 1 :
                avalible[0] -= 2
                avalible[2] += 1
            else :
                flag = False
                break
    if flag :
        print("YES")
    else :
        print("NO")
