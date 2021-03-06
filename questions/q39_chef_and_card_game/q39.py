# Codechef

# CRDGAME
# Chef and Card Game
# https://www.codechef.com/problems/CRDGAME

"""
Chef is playing a card game with his friend Morty Smith.

The rules of the game are as follows:

There are two piles of cards, pile A and pile B, each with N cards in it. Pile A belongs to Chef and pile B belongs to Morty.
Each card has one positive integer on it
The ‘power’ of a card is defined as the sum of digits of the integer on that card
The game consists of N rounds
In each round, both players simultaneously draw one card each from the top of their piles and the player who draws the card with higher power wins this round and gets a point. If the powers of both players' cards are equal then they get 1 point each.
The winner of the game is the player who has more points at the end of N rounds. If both players have equal number of points then the game ends in a draw.
The game is now over and Chef has told Morty to find the winner. Unfortunately, this task is too complex for him. Help Morty find the winner.

Input:
First line will contain T, number of testcases.
The first line of each test case will contain N, the number of rounds played.
The ith of the next N lines of each test case will contain Ai and Bi, the number on the card drawn by Chef and Morty respectively in round i.
Output:
For each test case, output two space separated integers on a new line:
Output

0 if Chef wins,
1 if Morty wins,
2 if it is a draw,
followed by the number of points the winner had.
(If it is a draw then output either player’s points).
Constraints
1≤T≤1000
1≤N≤100
1≤Ai,Bi≤109
Subtasks
100 points : No additional constraints
Sample Input:
2
3
10 4
8 12
7 6
2
5 10
3 4
Sample Output:
0 2
2 1
Explanation:
Test Case 1:

Round 1:

Chef’s card has power 1+0 = 1,
Morty’s card has power 4.
Therefore, Morty wins the round.

Round 2:

Chef’s card has power 8,
Morty’s card has power 1+2 = 3.
Therefore, Chef wins the round.

Round 3:

Chef’s card has power 7,
Morty’s card has power 6.
Therefore, Chef wins the round.

Therefore, Chef wins the game with 2 points (Morty has 1 point).

Test Case 2:

Round 1:

Chef’s card has power 5,
Morty’s card has power 1+0=1.
Therefore, Chef wins the round.

Round 2:

Chef’s card has power 3,
Morty’s card has power 4.
Therefore, Morty wins the round.

Therefore, the game ends in a draw and both players have 1 point each.

"""
#%%


def findsum(n) :
    if n < 10 :
        return n
    else :
        summ = 0
        while(n > 0) :
            a = n % 10
            summ += a
            n = int(n // 10)
        return summ


test = int(input())
for tes in range(test) :
    n = int(input())
    points = [0, 0]
    for round in range(n) :
        a, b = map(int, input().strip().split())
        a = findsum(a)
        b = findsum(b)
        if a > b :
            points[0] += 1
        elif b > a :
            points[1] += 1
        else :
            points[0] += 1
            points[1] += 1
    if points[0] > points[1] :
        print("0", points[0])
    elif points[1] > points[0] :
        print("1", points[1])
    else :
        print("2", points[0])
