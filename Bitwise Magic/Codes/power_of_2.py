"""
Power of 2
Given a positive integer N. The task is to check if N is a power of 2. More formally, check if N can be expressed as 2x for some x.

Input:
The first line contains T denoting the number of test cases. Each test case contains a single positive integer N.

Output:
Print "YES" if it is a power of 2 else "NO" (Without the double quotes).

User Task:
Your task is to complete the function isPowerofTwo() which takes n as parameter and returns true or false by checking is given number can be represented as power of two or not.

Constraints:
1 <= T <= 100
0 <= N <= 1018

Example:
Input :
2
1
98

Output :
YES
NO

Explanation:
Testcase 1:  1 is equal to 2 raised to 0 (20 == 1).
Testcase2: 98 cannot be obtained by any power of 2.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""
import math
def isPowerofTwo(n):
    if(n<=0):
        return(0)
    if(math.log(n,2)- int(math.log(n,2))< 0.000000001):
        return(1)
    return(0)

assert isPowerofTwo(1) == 1
assert isPowerofTwo(98) == 0

print('The code ran Correctly')