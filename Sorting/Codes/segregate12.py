"""
Closet 0s 1s and 2s
Given an array A of size N containing 0s, 1s, and 2s. The task is to segregate the 0s , 1s and 2s in the array as all the 0s should appear in the first part of the array, 1s should appear in middle part of the array and finally all the 2s in the remaining part of the array.
Note: Do not use inbuilt sort function.

Input:
The first line contains an integer 'T' denoting the total number of test cases. Then T testcases follow. Each testcases contains two lines of input. The first line denotes the size of the array N. The second lines contains the elements of the array A separated by spaces.

Output: 
For each testcase, in a newline, print the sorted array.

Your Task:
This is a function problem. You only need to complete the function segragate012 that takes A and N as parameter and sorts the array.

Constraints:
1 <= T <= 500
1 <= N <= 106
0 <= Ai <= 2

Example:
Input :
2
5
0 2 1 2 0
3
0 1 0
Output:
0 0 1 2 2
0 0 1

Explanation:
Testcase 1: After segragating the 0s, 1s and 2s, we have 0 0 1 2 2 which shown in the output.
Testcase 2: For the given array input , output will be 0 0 1.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def segragate012(a,n):
    a.sort()
