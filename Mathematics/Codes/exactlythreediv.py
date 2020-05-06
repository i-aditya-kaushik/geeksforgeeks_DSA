"""
Exactly 3 Divisors
Given a positive integer value N. The task is to find how many numbers less than or equal to N have numbers of divisors exactly equal to 3.

Input:
The first line contains integer T, denoting number of test cases. Then T test cases follow. The only line of each test case contains an integer N.

Output:
For each testcase, in a new line, print the answer of each test case.

Your Task:
This is a function problem. You only need to complete the function exactly3Divisors() that takes N as parameter and returns count of numbers less than or equal to N with exactly 3 divisors.

Constraints :
1 <= T <= 105
1 <= N <= 109

Example:
Input :
3
6
10
30
Output :
1
2
3

Explanation:
Testcase 1: There is only one number 4 which has exactly three divisors 1, 2 and 4.
Testcase 2: 4 and 9 are the only two numbers less than or equal to 10 that have exactly three divisors.
Testcase 3: 4, 9, 25 are the only numbers less than or equal to 30 that have exactly three divisors.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""
def exactly3Divisors(n):
    c=0
    prime=[True]*(n+1)
    prime[0] = prime[1] = False
    p=2
    while (p*p<=n): 
        if (prime[p] == True): 
            for i in range(p*2,n+1,p): 
                prime[i] = False  
        p+=1  
  
    i=0 
    while (i*i <= n):  
        if (prime[i]): 
            c+=1
        i+=1
    return(c)

assert exactly3Divisors(6) == 1
assert exactly3Divisors(30) == 3
assert exactly3Divisors(10) == 2

print('The code ran Correctly')