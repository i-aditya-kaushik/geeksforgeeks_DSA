"""
Intersection of two sorted arrays
Given two sorted arrays arr1[] and arr2[] of sizes N and M respectively. The task is to find intersection of the two arrays.
Intersection of two arrays contains the elements common to both the arrays. The intersection should not count duplicate elements.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains size of arrays N and M. Next two lines contains N and M elements.

Output:
For each testcase, there will be a single line of output containing intersection elements of the two arrays in sorted order.

Your Task:
This is a function problem. You only need to complete the function printIntersection() that takes N and M as parameters and prints the intersection of two arrays. If the intersection is empty then print -1.
The newline is appended by driver code.

Constraints:
1 <= T <= 100
1 <= N, M <= 105
1 <= arr[i], brr[i] <= 106

Example:
Input:
3
4 5
1 2 3 4
2 4 6 7 8
5 6
1 2 2 3 4
2 2 4 6 7 8
2 3
1 2
3 4
Output:
2 4
2 4
-1

Explanation:
Testcase 1: 2 and 4 are only common elements in both the arrays.
Testcase 2: 2 and 4 are only the common elements.
Testcase 3: no common elements so print -1.

** For More Input/Output Examples Use 'Expected Output' option **
"""

def printIntersection(a, b, n, m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return: print intersection list of these two arrays or -1
    '''
    ans = (set(a).intersection(b))
    if(len(ans)==0):
        print(-1,end="")
    else:
        ans = list(ans)
        ans = sorted(ans)
        for x in ans:
            print(x,end=" ")
