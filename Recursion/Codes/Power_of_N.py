"""
Power Of Numbers
Given a number N, let the reverse of the number be R. The task is to print the output of the Expression power(N,R), where pow function represents N raised to power R.
Note: As answers can be very large, print the result modulo 109 + 7.

Input:
The first line of the input consists of an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of a single line containing an integer N.

Output:
Corresponding to each test case, print in a new line, the output of the expression pow as described above.

Your Task:
This is a function problem. You just need to complete the function pow that takes two parameters N and R and returns power of (N to R)mod(109 + 7)

Constraints:
1 <= T <= 103
1 <= N <= 105

Example:
Input:
2
2
12
Output:
4
864354781

Explanation:
Testcase 1: The reverse of 2 is 2 and after raising power of 2 by 2 we get 4 which gives remainder as 4 by dividing 1000000007.
Testcase 2: The reverse of 12 is 21 and 1221 , when divided by 1000000007 gives remainder as 864354781.

** For More Input/Output Examples Use 'Expected Output' option **
"""

def power(a, b): 
    number = 0
    s=str(a)
    for i in range(len(s)): 
        number = (number*10 + int(s[i])) 
        number = number % 1000000007 
  
    ans= number
    mul = ans 
    for i in range(1,b): 
        ans = (ans*mul) % 1000000007 
          
    return ans 

assert power(12,21) == 864354781
assert power(2,2) == 4

print('The code ran Correctly')