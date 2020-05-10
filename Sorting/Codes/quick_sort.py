"""
Quick Sort
Given an array arr[] of size N. The task is to complete partition() function which is used to implement Quick Sort.

Input:
First line of the input denotes number of test cases 'T'. First line of the test case is the size of array and second line consists of array elements.

Output:
For each testcase, in a new line, print the sorted array.

Your Task:
This is a function problem. You only need to complete the function partition(). The printing is done automatically by the driver code.

Constraints:
1 <= T <= 50
1 <= N <= 103
1 <= arr[i] <= 104

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
Testcase 1: Elements in sorted form are 1 3 4 7 9.
Testcase 2: Elements in sorted form are 1 2 3 4 5 6 7 8 9 10.

** For More Input/Output Examples Use 'Expected Output' option **
"""

def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def partition(arr,low,high):
    # Hoare Partition: O(n),O(1) Not stable.. hence Quick sort is also Unstable
    # pivot is assumed at position 1
    # i=0 and j=7
    # i+=1 and j-=1 and keep on swapping wrt the requirements
    # the pivot might not be in the middle when we do hoarse Partition
    i = low-1         
    pivot = arr[high]     
    for j in range(low , high): 
        if arr[j] < pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return (i+1) 