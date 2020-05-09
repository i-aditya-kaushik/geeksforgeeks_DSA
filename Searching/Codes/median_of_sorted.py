"""
Median of Two sorted arrays
Given two sorted arrays arr[] and brr[] of sizes N and M respectively. The task is to find the median of the two arrays when they get merged.

Input:
First line of input contains number of testcases T. First line of input contains number of elements in both arrays N and M respectively. Next two lines contains the array elements.

Output:
For each testcase, print the median of two sorted arrays. If there are total even elements, we need to print floor of average of middle two elements.

Constraints:
1 <= T <= 100
1 <= N, M <= 106
1 <= arr[i], brr[i] <= 107

Example:
Input:
4
5 6
1 2 3 4 5
3 4 5 6 7 8
2 3
1 2
2 3 4
4 4
1 2 3 4
11 12 13 14
4 3
1 2 3 4
2 3 4

Output:
4
2
7
3

Explanation:
Testcase 1: After merging two arrays, elements will be as 1 2 3 3 4 4 5 5 6 7 8. So, median is 4.
Testcase 2: After merging two arrays , elements will be 1 2 2 3 4. So, the median is 2.
Testcase 3: After merging two arrays , elemenst will be 1 2 3 4 11 12 13 14 . So the median will be floor of average of middle terms i.e, 7.
Testcase 4: After merging two arrays, elements will be 1 2 2 3 3 4 4. So, the median will be 3.

** For More Input/Output Examples Use 'Expected Output' option **
"""

import math
def median(A,N):
    
    A.sort()
    if(len(A)%2==0):
        print( math.floor((A[N//2 - 1] + A[N//2])/2) )
    else:
        print( math.floor(A[N//2]) )
        
def func(arr,n,arr2,n2):
    arrf = arr+arr2
    median(arrf,n+n2)
    
t = int(input())
for x in range(t):
    nb = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr2= list(map(int,input().split()))
    func(arr,nb[0],arr2,nb[1])