"""
Inversion of array
Given an array arr[] consisting of N positive integers. The task is to find inversion count of array.

Inversion Count : For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, the size of array. The second line of each test case contains N elements.

Output:
Print the inversion count of array.

Your Task:
This is a function problem. You only need to complete the function inversionCount() that takes A and N as parameters and returns inversion count.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
1 ≤ C ≤ 1018

Example:
Input:
3
5
2 4 1 3 5
5
2 3 4 5 6
3
10 10 10
Output:
3
0
0

Explanation:
Testcase 1: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
Testcase 2: As the sequence is already sorted so there is no inversion count.
Testcase 3: As all the elements of array are same , so there is no inversion count.

** For More Input/Output Examples Use 'Expected Output' option **
"""

def Inversion_Count(arr, n): 
    temp_arr = [0]*n 
    return _mergeSort(arr, temp_arr, 0, n-1) 

def _mergeSort(arr, temp_arr, left, right): 
    inv_count = 0
    if left < right: 
        mid = (left + right)//2
        inv_count += _mergeSort(arr, temp_arr, left, mid) 
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right) 
        inv_count += merge(arr, temp_arr, left, mid, right) 
    return inv_count 
  
def merge(arr, temp_arr, left, mid, right): 
    i = left     
    j = mid + 1 
    k = left      
    inv_count = 0
    while i <= mid and j <= right: 
        if arr[i] <= arr[j]: 
            temp_arr[k] = arr[i] 
            k += 1
            i += 1
        else: 
            temp_arr[k] = arr[j] 
            inv_count += (mid-i + 1) 
            k += 1
            j += 1
    while i <= mid: 
        temp_arr[k] = arr[i] 
        k += 1
        i += 1
    while j <= right: 
        temp_arr[k] = arr[j] 
        k += 1
        j += 1
    for loop_var in range(left, right + 1): 
        arr[loop_var] = temp_arr[loop_var] 
          
    return inv_count  