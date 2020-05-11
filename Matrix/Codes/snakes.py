"""
Print Matrix in snake Pattern
Given a matrix mat[][] of size N x N. The task is to print the elements of the matrix in the snake pattern.


Input:
First line consists of an integer T denoting the number of test cases. First line of each test case consists of N, denoting number of elements(N x N) in Matrix. Second line of every test case consists of N x N spaced integers denoting elements of Matrix elements.

Output:
For each testcase, in a new line, print the matrix in snake pattern.

Your Task:
This is a function problem. You only need to complete the function print that takes a matrix and n as parameters and prints the matrix. The newline is automatically appended by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= mat[i][j] <= 100

Example:
Input:
2
3
45 48 54 21 89 87 70 78 15
2
1 2 3 4
Output:
45 48 54 87 89 21 70 78 15 
1 2 4 3

Explanation:
Testcase 1: Matrix is as below:
45 48 54
21 89 87
70 78 15

Printing it in snake pattern will lead to the output as 45 48 54 87 89 21 70 78 15.
Testcase 2: Matrix is as below:
1 2 
3 4
Printing it in snake pattern will give output as 1 2 4 3.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def printS(mat,n): 
    sum = 0
    for x in range(n):
        if(sum%2==0):
            for y in range(n):
               print(mat[x][y],end=" ")
        else:
            for y in range(n-1,-1,-1):
                print(mat[x][y],end=" ")
        sum+=1