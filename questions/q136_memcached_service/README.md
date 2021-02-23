# Memcached Service


https://www.codechef.com/CPAT002/problems/MEMSER


Chef is a programmer. In his computer, he is running a caching service, Memcached. He can give the commands "start", "restart" or "stop" to the service, the functionalities of which are specified below.

"start": Start the service.
"restart": If the service is started, do nothing. Otherwise, start the service.
"stop": If the service is not running, give an error. Otherwise, stop the service.
The service is initially not running. You are given n
 commands that he then gives to the program in sequence. Your task is to identify whether some error/s were encountered while running these commands.

Input
The first line of each test case contains an integer T
 denoting the number of test cases. The description of T
 test cases follows.
The first line of each test case contains an integer n
, denoting the number of commands.
The next line contains n
 space separated strings, each of which is either "start", "restart" or "stop".
Output
For each test case, output "404" if some error occurred, otherwise output "200" (without quotes).

Constraints
1≤T≤100
1≤n≤10
Subtasks
For 30% of the score: The only commands will be "start" or "stop", i.e. no "restart" command.
Remaining 70%: No extra constraints.
Sample Input
5
2
start stop
2
restart stop
3
start restart stop
3
start stop stop
1
stop
Sample Output
200
200
200
404
404
Explanation
In the first, second and third cases, there won't be any error.
In the fourth case, when you execute the third command, the service is already stopped. So, it will result in an error.
In the fifth case, you are trying to stop the service when it's not even started, and will hence result in an error.
