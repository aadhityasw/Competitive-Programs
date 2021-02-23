# Codechef 
# https://www.codechef.com/problems/COINS
# Bytelandian gold coins
# COINS

"""
In Byteland they have a very strange monetary system.

Each Bytelandian gold coin has an integer number written on it. A coin n can be exchanged in a bank into three coins: n/2, n/3 and n/4. But these numbers are all rounded down (the banks have to make a profit).

You can also sell Bytelandian coins for American dollars. The exchange rate is 1:1. But you can not buy Bytelandian coins.

You have one gold coin. What is the maximum amount of American dollars you can get for it?

Input
The input will contain several test cases (not more than 10). Each testcase is a single line with a number n, 0 <= n <= 1 000 000 000. It is the number written on your coin.

Output
For each test case output a single line, containing the maximum amount of American dollars you can make.

Example
Input:
12
2

Output:
13
2
You can change 12 into 6, 4 and 3, and then change these into 6+4+3=13. If you try changing the coin 2 into 3 smaller coins, you will get 1, 0 and 0, and later you can get no more than 1 out of them. It is better just to change the 2 coin directly into 2.


"""

"""def func(n) :
    a = (n // 2) + (n // 3) + (n // 4)
    s = 0
    if a > n :
        s = s + max((a // 2), func(a // 2))
        s = s + max((a // 3), func(a // 3))
        s = s + max((a // 4), func(a // 4))
        return s
    else :
        return n
    

test = int(input())
for t in range(test) :
    n = int(input())
    arr = [n]
    while(True) :
        if n == func(n) :
            break
        else :
            n = func(n)
    print(n)"""


"""test = int(input())
inarr = []
for t in range(test) :
    inarr.append(int(input()))
maxnum = max(inarr)
arr = [0] * (maxnum+1)
arr.append(0)
for i in range(1,  maxnum+1) :
    arr[i] = max(i, (arr[i//2] + arr[i//3] + arr[i//4]))
for t in range(test) :
    print(arr[inarr[t]])"""


bank = {}
def exchange(n) :
    if n < 12 :
        return n
    if n in bank :
        return bank[n]
    else :
        s = exchange(n//2) + exchange(n//3) + exchange(n//4)
        bank[n] = s
        return (s)

test = int(input())
for t in range(test) :
    n = int(input())
    print(exchange(n))
