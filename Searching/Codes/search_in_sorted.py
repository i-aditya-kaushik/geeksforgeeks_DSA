"""
Searching an element in a sorted array
Given a sorted array arr[] of N integers and a number K is given. The task is to check if the element K is present in the array or not.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of elements in the array and the number K seperated by space. Next line contains N elements.

Output:
For each testcase, if the element is present in the array print "1" (without quotes), else print "-1" (without quotes).

User Task:
The task is to complete the function searchInSorted() which searches for an element in sorted array.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= K <= 106
1 <= arr[i] <= 106

Example:
Input:
2
5 6
1 2 3 4 6
5 2
1 3 4 5 6

Output:
1
-1

Explanation:
Testcase 1: Since, 6 is present in the array at index 4 (0-based indexing), so output is 1.
Testcase 2: Since, 2 is not present in the array, so output is -1.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def searchInSorted(A,N,K):
#     int searchInSorted(int a[], int size, int ele) 
# {
#     if(size==0) return -1;
#     int l=0,r=size-1,mid;
    
#     while(l<=r){
#         mid=l+(r-l)/2;
#     if(a[mid]==ele) return 1; 
#     else{ 
#         if(a[mid]>ele){
#             l=l;
#             r=mid-1;
#         }
#         else{
#         l=mid+1;
#         r=r;
#         }
#     }
# }
# return -1;
# }
    if K in A:
        return(1)
    return(-1)