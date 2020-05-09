"""
Majority Element
Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.

Input:  
The first line of the input contains T denoting the number of testcases. The first line of the test case will be the size of array and second line will be the elements of the array.

Output: 
For each test case the output will be the majority element of the array. Output "-1" if no majority element is there in the array.

User Task:
The task is to complete the function findMajority() which finds the majority element in the array. If no majority exists, return -1.

Constraints:
1 <= T<= 100
1 <= N <= 107
0 <= Ai <= 106

Example:
Input:
2
5
3 1 3 3 2
3
1 2 3
Output:
3
-1

Explanation:
Testcase 1: Since, 3 is present more than N/2 times, so it is the majority element.
Testcase 2: Since, each element in {1,2,3} appears only once so there is no majority element.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def majorityElement(A,N):
    count = 1
    res = 0
    for x in range(1,N):
        if(A[res]!=A[x]):
            count-=1
            if(count<=0):
                res=x
                count=1
        else:
            count+=1
    if(count>=1 and A.count(A[res])>N//2):
        return(A[res])
    return -1
