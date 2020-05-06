"""
Multiplication Under Modulo
You are given two numbers a and b. You need to find the multiplication of a and b under modulo M.
Note: Take M as 109+7

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing a and b.

Output:
For each testcase, in a new line, print multiplication of a and b under modulo M.

Your Task:
This is a function problem. You need to complete the function multiplicationUnderModulo that takes a and b as parameters and returns multiplication of a and b under modulo M.

Constraints:
1 <= T <= 100
1 <= a,b <= 263-1

Examples:
Input:
2
9223372036854775807 9223372036854775807
1000000007 1000000007
Output:
737564071
0

Explanation:
Testcase 1: (9223372036854775807*9223372036854775807 ) mod (109+7) = 737564071
Testcase 2: (1000000007*1000000007) mod (109+7)) = 0

** For More Input/Output Examples Use 'Expected Output' option **
"""

def multiplicationUnderModulo(a,b):
    '''
    :param a: given value of a
    :param b: given value of b
    :return: Integer , sum under modulo
    '''   
    M = 1000000007
    return((a*b)%M)

assert multiplicationUnderModulo(9223372036854775807,9223372036854775807) == 737564071
assert multiplicationUnderModulo(1000000007,1000000007) == 0

print('The code ran Correctly')