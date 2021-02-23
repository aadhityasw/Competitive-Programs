# Programming Convolution


You have N number of MxM Matrices and 1 filter. Convolve N matrices on filter with Stride S which gives N resultant matrices.

Stride : Stride is the number of pixels shifts over the input matrix. e.g.

Stride = 1

image

Stride = 2

image

Pseudo Code for Convolution

for each image row in input image:
   for each pixel in image row:

      set accumulator to zero

      for each kernel row in kernel:
         for each element in kernel row:

            if element position  corresponding* to pixel position then
               multiply element value  corresponding* to pixel value
               add result to accumulator
            endif

      set output image pixel to accumulator
Input Format

First line is N : Number of matrices to convolve
Second like is S : Stride
Third line is 3x3 matrix : Filter
Fourth line is size of Matrix : M
Fifth Line onwards is N number of MxM matrix(matrices) : Input Matrix (every MxM input matrix is on a new line)
Constraints

N < 3
S <= 3
Filter is always 3x3 matrix
M <= 10
Output Format

N KxK Matrix

Sample Input 0

1
1
[[1, 0, 1], [0, 1, 0], [1, 0, 1]]
5
[[0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 0]]
Sample Output 0

[[1, 4, 3], [1, 2, 4], [1, 2, 3]]
Explanation 0

First lines states we can take 1 Matrix
Second line is states we will use stride of 1
Third line is filter
Fourth line is the size of matrix
Fifth line is a 5x5 input matrix
So the Matrices are like this

Filter

image

Input Matrix

image

Now we will convolve Matrix on filter and will multiply one to one. e.g.

image

Hence after convolution it gives 3x3 matrix

image

Print the result in this format only [[1, 4, 3], [1, 2, 4], [1, 2, 3]]

Sample Input 1

2
2
[[1, 0, 1], [0, 1, 0], [1, 0, 1]]
5
[[0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 0]]
[[1, 0, 0, 0, 1], [1, 1, 0, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, 0, 0, 1]]
Sample Output 1

[[1, 3], [1, 3]]
[[4, 2], [4, 2]]
Explanation 1

Given Number as 2 i.e. 2 matrices, after convolving those matrices on filter, it gives 2 matrices as an output.
