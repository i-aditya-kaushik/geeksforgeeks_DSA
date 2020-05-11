"""
Merge three sorted arrays
Given three sorted arrays A, B and C of size N, M and P respectively. The task is to merge them into a single array which must be sorted in increasing order.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains size of three arrays N, M and P. Next three lines contains N, M and P elements for arrays.

Output:
Output the merged sorted array.

Your Task:
This is a function problem. You only need to complete the function mergeThree() that takes A,B,C as parameters. The function returns an array or vector.

Constraints:
1 <= T <= 100
1 <= N, M, P <= 106
1 <= A[i], B[i], C[i] <= 106

Example:
Input:
2
4 5 6
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
2 3 4
1 2
2 3 4
4 5 6 7
Output:
1 1 1 2 2 2 3 3 3 4 4 4 5 5 6
1 2 2 3 4 4 5 6 7

Explanation:
Testcase 1: Merging these three sorted arrays, we have elements as 1 1 1 2 2 2 3 3 3 4 4 4 5 5 6.
Testcase 2: Merging three sorted arrays , we have elements as 1 2 2 3 4 4 5 6 7.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def mergeThree(a,b,c):
    arr = a+b+c
    arr.sort()
    return(arr)