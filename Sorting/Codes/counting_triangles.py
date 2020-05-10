"""
Count possible triangles
Given an unsorted array arr of positive integers. Find the number of triangles that can be formed with three different array elements as lengths of three sides of triangles. 

Input: 
The first line of the input contains T denoting the number of testcases. First line of test case is the length of array N and second line of test case are its elements.

Output:
Number of possible triangles are displayed to the user.

Your Task:
This is a function problem. You only need to complete the function findNumberOfTriangles() that takes N as parameter and returns the count of total possible triangles.

Constraints:
1 <= T <= 10
3 <= N <= 103
1 <= arr[i] <= 103

Example:
Input:
2
3
3 5 4
5
6 4 9 7 8
Output:
1
10

Explanation:
Testcase 1: A triangle is possible with all the elements 5, 3 and 4.
Testcase 2: There are 10 triangles possible with the given elements like (6,4,9) , (6,7,8),...
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def findNumberOfTriangles(arr,n):
    n = len(arr) 
    arr.sort() 
    count = 0
    for i in range(0, n-2): 
        k = i + 2
        for j in range(i + 1, n): 
            while (k < n and arr[i] + arr[j] > arr[k]): 
                k += 1
            if(k>j): 
                count += k - j - 1
    return count 
