"""
Count 1's in binary array
Given a binary sorted non-increasing array arr of size N. You need to print the count of 1's in the binary array.

Input:
The input line contains T, denotes the number of testcases. Each input contains two lines. The first line contains N(size of binary array). The second line contains N elements of binary array separated by space.

Output:
For each testcase in new line, print the count 1's in binary array.

User Task:
The task is to complete the function countOne() which return count of 1s in the input array.

Constraint:
1 <= T <= 100
1 <= N <= 5*106
arr[i] = 0,1

Example:
Input:
2
8
1 1 1 1 1 0 0 0
8
1 1 0 0 0 0 0 0
Output:
5
2

Explanation:
Testcase 1: Number of 1's in given binary array : 1 1 1 1 1 0 0 0 is 5.
Testcase 2: Number of 1's in given binary array : 1 1 0 0 0 0 0 0 is 2.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def countOnes(A,N):
    return(A.count(1))
