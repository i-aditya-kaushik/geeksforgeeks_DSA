"""
Possible Words From Phone Digits
Given a keypad as shown in diagram, and an N digit number. List all words which are possible by pressing these numbers.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line of each test case is N, N is the number of digits. The second line of each test case contains D[i], N number of digits.

Output:
Print all possible words from phone digits with single space.

Your Task:
This is a function problem. You just need to complete the function possibleWords that takes an array as parameter and prints all the possible words. The newline is automatically added by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 10
2 <=  D[i] <= 9

Example:
Input:
2
3
2 3 4
3
3 4 5
Output:
adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi
dgj dgk dgl dhj dhk dhl dij dik dil egj egk egl ehj ehk ehl eij eik eil fgj fgk fgl fhj fhk fhl fij fik fil

Explanation:
Testcase 1: When we press 2,3,4 then adg,adh,adi , ......,cfi are the list of possible words.
Testcase 2: When we press 3,4,5 then dgj,dgk,dgl,.......,fil are the list of possible words.

** For More Input/Output Examples Use 'Expected Output' option **
"""
hashTable = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"] 

def printWordsUtil(number, curr, output, n): 
    if(curr == n): 
        print(''.join(output), end=" ") 
        return 
    for i in range(len(hashTable[number[curr]])): 
        output.append(hashTable[number[curr]][i]) 
        printWordsUtil(number, curr + 1, output, n) 
        output.pop() 
        if(number[curr] == 0 or number[curr] == 1): 
            return
              

def possibleWords(number, n): 
    printWordsUtil(number, 0, [], n)

