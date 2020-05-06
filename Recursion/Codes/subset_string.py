"""
Power Set Using Recursion
You are given a string s. You need to print the lexicographically sorted power-set of the string.
Note: The string s contains lowercase letter of alphabet.

Input:
The first line of input contains T, denoting the number of testcases. T testcases follow. Each testcases contains one line of input containing string s.

Output:
For each testcase, in a new line, print the lexicographically sorted sub-sets of the powerset of s. Each subset is separated by a space. Each subset starts with empty string represented by " "(space).

Your Task:
This is a function problem. You only need to complete the function powerSet that takes string s as parameter and returns a vector/ArrayList of subsets. The lexicographic-sorting and printing is done automatically by the driver code.

Constraints:
1 <= T <= 100
1 <= |s| <= 10

Examples:
Input:
2
a
abc
Output:
 a
 a ab abc ac b bc c

Explanation:
Testcase1: space and a are only sets.
Testcase2: space,  a, ab, abc, ac, b, bc, c are the sets.

** For More Input/Output Examples Use 'Expected Output' option **
"""

l=[""]
def permuteRec(string, n, index = -1, curr = ""): 
  
    if index == n: 
        return
  
    if len(curr) > 0: 
        l.append(curr) 
  
    for i in range(index + 1, n): 
        curr += string[i] 
        permuteRec(string, n, i, curr) 
  
        curr = curr[:len(curr) - 1] 
  
def powerSet(string): 
    permuteRec(string, len(string))
    s= globals()['l']
    globals()['l'] = [""]
    return(s)

assert powerSet('a') == ['','a']
assert powerSet('abc') == ['','a','ab', 'abc', 'ac', 'b', 'bc', 'c']

print('The code ran Correctly')