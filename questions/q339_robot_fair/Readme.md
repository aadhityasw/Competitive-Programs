# Robot at the Fair


Winter is back and is end of season’s sale all over. The City’s biggest Housewares and Home Appliances Fair is inaugurated at the Mathura Trade Centre and the show hosted numerous retailers, wholesalers, distributors to promote domestic economy. Public participated in large groups and the Event coordinators have designed a Robot at the Event ground to give instructions to the public in which directions to move.

 The Event ground is a rectangular grid with R rows and C columns, with R*C cells in the grid. There are many obstacles in the event ground, so the Robot is set initially in the cell such that it is facing north, south, east or west. The initial position of the Robot (X,Y) is known. It can take a series of m moves through the ground. Each move is one of:

·    F - moves forward one cell in the direction that he is facing, or

·    L - turns 90 degrees counter-clockwise, remaining on the same cell, or

·    R - turns 90 degrees clockwise, remaining on the same cell.

 After making these moves, the Robot would stand at some final position where the guests wanted to drop. The coordinators wanted you to figure out where the Robot is standing. You will help them by writing a program to determine the final position of the Robot. You may also assume that the Robot is always facing a direction that is parallel to the sides of the event ground (north, south, east, or west).

Input format
The input begins with R and C (1 ≤ R ≤ 50; 1 ≤ C ≤ 80 ), each on a separate line.

Next R lines consists of C characters describing the event ground: a period character denotes a cell the Robot may walk through; a capital X character denotes a cell with an obstacle. 

Next line of the input consists of two integers X and Y (1 ≤ X ≤ R; 1 ≤ Y ≤ C ), which corresponds to the initial position of the Robot.

Below the grid is the number m (0 ≤ m ≤ 30000) followed by Robot’s moves. Each is a single character: F, L, or R.

Output format
Output in separate line each of the co-ordinates(separated by a space) of the final position of the Robot in the event ground.

Refer sample input and output for formatting specifications.

Sample testcases
Input 1
2 4
. . . .
. X X .
0 2
1
F
Output 1
0 1
0 3
