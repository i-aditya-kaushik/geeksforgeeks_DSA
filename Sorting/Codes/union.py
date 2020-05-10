"""
Union of Two Sorted Arrays
Given two sorted arrays arr[] and brr[] of size N and M respectively. The task is to find the union of these two arrays.
Union of two arrays can be defined as the common and distinct elements in the two arrays.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of testcases T. For each testcase, first line of input contains size of two arrays N and M. Next two line contains N and M elements.

Output:
For each testcase, print the union (common and distinct) of two arrays in a single line. You need to print the union in sorted order.

Your Task:
This is a function problem. You only need to complete the function findUnion() that takes N and M as parameter and prints the union of two arrays. The newline is automatically appended by the driver code.

Constraints:
1 <= T <= 100
1 <= N, M <= 105
1 <= arr[i], brr[i] <= 106

Example:
Input:
3
5 3
1 2 3 4 5
1 2 3
5 5
2 2 3 4 5
1 1 2 3 4
5 5
1 1 1 1 1
2 2 2 2 2
Output:
1 2 3 4 5
1 2 3 4 5
1 2

Explanation:
Testcase 1: Distinct elements including both the arrays are: 1 2 3 4 5.
Testcase 2: Distinct elements including both the arrays are: 1 2 3 4 5.
Testcase 3: Distinct elements including both the arrays are: 1 2.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""


def mergeArrays(a,b,n,m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return: None, print the union, space separated
    '''
    ans = (set(a).union(b))
    ans = list(ans)
    ans = sorted(ans)
    for x in ans:
        print(x,end=" ")