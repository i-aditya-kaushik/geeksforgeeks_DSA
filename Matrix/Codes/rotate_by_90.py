"""
Rotate by 90 degree
Given a square matrix mat[][] of size N x N. The task is to rotate it by 90 degrees in anti-clockwise direction without using any extra space.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines. The first line of each test case consists of an integer N, where N is the size of the square matrix. The second line of each test case contains N x N space separated values of the matrix mat.

Output:
Corresponding to each test case, in a new line, print the rotated matrix. 

User Task:
The task is to complete the function rotateby90() which rotates the input matrix by 90 degree. You just need to rotate the matrix, printing the matrix will be automatically done the driver code.

Constraints:
1 ≤ T ≤ 50
1 ≤ N ≤ 50
1 <= mat[][] <= 100

Example:
Input:
3
3
1 2 3 4 5 6 7 8 9
2
1 2 3 4
1
80
Output:
3 6 9 2 5 8 1 4 7
2 4 1 3
80

Explanation:
Testcase 1: Matrix is as below:
1 2 3
4 5 6
7 8 9

Rotating it by 90 degrees in anticlockwise directions will result as below matrix:
3 6 9
2 5 8
1 4 7
Testcase 2: Matrix is as below:
1 2
3 4
After rotating by 90 degree , matrix will be 
2 4
1 3
Testcase 3: Matrix is as below:
80
After rotating by 90 degree , matrix will be 
80
 

** For More Input/Output Examples Use 'Expected Output' option **
"""
def transpose(mat,n):
    for x in range(n):
        for y in range(n):
            if(y>x):
                break
            temp = mat[x][y]
            mat[x][y]= mat[y][x]
            mat[y][x]=temp
            
def rotateby90(a, n):
    transpose(a,n)
    for x in range(n//2):
        temp = a[x]
        a[x] = a[n-x-1]
        a[n-x-1] = temp