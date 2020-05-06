"""
Power Using Recursion
You are given two numbers n and p. You need to find np.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing n and p.

Output:
For each testcase, in a newline, print np.

Your Task:
This is a function problem. You only need to complete the function RecursivePower that takes n and p as parameters and returns np.

Constraints:
1 <= T <= 105
1 <= n, p <= 9

Examples:
Input:
2
9 9
2 9
Output:
387420489‬
512

Explanation:
Testcase 1: 387420489 is the value obtained when 9 is raised to the power of 9.
Testcase 2: 512 is the value obtained when 2 is raised to the power of 9.  

 

** For More Input/Output Examples Use 'Expected Output' option **
"""


def RecursivePower(n,p):
    '''
    return value of n^p recursively;
    '''
    if(p==0):
        return(1)
    return(n*(RecursivePower(n,p-1)))

assert RecursivePower(2,9) == 512

print('The code ran Correctly')