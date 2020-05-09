"""
Minimum Number in a sorted rotated array
Given an array A  which is sorted and contains N distinct elements. Also, this array is rotated at some unknown point. The task is to find the minimum element in it. 
Note: Expected time complexity is O(logN).

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains the number of elements in the array arr[] as N and next line contains space separated n elements in the array arr[].

Output:
Print an integer which denotes the minimum element in the array.

User Task:
The task is to complete the function minNumber() which finds the minimum in sorted and rotated array.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= arr[i] <= 107

Example:
Input:
3
10
2 3 4 5 6 7 8 9 10 1
5
3 4 5 1 2
8
10 20 30 45 50 60 4 6
Output:
1
1
4

Explanation:
Testcase 1: The array is rotated once anti-clockwise. So minium element is at last index (n-1) which is 1.
Testcase 2: The array is rotated and the minimum element present is at index (n-2) which is 1.
Testcase 3: The array is rotated and the minimum element present is 4.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def minNumber(arr,low,high):
    #return(min(arr)) : Time: 0.03 sec
    while(high>low):
        if(arr[low+1]>=arr[low] and arr[high]>=arr[low]):
            return arr[low]
        if(arr[high]<arr[low]):
            if(arr[high]>arr[high-1]):
                high-=1
            else:
                return arr[high] #Time = 0.03 sec