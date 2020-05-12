"""
Spirally traversing a matrix
Given a matrix mat[][] of size M*N. Traverse and print the matrix in spiral form.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test cases follow. Each testcase has 2 lines. First line contains M and N respectively separated by a space. Second line contains M*N values separated by spaces.

Output:
Elements when travelled in Spiral form, will be displayed in a single line.

Your Task:
This is a function problem. You only need to complete the function spirallyTraverse that takes m, n, and matrix as parameters and prints the spiral traversal. The driver code automatically appends a new line.

Constraints:
1 <= T <= 100
2 <= M, N <= 10
0 <= Ai <= 100

Example:
Input:
2
4 4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
3 4
1 2 3 4 5 6 7 8 9 10 11 12
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
1 2 3 4 8 12 11 10 9 5 6 7

Explanation:
Testcase 1:


Testcase 2: Applying same technique as shown above , output for the 2nd testcase will be 1 2 3 4 8 12 11 10 9 5 6 7.

** For More Input/Output Examples Use 'Expected Output' option **
"""


def spirallyTraverse(m, n, a) : 
    k = 0; l = 0
    while (k < m and l < n) : 
        for i in range(l, n) : 
            print(a[k][i], end = " ") 
              
        k += 1
        for i in range(k, m) : 
            print(a[i][n - 1], end = " ") 
              
        n -= 1
        if ( k < m) : 
              
            for i in range(n - 1, (l - 1), -1) : 
                print(a[m - 1][i], end = " ") 
              
            m -= 1
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(a[i][l], end = " ") 
              
            l += 1
# def spirallyTraverse(m, n, a): 
#     left = 0
#     right = n-1
#     top = 0
#     sum=0
#     down = m-1
#     # for x in a:
#     #     for y in x:
#     #         print(y,end=" ")
#     #     print()
#     while(top<=down and left<=right and sum!=m*n):
#         for x in range(left,right):
#             if sum!=m*n:
#                 sum+=1
#                 print(a[top][x],end=" ")
        
#         for x in range(top,down):
#             if sum!=m*n:    
#                 sum+=1
#                 print(a[x][right],end=" ")
        
#         for x in range(right,left,-1):
#             if sum!=m*n:    
#                 sum+=1
#                 print(a[down][x],end=" ")
        
#         for x in range(down,top,-1):
#             if sum!=m*n:
#                 sum+=1
#                 print(a[x][left],end=" ")
#         down-=1
#         top+=1
#         left+=1
#         right-=1
#6 6 2 28 2 7 23 4 3 25 22 12 26 3 28 3 
#6 6 2 28 2 7 23 4 3 25 22 12 26 3 28 
#6 6 2 28 2 7 23 4 3 25 22 12 26 3 28 3 