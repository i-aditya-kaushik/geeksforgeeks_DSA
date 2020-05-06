"""
Factorial Of Number
Given a positive integer N. The task is to find factorial of N.

Input:
The first line contains an integer 'T' denoting the total number of test cases. T testcases follow. In each test cases, it contains an integer 'N'.

Output:
For each testcase, in a new line, print the factorial of N.

Your Task:
This is a function problem. You just need to complete the function factorial() that takes N as parameter and returns factorial of N.

Constraints:
1 <= T <= 100
0 <= N <= 18

Example:
Input:
3
1
4
13

Output:
1
24
6227020800

Explanation:
Testcase 1: Factorial of 1 is 1.
Testcase 2: Factorial of 4 is 4 * 3 * 2 * 1 = 24.
Testcase 3: Factorial of 13 is 13 * 12 * 11 * ..* 2 * 1 = 6227020800
"""
def factorial(N):
    c=1
    for x in range(2,N+1):
        c*=x
    return(c)

assert factorial(1) == 1
assert factorial(4) == 24
assert factorial(13) == 6227020800

print('The code ran Correctly')