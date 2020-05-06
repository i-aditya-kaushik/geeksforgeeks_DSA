"""
Digits In Factorial
Given an integer N. The task is to find the number of digits that appear in its factorial, where factorial is defined as, factorial(n) = 1*2*3*4……..*N and factorial(0) = 1.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of one line. The first line of each test case consists of an integer N.

Output:
Corresponding to each test case, in a new line, print the number of digits that appear in its factorial.

Your Task:
This is a function problem. You only need to complete the function digitsInFactorial() that takes N as parameter and returns number of digits in factorial of N.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 104

Example:
Input:
2
5
120
Output:
3
199

Explanation:
Testcase 1: Factorial of 5 is 120. Number of digits in 120 is 3 (1, 2, and 0).
Testcase 2: Number of digits in 120! is 199.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

import math

def digitsInFactorial(n):
    if (n < 0): 
        return 0
  
    if (n <= 1): 
        return 1 
  
    digits = 0; 
    for i in range(2, n + 1): 
        digits += math.log10(i) 
  
    return math.floor(digits) + 1 

assert digitsInFactorial(2) == 1
assert digitsInFactorial(5) == 3
assert digitsInFactorial(120) == 199

print('The code ran Correctly')