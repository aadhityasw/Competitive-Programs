# UW Galaxies


The year is 1313, and Humanity’s Rush to the Stars is now 200 years old. The problem of real-time connection between star systems remains, however, and the key is the unterwave.

Unterwave (UW) connection works as direct UW links have been set up between certain pairs of star systems, and two systems without a direct link communicate by hopping along existing links through intermediary systems. Although no system has over 20

direct links to other systems, any two systems can communicate, either directly or indirectly.

You have been asked to select two star systems for your company’s new home offices—one in a human system, and one in an alien system. You are to select them so that the UW distance (a measure of communication latency) is minimized.

Every star system has a gravity rate that affects UW connection﻿. Just as no two snowflakes on earth have the same crystalline architecture﻿, no two star systems in the universe have the same gravity. If a connection path from from one system to another encounters the sequence G=g1,g2,…,gn of gravity values, including the source and destination of the message, then three sequences of n−1 terms each may be defined, relating to physical characteristics of UW communication:

cap(G)=g2⋅g1, g3⋅g2, …, gn⋅gn−1(Capacitance)

pot(G)=g2−g1, g3−g2, …, gn−gn−1(Potential)

ind(G)=g2+g1, g3+g2, …, gn+gn−1(Inductance)



For two sequences A=a1, a2, …, am and B=b1, b2, …, bm we define:

A⋅B=a1⋅b1, a2⋅b2, …, am⋅bmA−B=a1−b1, a2−b2, …, am−bm

Finally, the UW distance is given by the absolute value of the sum of the values of the sequence

pot(G)⋅([cap(G) ⋅ cap(G)]−ind(G)).



The UW distance can be quite large. Fortunately, your team has a gravity dispersal device, which may be placed in any single system. It reduces by 1 the gravity of that system, but increases by 1 the gravities of all systems directly linked to it. Use of this device is optional.﻿

Input format
The first line has a single integer n, giving the number of star systems. The next n lines describe the star systems, numbered 1 to n. Each line has the form g and d where g is the gravity value of that system and d is either ‘h’ or ‘a’, designating the system as human or alien (there is at least one system of each type). All values of g are distinct. The next line has a positive integer e giving the number of direct links between systems. Each of the next e lines contains two integers separated by a single space, which are the numbers of two systems that are directly linked. Links are bidirectional, and no link appears more than once in the input. No system links directly to more than 20 other systems.

Output format
Output the minimum UW distance that can be achieved between an alien and human system.

Code constraints
2≤n≤500

1≤g≤10000

Sample testcases
Input 1
3
20 h
21 a
19 h
3
1 2
2 3
3 2
Output 1
1261
