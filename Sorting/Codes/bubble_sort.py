"""
Bubble Sort
The task is to complete bubble function which is used to implement Bubble Sort!

Input:
First line of the input denotes the number of test cases 'T'. First line of the test case is the size of array and second line consists of array elements.

Output:
For each testcase, in a new line, print the sorted array.

Your Task:
This is a function problem. You only need to complete the function bubble that sorts the array. Printing is done automatically by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 103
1 <= arr[i] <= 103

Example:
Input:
2
5
4 1 3 9 7
10
10 9 8 7 6 5 4 3 2 1
Output:
1 3 4 7 9
1 2 3 4 5 6 7 8 9 10

Explanation:
Testcase 1: 1 3 4 7 9 are in sorted form.
Testcase 2: For the given input , 1 2 3 4 5 6 7 8 9 10 are in sorted form.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""
def bubble(arr, i, n):
    for x in range(n-1):
        if(arr[x]>arr[x+1]):
            temp = arr[x+1]
            arr[x+1]=arr[x]
            arr[x]=temp
    return(arr)