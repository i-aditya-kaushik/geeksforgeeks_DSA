"""
Boolean Matrix Problem
Given a boolean matrix mat[r][c] of size r X c, modify it such that if a matrix cell mat[i][j] is 1 (or true) then make all the cells of ith row and jth column as 1.

Input:
The first line of input contains an integer T denoting the number of test cases.The first line of each test case is r and c, r is the number of rows and c is the number of columns.The next r lines contain c elements having either 0 or 1 and separated by spaces.

Output:
Print the modified array.

Your Task:
This is a function problem. You only need to complete the function booleanMatrix that takes r, c, and matrix as parameters and prints the modified array. You need to append a newline to separate ouput of individual testcases.

Constraints:
1 ≤ T ≤ 100
1 ≤ r, c ≤ 1000
0 ≤ A[i][j] ≤ 1

Example:
Input:
3
2 2
1 0
0 0
2 3
0 0 0 
0 0 1
4 3
1 0 0
1 0 0
1 0 0
0 0 0
Output:
1 1
1 0
0 0 1 
1 1 1
1 1 1
1 1 1
1 0 0

Explanation:
Testcase1: Since only first element of matrix has 1 (at index 1,1) as value, so first row and first column are modified to 1.
Testcase 2: Since only the last element of matrix has 1 (at index 2,3) , so last row and last column is modified to 1.
Testcase 3: Since first element of 1st,2nd,3rd row of matrix has value 1 so, 1st column and 1st,2nd,3rd row of matrix has been modified to 1.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def booleanMatrix(r, c, mat):
    l = []
    for x in range(r):
        for y in range(c):
            if(mat[x][y]==1):
                l.append([x,y])
    for x in l:
        for y in range(r):
            mat[y][x[1]] = 1
        for z in range(c):
            mat[x[0]][z] = 1
    for x in mat:
        for y in x:
            print(y,end=" ")
        print()