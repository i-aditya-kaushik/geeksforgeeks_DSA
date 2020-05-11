"""
Sum of upper and lower triangles
Given a square matrix mat[][] of size N*N, print the sum of upper and lower triangular elements. Upper Triangle consists of elements on the diagonal and above it. Lower triangle consists of elements on the diagonal and below it. 

Input:
The first line consists of an integer T i.e number of test cases. The first line of each test case consists of an integer N denoting the size of the matrix. The next line contains N*N spaced separated integers.

Output:
For each testcase, in a new line, print the required output.

Your Task:
This is a function problem. You only need to complete the function sumTriangles that takes n and matrix as parameters and prints the sum of upper and lower triangles. The newline is automatically appended by the driver code.

Constraints: 
1 <= T <= 100
1 <= N <= 100
1 <= mat[i][j] <= 100

Example:
Input:
2
3
6 5 4 1 2 5 7 9 7
2
1 2 3 4
Output:
29 32
7 8

Explanation:
Testcase1: The given matrix is

6 5 4
1 2 5
7 9 7
The elements of upper triangle are
6 5 4
   2 5
      7
Sum of these elements is 6+5+4+2+5+7=29
The elements of lower triangle are
6
1 2
7 9 7
Sum of these elements is 6+1+2+7+9+7= 32.
Testcase 2:
Upper triangular matrix:
1 2
   4
Sum of these elements are 7.
Lower triangular matrix:
1
3 4
Sum of these elements are 8.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def sumTriangles(n, mat):
    upper = 0
    lower = 0
    for x in range(n):
        for y in range(n):
            if(x==y):
                upper+=mat[x][y]
                lower+=mat[x][y]
            elif(x<y):
                upper+=mat[x][y]
            else:
                lower+=mat[x][y]
    print(upper,lower,end=" ")