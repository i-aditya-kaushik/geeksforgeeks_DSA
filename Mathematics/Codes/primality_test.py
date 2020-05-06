"""
Primality Test
For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.

Input:
First line contains an integer, the number of test cases 'T'. T testcases follow. Each test case should contain a positive integer N.

Output:
For each testcase, in a new line, print "Yes" if it is a prime number else print "No".

Your Task:
This is a function problem. You just need to complete the function isPrime that takes N as parameter and returns True if N is prime else returns false. The printing is done automatically by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
2
5
4
Output:
Yes
No

Explanation:
Testcase 1: 5 is the prime number as it is divisible only by 1 and 5.
Testcase 2: 4 is not a prime number as it is divisible by 1 2 and 4.
"""

def isPrime(N):
    if(N==2 or N==3):
        return(1)
    if(N%2==0 or N%3==0):
        return(0)
    for x in range(5, int(N**0.5)+1 , 6):
        
        if(N%x == 0 or N%(x+2)==0):
            return(0)
    return(1)

assert isPrime(6) == 0
assert isPrime(2) == 1
assert isPrime(7) == 1

print('The code ran Correctly')