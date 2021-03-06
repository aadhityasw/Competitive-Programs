# Cross the Buildings


Bob is standing on top of a building. There are n buildings next to each other with different heights. He is standing on top of the first building. Bob wants to move to the top of the nth building.
The buildings are of red color. Fortunately, Bob found a magic sack and a magic saw. The magic saw can cut each building once and the cut block goes into the magic sack. The magic sack has two compartments, one compartment has m green blocks each of unit height, and the other compartment has the cut red blocks.
In order for Bob to move from the top of one building to the next, the height of the two buildings must be the same. In case their heights are different Bob can perform the following operations to make the current building’s height the same as the next one-
1. Cut the current building of certain units.
2. Add any number of green blocks from the sack.
3. Add the last cut red block from the sack and cut the extra height if needed
4. Add any number of green blocks and the last cut red block from the sack.
Whenever Bob cuts or adds blocks he moves to the new height after cutting or adding the blocks.
Also he cannot add two different red blocks in the same building, he can add only the recently cut red block.
Help Bob to find if he can successfully reach the top of the final building from the top of the first building.

Input
Each test case consists of two lines. 
First-line consists of two integers’ n and m.
The next line consists of n integers separated by a space where each integer represents the height of the ith building.

Ouput
Print “YES” if Bob can move from the top of the first building to the top of the last building, else, print “NO”.

Constraints
1 <= n <= 109
1 <= m <= 109
0 <= ai <= 109 where ai is the height of the ith building

Sample Test Case
Input
5 2
5 6 3 4 7

Output
YES

Explanation
Bob is currently at the first building of height 5 units, so he adds a green block to the current building and increases his height by 1 unit. Now he’ll be of the same height as the second building so he moves to the second building. Now he cuts three units of the building and moves the red block into the sack. After cutting he’ll be at height 3 which is of the same height as the third building, so he moves to the third building. Now he will add the last put red block which is of height 3 to the current building. Now he’ll be at height 6 in order to move to the next building he cuts down 2 units and moves them into the sack. Now he’ll be at height 4, so he can move to the fourth building. Now he adds the remaining one green block and the last put red block of 2 units to the current building. Now he’ll be at height 7 and can move to the fifth building.

Time Limit:	5 secs

