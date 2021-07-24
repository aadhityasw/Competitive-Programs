# Zoo Travel


Kumar went to his grandmother's home and they have planned to go to a Zoo in their village. There are N people in the village, who want to visit Zoo. The road to reach the Zoo is not so safe. So, they go to the zoo only in a protected vehicle which can accommodate atmost 2 people. (There is only one such vehicle available in the village).People started to hire this vehicle to reach safely by driving it by themselves.



Every part of the journey from the village to the zoo or from the zoo to the village has some cost associated with it which is given by an array A[] elements. Array A[] has n elements, where A(i) represents the cost ith person has to pay if they travel alone in the vehicle. If two people travel in the vehicle, the cost of travel will be the maximum of the cost of two people.



Help Kumar to calculate the minimum total cost so that all N people can reach Zoo safely.



Sample Input and Output 1

30 and 40 go together (which costs 40) and 30 comes back (total cost 70 now). Now 60 and 70 go(total cost 140) and 40 comes back(total 180) and now 30 and 40 go(total cost 220)



Sample Input and Output 2

Both can reach the zoo in 45

Input format
The first line has an integer N, denoting the number of persons.

Next line contains N space separated distinct integers denoting the cost of ith person.

Output format
Print the minimum cost required so that all people can reach Zoo

Sample testcases
Input 1
4
30 40 60 70
Output 1
220
Input 2
2
32 45
Output 2
45
