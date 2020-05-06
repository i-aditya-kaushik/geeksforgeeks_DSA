"""
Count total set bits
You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. The first line of each test case is N.

Output:
For each testcase, in a new line, print the total count of all bits.

User Task:
The task is to complete the function countSetBits() that takes n as parameter and returns the count of all bits.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 103

Example:
Input:
2
4
17
Output:
5
35

Explanation:
Testcase1:
An easy way to look at it is to consider the number, n = 4:
0 0 0 = 0 set bits
0 0 1 = 1 set bits
0 1 0 = 1 set bits
0 1 1 = 2 set bits
1 0 0 = 1 set bits
Therefore, the total number of set bits is 5.
Testcase 2: From numbers 1 to 17(both inclusive), the total number of set bits is 35.

** For More Input/Output Examples Use 'Expected Output' option **
"""

def countSetBits(n):
    c=0
    for x in range(n+1):
        if(x%2==1):
            c+=1
        while(x!=0):
            x=x>>1
            if(x%2==1):
                c+=1
    return(c)
    
assert countSetBits(4) == 5
assert countSetBits(17) == 35

print('The code ran Correctly')