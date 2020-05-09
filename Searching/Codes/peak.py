"""
Peak element
Given an array A of N integers. The task is to find a peak element in it in O( log N ) .
An array element is peak if it is not smaller than its neighbours. For corner elements, we need to consider only one neighbour.
Note: There may be multiple peak element possible, in that case you may return any valid index.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer N. Then in the next line are N space separated values of the array.

Output:
For each test case output will be 1 if the index returned by the function is an index with peak element.

User Task:
You don't have to take any input. Just complete the provided function peakElement() and return the valid index.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[] <= 106

Example:
Input:
2
3
1 2 3
2
3 4
Output:
1
1

Explanation:
Testcase 1: In the given array, 3 is the peak element as it is greater than its neighbour.
Testcase 2: 4 is the peak element as it is greater than its neighbour elements.
 

** For More Input/Output Examples Use 'Expected Output' option
"""

def peakElement(arr, n):
    if(n==0):
        return 0
    if(n==1):
        return 0
    if(arr[0] > arr[1]):
      return 0 
    if(arr[n-1] > arr[n-2]) :
      return n-1
    for x in range(1,n-1):
      if(arr[x] > arr[x-1] and arr[x] > arr[x+1]): 
        return x