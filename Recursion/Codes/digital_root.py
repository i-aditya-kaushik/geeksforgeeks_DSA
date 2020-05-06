"""
Digital Root
You are given a number n. You need to find the digital root of n.
DigitalRoot of a number is the recursive sum of its digits until we get a single digit number.
Eg.DigitalRoot(191)=1+9+1=>11=>1+1=>2

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing n.

Output:
For each testcase, in a newline, print the digital root of n.

Your Task:
This is a function problem. You only need to complete the function digitalRoot that takes n as parameter and returns the digital root of n.

Constraints:
1 <= T <= 105
1 <= n <= 107

Examples:
Input:
2
1
99999
Output:
1
9

Explanation:
Testcase 1: Digital root for 1 is 1.
Testcase 2: Digital root for 99999 is 9 + 9 + 9 + 9 + 9 => 45 => 4 + 5 => 9.

** For More Input/Output Examples Use 'Expected Output' option **
"""

def digitalRoot(num): 
    num = str(num)
    if (num == "0"): 
        return 0
    ans = 0
    for i in range (0, len(num)): 
        ans = (ans + int(num[i])) % 9
    if(ans == 0): 
        return 9
    else:  
        return ans % 9

assert digitalRoot(10514) == 2
assert digitalRoot(99999) == 9
assert digitalRoot(1) == 1

print('The code ran Correctly')