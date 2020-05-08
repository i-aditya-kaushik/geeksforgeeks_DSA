"""
Wave Array
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array and return it. In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5..... (considering the increasing lexicographical order).

Input Format:
The first line contains an integer T, depicting total number of test cases. T testcases follow. The first line of each testcase contains an integer N depicting the size of the array. The second line contains N space separated elements of the array.

Output Format:
For each testcase, in a new line, print the array into wave-like array.

User Task:
The task is to complete the function convertToWave() which converts the given array to wave array. The newline is automatically added by the driver code.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106
0 ≤ A[i] ≤107

Example:
Input:
2
5
1 2 3 4 5
6
2 4 7 8 9 10

Output:
2 1 4 3 5
4 2 8 7 10 9

Explanation:
Testcase 1: Array elements after sorting it in wave form are 2 1 4 3 5.
Testcase 2: Array elements after sorting it in wave form are 4 2 8 7 10 9.

** For More Input/Output Examples Use 'Expected Output' option **
"""

def convertToWave(A,N):
    for x in range(0,N-1,2):
        temp = A[x+1]
        A[x+1] = A[x] 
        A[x] = temp