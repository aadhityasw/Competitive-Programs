# Programming Padding



Given a matrix add N layer of padding at particular location(explained below), convolve the filter on padded matrix and print the resultant matrix

Padding : Padding in computer vision is used to pad the image. Please see below image to understand zero padding.
image

This is zero padding, which we will use in this program.

Location
L : Add padding to left of 4x4 matrix
R : Add padding to right of 4x4 matrix
LR : Add padding to left and right of 4x4 matrix
T : Add padding to top of the 4x4 matrix
B : Add padding to bottom of the 4x4 matrix
TB : Add padding to the Top and bottom of 4x4 matric
A : Add padding to all sides of 4x4 matrix.

Layer number

1 : add 1 layer of padding
2 : add 2 layers of padding etc
example1

   0 1 2 4 5  
   0 5 6 1 3 
   0 8 4 7 1 
   0 5 2 1 8 
This is an example1 of L padding with layer=1

example2

   0 1 2 4 5 0 
   0 5 6 1 3 0
   0 8 4 7 1 0
   0 5 2 1 8 0
This is an example2 of LR padding with layer=1

example3

   0 0 0 0
   0 0 0 0
   1 2 4 5  
   5 6 1 3 
   8 4 7 1 
   5 2 1 8 
   0 0 0 0
   0 0 0 0
This is an example3 of TB - padding with layer=2

Stride : Stride is the number of pixels shifts over the input matrix. e.g.

Stride = 1

image

Stride = 2

image

Input Format

First line is 4x4 matrix : Input Matrix
Second line is location
Third line is N : layer number
Fourth line is 3x3 matrix : filter
Fifth line is S : a stride
Constraints

Input matrix is always 4x4 Matrix
N < 3
Filter matrix is always 3x3 matrix
S <= 3
Output Format

A Matrix, its size depends on the layer number, location and stride

Sample Input 0

[[1, 1, 0, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 0]]
TB
1
[[0, 0, 1], [0, 1, 0], [1, 0, 0]]
1
Sample Output 0

[[1, 1], [1, 2], [1, 1], [1, 1]]
Explanation 0

First line is 4x4 input matrix : [[1, 1, 0, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 0]]
Second line is location : TB
Third line is layer number : 1
Fourth line is 3x3 matrix : [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
Firth line is S Stride : 1
First we will add TB(Top and Bottom) Padding to the input matrix on 1 layer

Input matrix

image

Padded matrix with TB location and layer 1

image

Filter

image

Now convolve filter on this matrix which gives this resultant matrix

image

Print resultant matrix in this format only : [[1, 1], [1, 2], [1, 1], [1, 1]]

Sample Input 1

[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
LR
2
[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
3
Sample Output 1

[3, 9]
Explanation 1

First line is input Matrix

image

Second and third like in location and layers number respectively, after applying that to input matrix, it will look like this.

image

Fourth line is a 3x3 filter matrix

image

Fifth is stride=3 which will look while solving example.

So first the filter and input matrix is convolved(element-wise multiplication) i.e.
image

So we get our first element output.

Now since we have take stride = 3 we will leave matrices with stride = 1
image

and will leave matrix with stride = 2

image

So now we will consider stride = 3 matrix which is

image

and perform multiplication and we get our second output element

image

So here we cannot proceed further, since stride = 3 will go out of the matrix range. So we stop here and hence

[3, 9] is the output matrix.
