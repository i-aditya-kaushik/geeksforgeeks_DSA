"""
Longest Subarray Of Evens And Odds
You are given an array of size n. Find the maximum possible length of a subarray such that its elements are arranged alternately either as even and odd or odd and even .

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input. The first line contains n. The second line contains the elements of the array.

Output Format:
For each testcase, in a new line, print the maximum length of the subarray.

Your Task:
This is a function problem. You don't need to take any input. Just complete the function maxEvenOdd() that returns the maximum length.

Constraints:
1 <= T <= 100
1 <= n <= 103
1 <= Ai <= 103

Example:
Input:
3
5
10 12 14 7 8
2
4 6
3
1 2 3

Output:
3
1
3

Example:
Testcase 1: The max length of subarray is 3 and the subarray is {14 7 8}. Here the array starts as an even element and has odd and even elements alternately.
Testcase 2: The array contains {4 6}. So, we can only choose 1 element as that will be the max length subarray.
Testcase 3: The subarray with max length 3 is {1 2 3}. It starts with an odd element and has even and odd elements alternately.

** For More Input/Output Examples Use 'Expected Output' option **
"""

def maxEvenOdd(arr,n):
    p=[0]*n
    for x in range(n):
        if(arr[x]%2==0):
            p[x] = 1
        else:
            p[x] = -1
    sum = 1
    sum2 = 1
    for x in range(1,n):
        if(p[x-1]!=p[x]):
            sum+=1
        else:
            if(sum2<sum):
                sum2=sum
            sum=1
    return(max(sum,sum2))