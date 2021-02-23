# Codechef June2020

# EOEO
# The Tom and Jerry Game!
# https://www.codechef.com/problems/EOEO
"""
As usual, Tom and Jerry are fighting. Tom has strength TS and Jerry has strength JS. You are given TS and your task is to find the number of possible values of JS such that Jerry wins the following game.

The game consists of one or more turns. In each turn:

If both TS and JS are even, their values get divided by 2 and the game proceeds with the next turn.
If both TS and JS are odd, a tie is declared and the game ends.
If TS is even and JS is odd, Tom wins the game.
If TS is odd and JS is even, Jerry wins the game.
Find the number of possible initial values of JS such that 1≤JS≤TS, there is no tie and Jerry wins the game.
"""

def trailing_zeros(a):
	count = 0
	while (a & 1) == 0 :
		a = a >> 1
		count += 1
	return count

test = int(input())
for t in range(test) :
    ts = int(input())
    zeros = trailing_zeros(ts)
    n = 2 ** (zeros+1)
    count = ts // n
    print(count)
