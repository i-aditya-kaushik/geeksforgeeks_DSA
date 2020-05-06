"""
Addition Under Modulo
You are given two numbers a and b. You need to find the sum of a and b under modulo M.
Note: Take M as 109+7

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing a and b.

Output:
For each testcase, in a new line, print sum of a and b under modulo M.

Your Task:
This is a function problem. You need to complete the function sumUnderModulo that takes a and b as parameters and returns sum of a and b under modulo M.

Constraints:
1 <= T <= 100
1 <= a,b <= 263-1

Examples:
Input:
2
9223372036854775807 9223372036854775807
1000000007 1000000007
Output:
582344006
0

Explanation:
Testcase 1: 9223372036854775807 + 9223372036854775807  = 18446744073709551614. Now do (18446744073709551614) mod (109+7) = 582344006
Testcase 2: 1000000007 + 1000000007  = ‭(2000000014‬)mod(109+7) = 0

** For More Input/Output Examples Use 'Expected Output' option **
"""
def sumUnderModulo(a,b):
    '''
    :param a: given value of a
    :param b: given value of b
    :return: Integer , sum under modulo
    '''
    M = 1000000007
    return((a+b)%M)

assert sumUnderModulo(9223372036854775807,9223372036854775807) == 582344006
assert sumUnderModulo(1000000007,1000000007) == 0
assert sumUnderModulo(0,0) == 0

print('The code ran Correctly')