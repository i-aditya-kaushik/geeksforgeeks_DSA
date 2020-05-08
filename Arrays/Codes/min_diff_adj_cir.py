"""
Minimum adjacent difference in a circular array
Given an array Arr of N integers arranged in a circular fashion. Your task is to find the minimum absolute difference between adjacent elements.

Input:
The input line contains T, denoting the number of testcases. Each testcase contains two lines. The first line contains N(size of array). The second line contains N elements of array separated by space.

Output:
For each testcase in new line print the minimum absloute difference.

User Task:
The task is to complete the function minAdjDiff() which returns the minimum difference between adjacent elements in circular array.

Constraint:
1 <= T <= 100
2 <= N <= 106
-106 <= Arr[i] <= 106

Example:
Input:
3
7
8 -8 9 -9 10 -11 12
8
10 -3 -4 7 6 5 -4 -1
8
-1 40 -14 7 6 5 -4 -1

Output:
4
1
0

Explanation:
Testcase 1: The absolute difference between adjacent elements in the given array are as such: 16 17 18  19 21 23 4(first and last). Among the calculated absolute difference the minimum is 4.
Testcase 2: The absolute difference between adjacent elements in the given array are as such: 13 1 11 1 1 9 3 11(first and last). Among the calculated absolute difference, the minimum is 1.
Testcase 3: The absolute difference between adjacent elements in the given array are as such: 41 54 21 1 1 9 3 0(first and last). Among the calculated absolute difference, the minimum is 0.

** For More Input/Output Examples Use 'Expected Output' option **
"""

def minAdjDiff(arr, n):
    s=[]
    for x in range(n-1):
        s.append(abs(arr[x]-arr[x+1]))
    s.append(abs(arr[n-1]-arr[0]))
    return(min(s))
