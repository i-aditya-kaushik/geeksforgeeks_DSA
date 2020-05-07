"""
Max and Second Max
Given an array arr[] of size N of positive integers which may have duplicates. The task is to find maximum and second maximum from the array, and both of them should be distinct, so If no second max exists, then second max will be -1.

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains size of array N, next line contains array elements.

Output Format:
For each testcase, print the maximum and second maximum from the array. IF no second max exists, print "-1" for second max.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= arr[i] <= 106

User Task:
The task is to complete the function largestAndSecondLargest(), which should print maximum and second maximum element from the array.

Example:
Input:
3
5
1 2 3 4 5
3
2 1 2
2
5 5

Output:
5 4
2 1
5 -1

Explanation:
Testcase 1: From the given array elements, 5 is the largest and 4 is the second largest.
Testcase 2: From the given array elements, 2 is the largest and 1 is the second largest.
Testcase 3: From the given array elements, 5 is the largest and -1 is the second largest.

 

** For More Input/Output Examples Use 'Expected Output' option **
"""
def largestAndSecondLargest(sizeOfArray, arr):
    max1 = -1
    max2 = -1
    
    ''''''''''''''''''''''''''''''''''''''''''''''''
    ''' Your code here'''
    ''' Function should print max and second max '''
    ''''''''''''''''''''''''''''''''''''''''''''''''
    s = set(arr)
    max1 = max(s)
    s.remove(max1)
    if(len(s)!=0):
        max2 = max(s)
    print (max1, max2)