# Elections 


Two national parties BJP and Congress are head to head in the election and are blaming each other as always. The Election has become interesting because of the importance of Regional parties. BJP is boasting on the work done during their tenure by the Government and how much they thought for the nation and people. On the other hand, Congress and other parties are calling it a hoax and urging people to vote for them. BJP star campaigners are just launching the missiles and making place amongst the people again. Congress is worried because of their track record and are breaking the boundaries to get to the people. The other Regional parties are also pulling out every trick in their book. The Election is taking ups and downs frequently.

The voting is done in various phases and News channels are on the edge of their seats covering the areas where elections are to be held. Opinion polls are being conducted in the areas and public opinion is taken to predict the winner of the elections. People are also talking whether the Modi led Government will continue to rule or the Congress and other parties would be able to pull out some magic.
There are many political pandits and experts in the news industry which are covering the elections for a long time now. With their experience in the political field, they have come out with a theory which they claim can predict if the BJP government will come to power again or not.
The experts have formed a matrix in the form of Phases and States.
The experts have provided the number of wins required by BJP in different phases and states to form the government. According to theory, if it is possible to arrange the wins required by BJP in the form of experts matrix, then they will definitely form the government otherwise there will be a new government.

<br>
If BJP can form the government as per the theory, then the output would be "YES" indicating that people are happy with the government otherwise the output would be "NO" indicating that people are unhappy with the government.
<br>
Note: There are different seats in States which are to be voted in different phases. The number of phases and states is not restricted to the actual number of states and phases in the Indian Election.
<br>
<br>


### Input Format<br>
The first line consists of T, number of test cases. <br>
The first line of each test case consists of r and c, number of phases and states respectively.<br>
The second line of each test case consists of the number of wins ri required by BJP in the phases to win elections.<br>
<br>
The third line of each test case consists of the number of wins ci required by BJP in the States to win the elections.<br>

<br>


### Constraints<br>
1<=T<5<br>
1<= r, c <=100000<br>
0<= ri <=c<br>

0<=ci <=r<br>


### Output Format<br>
Print "YES" (without quotes) if BJP can form the government as per the experts theory otherwise print "NO" (without quotes).<br>


### Sample TestCase 1<br>
Input<br>
2<br>
3 2<br>
2 1 0 <br>
1 2 <br>
3 3<br>
3 2 1 <br>
1 2 2<br>
<br>
Output<br>
YES<br>

NO<br>

### Explanation<br>

Test Case 1:<br>
As per the theory, to form the government, BJP should win 2 seats in the first phase, 1 seat in second phase and 0 in last phase.



BJP also needs to follow the number of wins in states column wise. There should be a single win in the seats of first state and 2 wins in the seats of second state.



It is possible for BJP to win the seats in this format and form the matrix as per the theory.The matrix can be successfully made thus BJP can form the government. Thus, the answer is YES.


<br>
Test Case 2:<br> 
It is not possible to create the matrix with respective wins by BJP in phases and states. Thus, the answer is NO.
