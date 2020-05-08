"""
Check if array is sorted and rotated
Given an array arr[] of N distinct integers, check if this array is Sorted (non-increasing or non-decreasing) and Rotated counter-clockwise. Note that input array may be sorted in either increasing or decreasing order, then rotated.
A sorted array is not considered as sorted and rotated, i.e., there should be at least one rotation.

Input:
The first line of input contains number of testcases T. Each testcase contains 2 lines, the first line contains N, the number of elements in array, and second line contains N space separated elements of array.

Output:
Print "Yes" if the given array is sorted and rotated, else Print "No", without Inverted commas.

User Task:
The task is to complete the function checkRotatedAndSorted() which checks if an array is sorted and rotated clockwise.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= A[i] <= 106

Example:
Input:
5
4
3 4 1 2
3
1 2 3
4
10 20 30 14
5
30 20 10 50 35
5
30 20 10 50 25

Output:
Yes
No
No
Yes
No

Explanation:
Testcase 1: The array is sorted (1, 2, 3, 4) and rotated twice (3, 4, 1, 2).
Testcase 2: The array is sorted (1, 2, 3) is not rotated.
Testcase 3: The array is sorted (10, 20, 30, 14) is not sorted and rotated as 14 is greater than 10.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

import sys
def checkRotatedAndSorted(arr,n):
    min1 = sys.maxsize 
    m_ind = -1
    for i in range(n): 
        if arr[i]< min1: 
            min1 = arr[i] 
            m_ind = i 
    flag1 = 1
    for i in range(1, m_ind): 
        if arr[i] < arr[i - 1]: 
            flag1 = 0
            break
    flag2 = 1
    for i in range(m_ind + 1, n) : 
        if arr[i] < arr[i - 1]: 
            flag2 = 0
            break
    if (flag1 and flag2 and 
        arr[n - 1] <= arr[0]): 
        return(1) 
    else: 
        return(0) 