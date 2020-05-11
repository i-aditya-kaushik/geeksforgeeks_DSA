"""
Three way partitioning
Given an array A[] and a range [a, b]. The task is to partition the array around the range such that array is divided in three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the q.
The individual elements of three sets can appear in any order. You are required to return the modified arranged array.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. First line of each test case contains an integer N denoting the size of the array. Then in the next line are N space separated values of the array (A[]).Then the next line contains two space separated integers which denote the range(a,b).

Output:
For each test case the output will be 1 if the array is properly arranged else it would be 0.

User Task:
The task is to complete the function threeWayPartition() which should segregate the elements as required. The function returns an array.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[i] <= 106

Example:
Input:
2
5
1 2 3 3 4
1 2
3
1 2 3
1 3
Output:
1
1

Explanation:
Testcase 1: First, array has elements less than or equal to 1. Then , elements between 1 and 2. And, finally elements greater than 2. So, output is 1.
Testcase 2: First, array has elements less than or equal to 1. Then, elements between 1 and 3. And, finally elements greater than 3. So, output is 1.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def threeWayPartition(arr, n, a, b): 
    p = 0
    q = n - 1
    i = 0
    while i <= q: 
        if arr[i] < a: 
            temp = arr[i] 
            arr[i] = arr[p] 
            arr[p] = temp 
            i += 1
            p += 1
        elif arr[i] > b: 
            temp = arr[i] 
            arr[i] = arr[q] 
            arr[q] = temp 
            q -= 1
        else: 
            i += 1
    return(arr)