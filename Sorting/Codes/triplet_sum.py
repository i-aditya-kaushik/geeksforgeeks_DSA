"""
Triplet Sum in Array
Given an array A[] of N numbers and another number x. The task is to determine whether or not there exist three elements in A[] whose sum is exactly x.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains n and x. Next line contains array elements.

Output:
Print "1" (without quotes) if there exist three elements in A whose sum is exactly x, else "0" (without quotes).

Your Task:
This is a function problem. You only need to complete the function find3Numbers() that takes A, arr_size, and sum as parameters and returns true or false.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 103
1 ≤ A[i] ≤ 105

Example:
Input:
2
6 13
1 4 45 6 10 8
5 10
1 2 4 3 6
Output:
1
1

Explanation:
Testcase 1: There is one triplet with sum 13 in the array. Triplet elements are 1, 4, 8, whose sum is 13.
Testcase 2: There is one triplet with sum 10 in the array. Triplet elements are 1 , 3 , 10.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def find3Numbers(a, n, sum): 
    a.sort() 
    # print(a)
    for i in range(0, n-2): 
        l = i + 1 
        r = n-1 
        while (l < r): 
            if( a[i] + a[l] + a[r] == sum): 
                return 1
            elif (a[i] + a[l] + a[r] < sum): 
                l += 1
            else: 
                r -= 1
    return 0

print(find3Numbers([1,4,45,6,10,8],6,13))