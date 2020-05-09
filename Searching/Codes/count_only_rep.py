"""
Count only Repeated
Given an array arr[] of N positive integers, where elements are consecutive (sorted). Also, there is a single element which is repeating X (any variable) number of times. Now, the task is to find the element which is repeated and number of times it is repeated.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of elements in the array N. Next line contains the array elements.

Output:
For each testcase, there will be a single line containing the element which is repeated and the number of times it is repeated, seperated by space.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= arr[i] <= 1015

Input:
2
5
1 2 3 3 4
5
2 3 4 5 5

Output:
3 2
5 2

Example:
Testcase 1: In the given array, 3 is occuring two times.So the output is 3 2.
Testcase 2: In the given array, 5 is occuring two times.So the output is 5 2.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""
def func(arr,n):
    for x in range(n-1):
        if(arr[x+1]==arr[x]):
            return(str(arr[x])+" "+str(arr.count(arr[x])))


t = int(input())
for x in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(func(arr,n))