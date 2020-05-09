"""
Maximum Water Between Two Buildings
Given an integer array height of size N which represents the heights of N buildings, the task is to delete N-2 buildings such that the water that can be trapped between the remaining two building is maximum. Please note that the total water trapped between two buildings is gap between them (number of buildings removed) multiplied by height of the smaller building.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input. The first line contains N denoting the number of elements in the array. The second line contains the elements of the array.

Output Format:
For each testcase, in a new line, print the maximum amount of water that can be stored between any two buildings after you remove n-2 buildings.

Your Task:
This is a function problem. You need to complete the function maxWater that takes height array and size N as parameters and returns the max water that can be stored. The printing is done by the driver code.

Constraints:
1 <= T <= 100
1 <= heighti <= 106
1 <= N <= 105

Examples:
Input:
2
6
2 1 3 4 6 5
2
2 1
Output:
8
0

Explanation:
Testcase1: The heights are 2 1 3 4 6 5. So we choose the following buildings 2 1 3 4 6 5  and remove others. So total removed buildings is equal to 4, now the height of smaller one is 2. So answer is 2 * removed buildings = 2*4 = 8. There is no answer greater than this.
Testcase2: The heights are 2 1. So we choose the following buildings 2 5  and remove others. But there is no other buildings to be removed so total removed = 0.  Now the height of smaller one is 2. So answer is 2 * removed buildings = 2*0 = 0.

** For More Input/Output Examples Use 'Expected Output' option **
"""

#FINAL CODE: 1.1 sec
def maxWater(height, n): 
    max_fin = 0
    lr = 0
    rr = n - 1
    while (lr < rr): 
        if (height[lr] < height[rr]):      
            max_fin = max(max_fin, (rr - lr - 1) * height[lr]) 
            lr += 1 
        elif (height[rr] < height[lr]): 
            max_fin = max(max_fin, (rr - lr - 1) * height[rr]) 
            rr -= 1 
        else:      
            max_fin = max(max_fin, (rr - lr - 1) * height[lr]) 
            lr += 1 
            rr -= 1 
    return max_fin 


#FIRST CODE: >3.12 sec
# def maxWater(height, n): 
#     if(n<=2):
#         return(0)
#     l = 0 
#     r = n
#     s=[]
#     while(r-l-2>0):
#         ma = max(height[l],height[r-1])
#         mi = min(height[l],height[r-1])
#         if(len(s)==0):
#             # print(height[l],height[r-1],mi, r-l-2, mi*(r-l-2))
#             s.append(mi*(r-l-2))
#         if(mi*(r-l-2) > s[-1]):
#             ma = max(height[l],height[r-1])
#             mi = min(height[l],height[r-1])
#             # print(height[l],height[r-1],mi, r-l-2, mi*(r-l-2))
#             s.append(mi*(r-l-2))
#         if(ma == height[r-1]):
#             l+=1
#             if(height[l]>=ma):
#                 continue
#         if(ma == height[l]):
#             r-=1
#             if(height[r]>=ma):
#                 continue
#     return(max(s))
  