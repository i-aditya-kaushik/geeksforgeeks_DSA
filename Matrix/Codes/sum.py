"""
Adding two matrices
Addition is one of the easiest operation to carry out. The same hold true for matrices. Two matrices can be added only if they have the same dimensions. The elements at similar positions get added.

You are given two matrices. The first matrix's dimensions are given by n1,m1. The second matrix's dimensions are given by n2,m2. You need to add both the matrices. If addition is not possible then print -1.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains four lines of input. The first line contains dimensions of the first array n1 and m1. The second line contains n1*m1 elements separated by spaces. The third line contains dimensions of the second array n2 and m2. The fourth line contains n2*m2 elements separated by spaces.

Output:
For each testcase, in a new line, print the sum of matrix if possible; else print -1.

Your Task:
This is a function problem. You only need to complete the function sumMatrix that taks n1, m1, n2, m2, matrix1, matrix2 as parameters and prints the sum of matrices. The newline is automatically appended by the driver code.

Constraints:
1 <= T <= 100
1 <= n1, m1, n2, m2 <= 30
0 <= arri <= 100

Examples:
Input:
2
2 3
1 2 3 4 5 6
2 3
1 3 3 2 3 3
3 2
1 2 3 4 5 6
3 2
1 3 3 2 3 3
Output:
2 5 6 6 8 9
2 5 6 6 8 9

Explanation:
Testcase 1: Adding each elements in first matrix to the elements with corresponding row and column (cell) of another matrix will result in the sum as 2 5 6 6 8 9.
Testcase 2: Adding each elements in first matrix to the elements with corresponding row and column of 2nd matrix , will result in the sum as 2 5 6 6 8 9.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def sumMatrix(n1, m1, n2, m2, arr1, arr2):
    if n1!=n2:
        print('-1',end=" ")
        return
    if m1!=m2:
        print('-1',end=" ")
        return
    n = max(n1,n2)
    m = max(m1,m2)
    for x in range(n):
        for y in range(m):
            print(arr1[x][y]+arr2[x][y],end=" ")