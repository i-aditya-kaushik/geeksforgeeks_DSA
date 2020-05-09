"""
Subarray with given sum
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

User Task:
The task is to complete the function subarraySum() which finds starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else -1 is printed. The driver code automatically appends a new line.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= Ai <= 1010

Example:
Input:
3
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
4 15
5 7 1 2
Output:
2 4
1 5
1 4

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12.
Testcase2: sum of elements from 1st position to 5th position is 15.
Testcase 3: Sum of elements from 1st to 4th position is 15.

** For More Input/Output Examples Use 'Expected Output' option **
"""
#Python: more than expected time
def sumsub(arr,lr,rr):
    sum2 = 0
    for x in range(lr,rr+1):
        sum2+=arr[x]
    return(sum2)
#Complete this function
def subArraySum(arr, n, s): 
    lr = 0
    rr = 0
    sum= sumsub(arr,lr,rr)
    while(True):
        if(rr>n or lr>n):
            print(-1,end="")
            return
        if(sum<s):
            try:
                sum+=arr[rr+1]
            except:
                print(-1,end="")
                return
            rr+=1
        elif(sum==s):
            print(str(lr+1)+" "+str(rr+1),end=" ")
            return
        elif(sumsub(arr,lr,rr)>s):
            sum-=arr[lr]
            lr+=1
        else:
            continue
    print(-1,end="")
# Wrote the same code in C++
# void subarraySum(int arr[], int n, int s){
#     int lr = 0;
#     int rr = 0;
#     int sum= arr[0];
#     while(true){
#         if(rr>n or lr>n){
#             cout<<"-1";
#             return;}
#         if(sum<s){
#             sum+=arr[rr+1];
#             rr+=1;
#         }
#         else if(sum==s){
#             cout<<(lr+1);
#             cout<<" ";
#             cout<<(rr+1);
#             return;
#         }
#         else if(sum>s){
#             sum-=arr[lr];
#             lr+=1;
#         }
#         else{
#             continue;}
#     }
    
# }